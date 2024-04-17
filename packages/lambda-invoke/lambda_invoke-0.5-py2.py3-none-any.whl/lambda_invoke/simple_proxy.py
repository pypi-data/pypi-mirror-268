import base64
import json
from io import BytesIO
from urllib.parse import parse_qs, urlparse


class _JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return obj.decode()
        # We should not fall through as Requests type checks headers for str/bytes
        return json.JSONEncoder.default(self, obj)


class SimpleProxyResponse:
    def __init__(self, invoke_response):
        self.invoke_response = invoke_response
        self._lambda_response_contents = None

    def read(self):
        self.lambda_response = self.invoke_response["Payload"].read()

    async def async_read(self):
        payload = self.invoke_response["Payload"]
        self.lambda_response = await payload.read()

    @property
    def lambda_response_contents(self):
        if not self._lambda_response_contents:
            self._lambda_response_contents = json.loads(self.lambda_response.decode())
        return self._lambda_response_contents

    def decoded_payload(self, field):
        if self.lambda_response_contents.get("isBase64Encoded", False):
            return base64.b64decode(self.lambda_response_contents[field])
        else:
            return self.lambda_response_contents[field].encode("utf-8")

    @property
    def body(self):
        if "body" in self.lambda_response_contents:
            return self.decoded_payload("body")
        elif "errorMessage" in self.lambda_response_contents:
            return self.decoded_payload("errorMessage")
        return None  # pragma: no cover

    @property
    def body_stream(self):
        return BytesIO(self.body)

    @property
    def status_code(self):
        return self.lambda_response_contents.get("statusCode", 502)

    @property
    def headers(self):
        return self.lambda_response_contents.get("headers", {})


class LambdaSimpleProxy:
    def __init__(self, region, method, url, headers, body):
        self.region = region
        self.method = method
        self.url = urlparse(url)
        self.headers = headers
        self.body = body

    @property
    def function_name(self):
        host_parts = self.url.hostname.split(".")
        if len(host_parts) > 1:
            return f"{host_parts[-1]}:{host_parts[-2]}"
        return host_parts[0]

    @property
    def request_query_string(self):
        qs = {
            "queryStringParameters": {
                key: value[0]
                for key, value in parse_qs(self.url.query).items()
                if len(value) == 1
            }
        }
        multi_value_qs = {
            key: value
            for key, value in parse_qs(self.url.query).items()
            if len(value) > 1
        }
        if multi_value_qs:
            qs["multiValueQueryStringParameters"] = multi_value_qs
        return qs

    @property
    def request_body(self):
        if not self.body:
            return False, None
        try:
            if isinstance(self.body, str):
                return False, self.body
            else:
                return False, self.body.decode("utf-8")
        except UnicodeDecodeError:
            return True, base64.b64encode(self.body).decode("utf-8")

    @property
    def request_payload(self):
        """
        Mimicking API gateway simple proxy json object that can be handled by lambda
        http://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format
        """
        base64_encoded, body = self.request_body
        return {
            "resource": self.url.path,
            "httpMethod": self.method,
            "path": self.url.path,
            "pathParameters": "",
            "headers": self.headers,
            "body": body,
            "isBase64Encoded": base64_encoded,
            "requestContext": {},
            **self.request_query_string,
        }

    @property
    def request_payload_json(self):
        return json.dumps(self.request_payload, cls=_JSONEncoder)

    @property
    def invoke_params(self):
        return {
            "FunctionName": self.function_name,
            "InvocationType": "RequestResponse",
            "LogType": "Tail",
            "Payload": self.request_payload_json,
        }

    def send(self, client):
        invoke_response = client.invoke(**self.invoke_params)
        response = SimpleProxyResponse(invoke_response)
        response.read()
        return response

    async def async_send(self, client):
        invoke_response = await client.invoke(**self.invoke_params)
        response = SimpleProxyResponse(invoke_response)
        await response.async_read()
        return response
