import unittest
from .context import api


class TestApiCall(unittest.TestCase):
    def test_api_call_returns_Ok(self):
        response = api.fetch_data(
            "http://sam-user-activity.eu-west-1.elasticbeanstalk.com")
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()