import unittest
import requests
import os
from dotenv import load_dotenv
from utils.t_manager import retrieve_token

class TestDefaultsEndpoint(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        # Load environment variables from .env file
        load_dotenv()

        # Strictly fetch URLs from environment variables
        self.TESTING_URL = os.getenv('TESTING_URL') or None
        self.PRODUCTION_URL = os.getenv('PRODUCTION_URL') or None

        # Set docstring for the test function
        self.test_defaults.__func__.__doc__ = "Test the /app/defaults endpoint for a 200 status code in both testing and production environments."

    def make_request(self, environment, endpoint, data=None):
        """Helper method to make a request based on the environment."""
        # Validate the environment
        if environment not in ['testing', 'production']:
            raise ValueError("Invalid environment provided")

        # Fetch the token based on the environment
        token = retrieve_token(environment)

        # Set up the request headers
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'{token}'
        }

        # Construct the URL for the specified endpoint based on the environment
        base_url = self.TESTING_URL if environment == 'testing' else self.PRODUCTION_URL
        if not base_url:
            raise ValueError(f"{environment.upper()}_URL environment variable is not set.")

        url = f"{base_url}/app/{endpoint}"

        response = requests.get(url, headers=headers, json=data)

        return response
    
    def test_defaults(self):
        """Test the /app/defaults endpoint for a 200 status code in both testing and production environments."""
        # Ensure that required environment variables are set
        self.assertIsNotNone(self.TESTING_URL, "TESTING_URL environment variable is not set.")
        self.assertIsNotNone(self.PRODUCTION_URL, "PRODUCTION_URL environment variable is not set.")

        # Test in the testing environment
        try:
            response_testing = self.make_request('testing', 'defaults')
            self.assertEqual(response_testing.status_code, 200, "/app/defaults endpoint test failed in testing environment")
        except AssertionError as e:
            error_message = f"Test Failed: {self._testMethodName} - {str(e)}"
            self.failure_reason = error_message
            raise

        # Test in the production environment
        try:
            response_production = self.make_request('production', 'defaults')
            self.assertEqual(response_production.status_code, 200, "/app/defaults endpoint test failed in production environment")
        except AssertionError as e:
            error_message = f"Test Failed: {self._testMethodName} - {str(e)}"
            self.failure_reason = error_message
            raise

if __name__ == "__main__":
    unittest.main()
