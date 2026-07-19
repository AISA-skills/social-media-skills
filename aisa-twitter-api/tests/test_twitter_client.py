"""Regression tests for the AIsa and optional Xquik read clients."""

import importlib.util
import io
import json
import pathlib
import sys
import unittest
import urllib.error
from unittest.mock import patch


MODULE_PATH = pathlib.Path(__file__).parents[1] / "scripts" / "twitter_client.py"
SPEC = importlib.util.spec_from_file_location("aisa_twitter_client", MODULE_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError("Unable to load twitter_client.py")
twitter_client = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = twitter_client
SPEC.loader.exec_module(twitter_client)


class Response:
    """Minimal context-managed urllib response for request tests."""

    def __init__(self, payload):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, _exception_type, _exception, _traceback):
        return False

    def read(self):
        return json.dumps(self.payload).encode("utf-8")


class TwitterClientTests(unittest.TestCase):
    """Cover shared request behavior and the optional Xquik client."""

    def test_aisa_request_omits_empty_query_values(self):
        with patch.object(
            twitter_client.urllib.request,
            "urlopen",
            return_value=Response({"success": True}),
        ) as urlopen:
            result = twitter_client.TwitterClient("aisa-key")._request(
                "GET",
                "/twitter/example",
                params={"cursor": "", "limit": 0, "query": "agents"},
            )

        self.assertTrue(result["success"])
        request = urlopen.call_args.args[0]
        self.assertEqual(
            request.full_url,
            "https://api.aisa.one/apis/v1/twitter/example?limit=0&query=agents",
        )

    def test_json_http_error_is_always_unsuccessful(self):
        error = urllib.error.HTTPError(
            "https://api.aisa.one/example",
            429,
            "Too Many Requests",
            {},
            io.BytesIO(b'{"error":{"code":"RATE_LIMITED"}}'),
        )

        with patch.object(twitter_client.urllib.request, "urlopen", side_effect=error):
            result = twitter_client.TwitterClient("aisa-key")._request(
                "GET", "/twitter/example"
            )

        self.assertFalse(result["success"])
        self.assertEqual(result["error"]["code"], "RATE_LIMITED")

    def test_non_json_http_error_preserves_status_and_body(self):
        error = urllib.error.HTTPError(
            "https://api.aisa.one/example",
            502,
            "Bad Gateway",
            {},
            io.BytesIO(b"upstream unavailable"),
        )

        result = twitter_client.http_error_result(error)

        self.assertFalse(result["success"])
        self.assertEqual(result["error"], {"code": "502", "message": "upstream unavailable"})

    def test_xquik_request_uses_expected_route_query_and_header(self):
        with patch.object(
            twitter_client.urllib.request,
            "urlopen",
            return_value=Response({"tweets": [], "has_next_page": False, "next_cursor": ""}),
        ) as urlopen:
            result = twitter_client.XquikClient(
                "xquik-key", "https://example.test/api/v1/"
            ).search("AI agents", "Top", "next", 20)

        self.assertEqual(result["tweets"], [])
        request = urlopen.call_args.args[0]
        self.assertEqual(
            request.full_url,
            "https://example.test/api/v1/x/tweets/search?q=AI+agents&queryType=Top&cursor=next&limit=20",
        )
        self.assertEqual(request.get_header("X-api-key"), "xquik-key")

    def test_xquik_summary_preserves_api_errors(self):
        client = twitter_client.XquikClient("xquik-key")
        with patch.object(
            client,
            "search",
            return_value={"success": False, "error": "insufficient_credits"},
        ):
            result = client.search_summary("agents")

        self.assertFalse(result["success"])
        self.assertEqual(result["error"], "insufficient_credits")

    def test_xquik_summary_normalizes_supported_author_shapes(self):
        client = twitter_client.XquikClient("xquik-key")
        response = {
            "tweets": [
                {
                    "id": "1",
                    "text": "nested",
                    "author": {"username": "alice"},
                    "createdAt": "2026-07-18T00:00:00Z",
                    "url": "https://x.com/alice/status/1",
                },
                {"id": "2", "text": "flat", "userName": "bob"},
            ],
            "has_next_page": True,
            "next_cursor": "cursor-2",
        }
        with patch.object(client, "search", return_value=response):
            result = client.search_summary("agents")

        self.assertTrue(result["success"])
        self.assertEqual(result["count"], 2)
        self.assertEqual([tweet["author"] for tweet in result["tweets"]], ["alice", "bob"])
        self.assertTrue(result["has_next_page"])
        self.assertEqual(result["next_cursor"], "cursor-2")


if __name__ == "__main__":
    unittest.main()
