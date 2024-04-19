import unittest
import requests
import os
from dotenv import load_dotenv
from utils.t_manager import retrieve_token

import logging
import json

class TestRegister(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        # Load environment variables from .env file
        load_dotenv()

        # Strictly fetch URLs from environment variables
        self.TESTING_URL = os.getenv('TESTING_URL')
        self.PRODUCTION_URL = os.getenv('PRODUCTION_URL')

        # Set docstrings for test functions
        self.test_successful_registration.__func__.__doc__ = "Test for successful registration."
        self.test_unsuccessful_registration.__func__.__doc__ = "Test for unsuccessful registration."

    def make_request(self, environment, data=None):
        """
        Helper method to make a request based on the environment.

        Parameters:
        - environment (str): The environment ('testing' or 'production').
        - data (dict): The data to be sent in the request.

        Returns:
        - response: The response object from the request.
        """
        if environment == 'testing':
            url = self.TESTING_URL + '/portal/register'
            token = retrieve_token('testing')
        else:  # 'production'
            url = self.PRODUCTION_URL + '/portal/register'
            token = retrieve_token('production')

        headers = {
            'Content-Type': 'application/json',
            # 'Authorization': f'{token}'
        }

        # Log the request data
        logging.info(f"Request URL: {url}")
        logging.info(f"Request Headers: {headers}")
        logging.info(f"Request Data: {json.dumps(data)}")

        # Make the request
        response = requests.post(url, json=data, headers=headers)

        # Log the response data
        logging.info(f"Response Status Code: {response.status_code}")
        logging.info(f"Response Data: {json.dumps(response.json())}")

        return response

    def test_successful_registration(self):
        """Test for successful registration."""

        # Ensure URLs are set
        assert self.TESTING_URL is not None, "TESTING_URL environment variable is not set."
        assert self.PRODUCTION_URL is not None, "PRODUCTION_URL environment variable is not set."

        # Define the data payload for the successful test
        data = {
            "email": "jroscoe@wavelynxtech.com",
            "first_name": "Sample",
            "last_name": "Simple",
            "company": "Sample Experiences"
        }

        try:
            # Test with the testing environment
            response = self.make_request('testing', data=data)
            self.assertEqual(response.status_code, 200, "Testing environment failed")
        except AssertionError as e:
            error_message = f"Test Failed: {self._testMethodName} - {str(e)}"
            self.failure_reason = error_message
            raise

        try:
            # Test with the production environment
            response = self.make_request('production', data=data)
            self.assertEqual(response.status_code, 200, "Production environment failed")
        except AssertionError as e:
            error_message = f"Test Failed: {self._testMethodName} - {str(e)}"
            self.failure_reason = error_message
            raise

    def test_unsuccessful_registration(self):
        """Test for unsuccessful registration."""

        # Ensure URLs are set
        assert self.TESTING_URL is not None, "TESTING_URL environment variable is not set."
        assert self.PRODUCTION_URL is not None, "PRODUCTION_URL environment variable is not set."

        # Define the data payload for the successful test
        data = {
            "email": "tschmidt@wavelynxtech",
            "first_name": "Sample",
            "last_name": "Simple",
            "company": "Sample Experiences"
        }

        try:
            # Test with the testing environment
            response = self.make_request('testing', data=data)
            self.assertNotEqual(response.status_code, 404, "Testing environment unexpected success")
        except AssertionError as e:
            error_message = f"Test Failed: {self._testMethodName} - {str(e)}"
            self.failure_reason = error_message
            raise

        try:
            # Test with the production environment
            response = self.make_request('production', data=data)
            self.assertNotEqual(response.status_code, 404, "Production environment unexpected success")
        except AssertionError as e:
            error_message = f"Test Failed: {self._testMethodName} - {str(e)}"
            self.failure_reason = error_message
            raise

if __name__ == "__main__":
    unittest.main()
