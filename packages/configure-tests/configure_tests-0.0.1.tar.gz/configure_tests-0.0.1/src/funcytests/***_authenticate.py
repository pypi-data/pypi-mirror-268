import unittest
import requests
import os
from dotenv import load_dotenv

class TestAuthenticate(unittest.TestCase):

    def setup(self):
        """Set up the test environment."""
        load_dotenv()

        # Fetch environment variables for testing and production URLs
        self.testing_url = os.getenv("TESTING_URL")
        self.production_url = os.getenv("PRODUCTION_URL")

        # Set docstrings for test functions
        self.test_successful_authentication.__func__.__doc__ = "Test for successful authentication"
        self.test_unsuccessful_authentication.__func__.__doc__ = "Test for unsuccessful authentication"

    def test_successful_authentication(self):
        """Test for successful authentication."""
        # Ensure URLs are set
        if self.testing_url is None or self.production_url is None:
            raise ValueError("Testing or Production URL not set. Make sure to set them before running tests.")

        # Define activation tokens for testing and production
        testing_activation_token = "apitesting_test"
        production_activation_token = "apitesting_production"

        # Loop through testing and production environments
        for base_url, activation_token in zip((self.testing_url, self.production_url), (testing_activation_token, production_activation_token)):
            url = f"{base_url}/app/authenticate"
            headers = {'Content-Type': 'application/json'}
            data = {
                "activation_code": activation_token,
                "device": {
                    "app_version": "1.0",
                    "device_id": "some-random-string",
                    "device_type": "TEST",
                    "os_version": "0.0.0",
                }
            }

            # Make the authentication request
            response = requests.post(url, json=data, headers=headers)

            try:
                # Check if the response is successful and contains auth_token
                self.assertEqual(response.status_code, 200, "Authentication failed")
                response_data = response.json()
                self.assertIn("auth_token", response_data, "Auth token not found in response")
            except AssertionError as e:
                error_message = f"Test Failed: {self._testMethodName} - {str(e)}"
                self.failure_reason = error_message
                raise

    def test_unsuccessful_authentication(self):
        """Test for unsuccessful authentication."""
        # Ensure URLs are set
        if self.testing_url is None or self.production_url is None:
            raise ValueError("Testing or Production URL not set. Make sure to set them before running tests.")

        # Define activation tokens for testing and production
        testing_activation_token = "testing_activation_token"
        production_activation_token = "production_activation_token"

        # Loop through testing and production environments
        for base_url, activation_token in zip((self.testing_url, self.production_url), (testing_activation_token, production_activation_token)):
            url = f"{base_url}/app/authenticate"
            headers = {'Content-Type': 'application/json'}
            data = {
                "activation_code": activation_token,
                "device": {
                    "device_id": "API_TESTING",
                    "app_version": "0.0.0",
                    "os_version": "0.0.0",
                    "device_type": "API_TESTING"
                }
            }

            # Make the authentication request
            response = requests.post(url, json=data, headers=headers)

            try:
                # Check if the response indicates unsuccessful authentication
                if response.status_code != 401:
                    self.fail(f"Unexpected status code: {response.status_code}")
            except AssertionError as e:
                error_message = f"Test Failed: {self._testMethodName} - {str(e)}"
                self.failure_reason = error_message
                raise

if __name__ == "__main__":
    unittest.main()
