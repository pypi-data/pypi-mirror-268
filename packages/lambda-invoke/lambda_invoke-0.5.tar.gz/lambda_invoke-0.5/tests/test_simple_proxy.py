import json
from datetime import datetime
from unittest import IsolatedAsyncioTestCase, TestCase
from unittest.mock import DEFAULT, AsyncMock, MagicMock, patch

from lambda_invoke import LambdaSimpleProxy
from lambda_invoke.simple_proxy import _JSONEncoder

BINARY_PAYLOAD = bytes([0xDE, 0xAD, 0xBE, 0xEF] * 100)
UNICODE_PAYLOAD = "\u2620\U0001F42E" * 100
STATUS_UP_PAYLOAD = b'{"body": "ewogICJzdGF0dXMiOiAiVVAiCn0K", "isBase64Encoded": "true", "statusCode": 200, "headers": {"Content-Type": "application/json", "X-Request-ID": "", "Content-Length": "21"}}'  # noqa: E501


class PatcherBase:
    def add_patcher(self, target, new=DEFAULT, new_callable=None):
        target_patch = patch(target, new, new_callable)
        self.addCleanup(target_patch.stop)
        return target_patch.start()


class TestSimpleProxy(PatcherBase, TestCase):
    def setUp(self):
        self.mock_client = MagicMock()
        self.set_response_payload(
            b'{"body": "ewogICJmb3JtIjoge30sIAogICJoZWFkZXJzIjogIlVzZXItQWdlbnQ6IHB5dGhvbi1yZXF1ZXN0cy8yLjI1LjFcclxuQWNjZXB0LUVuY29kaW5nOiBnemlwLCBkZWZsYXRlXHJcbkFjY2VwdDogKi8qXHJcbkNvbm5lY3Rpb246IGtlZXAtYWxpdmVcclxuXHJcbiIsIAogICJwYXJhbSI6ICJmb28iLCAKICAicXVlcnlfc3RyaW5ncyI6IHt9Cn0K", "isBase64Encoded": "true", "statusCode": 200, "headers": {"Content-Type": "application/json", "X-Request-ID": "", "Content-Length": "195"}}'  # noqa: E501
        )

    def set_response_payload(self, payload):
        self.mock_client.invoke().__getitem__().read.return_value = payload

    def extract_sent_payload(self, key):
        return json.loads(self.mock_client.invoke.call_args[1]["Payload"])[key]

    def test_200_ok(self):
        self.set_response_payload(STATUS_UP_PAYLOAD)
        proxy = LambdaSimpleProxy("us-east-1", "get", "http://example/", {}, None)
        response = proxy.send(self.mock_client)
        assert response.status_code == 200
        assert response.body_stream.read() == b'{\n  "status": "UP"\n}\n'
        assert response.headers["Content-Type"] == "application/json"
        assert self.mock_client.invoke.call_args.kwargs.get("FunctionName") == "example"

    def test_200_ok_basic_auth_ignored(self):
        self.set_response_payload(STATUS_UP_PAYLOAD)
        proxy = LambdaSimpleProxy(
            "us-east1", "get", "http://foo:bar@example/", {}, None
        )
        response = proxy.send(self.mock_client)
        assert response.status_code == 200
        assert self.mock_client.invoke.call_args.kwargs.get("FunctionName") == "example"

    def test_200_ok_alias(self):
        self.set_response_payload(STATUS_UP_PAYLOAD)
        proxy = LambdaSimpleProxy(
            "us-east1", "get", "http://foo:bar@v1.example/", {}, None
        )
        response = proxy.send(self.mock_client)
        assert response.status_code == 200
        assert (
            self.mock_client.invoke.call_args.kwargs.get("FunctionName") == "example:v1"
        )

    def test_json(self):
        proxy = LambdaSimpleProxy("us-east-1", "get", "http://example/", {}, None)
        response = proxy.send(self.mock_client)
        assert response.status_code == 200

    def test_str_body(self):
        proxy = LambdaSimpleProxy("us-east-1", "get", "http://example/", {}, "foo")
        response = proxy.send(self.mock_client)
        assert response.status_code == 200

    def test_utf8_body(self):
        proxy = LambdaSimpleProxy("us-east-1", "get", "http://example/", {}, b"foo")
        response = proxy.send(self.mock_client)
        assert response.status_code == 200

    def test_binary_body(self):
        proxy = LambdaSimpleProxy(
            "us-east-1", "get", "http://example/", {}, BINARY_PAYLOAD
        )
        response = proxy.send(self.mock_client)
        assert response.status_code == 200

    def test_lambda_exception(self):
        self.set_response_payload(
            b'{"errorMessage": "Unable to import module \'service\': No module named \'foobarbaz\'", "errorType": "Runtime.ImportModuleError", "stackTrace": [] }'  # noqa: E501
        )
        proxy = LambdaSimpleProxy("us-east-1", "get", "http://example/", {}, None)
        response = proxy.send(self.mock_client)
        assert response.status_code == 502
        assert (
            response.body
            == b"Unable to import module 'service': No module named 'foobarbaz'"
        )

    def test_custom_header_byte_string(self):
        header_data = {"foo": b"bar"}
        proxy = LambdaSimpleProxy(
            "us-east-1", "get", "http://example/", header_data, None
        )
        response = proxy.send(self.mock_client)
        assert response.status_code == 200

    def test_json_serialize_fallthrough(self):
        json.dumps({"foo": "bar"}, cls=_JSONEncoder)
        with self.assertRaises(TypeError):
            json.dumps({"foo": datetime.fromisoformat("2021-06-19")}, cls=_JSONEncoder)

    def test_query_string(self):
        proxy = LambdaSimpleProxy(
            "us-east-1", "get", "http://example/?a=1&b=2", {}, None
        )
        response = proxy.send(self.mock_client)
        assert response.status_code == 200
        sent_payload = json.loads(
            self.mock_client.invoke.call_args.kwargs.get("Payload")
        )
        assert sent_payload.get("queryStringParameters") == {"a": "1", "b": "2"}
        assert "multiValueQueryStringParameters" not in sent_payload.keys()

    def test_mix_multi_value_query_string(self):
        proxy = LambdaSimpleProxy(
            "us-east-1", "get", "http://example/?a=1&b=2&a=bob", {}, None
        )
        response = proxy.send(self.mock_client)
        assert response.status_code == 200
        sent_payload = json.loads(
            self.mock_client.invoke.call_args.kwargs.get("Payload")
        )
        assert sent_payload.get("queryStringParameters") == {"b": "2"}
        assert sent_payload.get("multiValueQueryStringParameters") == {
            "a": ["1", "bob"]
        }

    def test_only_multi_value_query_string(self):
        proxy = LambdaSimpleProxy(
            "us-east-1", "get", "http://example/?a=1&a=bob", {}, None
        )
        response = proxy.send(self.mock_client)
        assert response.status_code == 200
        sent_payload = json.loads(
            self.mock_client.invoke.call_args.kwargs.get("Payload")
        )
        assert sent_payload.get("queryStringParameters") == {}
        assert sent_payload.get("multiValueQueryStringParameters") == {
            "a": ["1", "bob"]
        }


class TestSimpleProxyAsync(IsolatedAsyncioTestCase):
    async def test_200_ok_async(self):
        proxy = LambdaSimpleProxy("us-east-1", "get", "http://example/", {}, None)
        mock_client = MagicMock()
        mock_invoke_result = MagicMock()
        mock_client.invoke = AsyncMock(side_effect=mock_invoke_result)
        mock_invoke_result().__getitem__().read = AsyncMock(
            return_value=STATUS_UP_PAYLOAD
        )

        response = await proxy.async_send(mock_client)
        assert response.status_code == 200
        assert response.body_stream.read() == b'{\n  "status": "UP"\n}\n'
        assert response.headers["Content-Type"] == "application/json"
