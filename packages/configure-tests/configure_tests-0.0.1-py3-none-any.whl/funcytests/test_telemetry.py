import unittest
import requests
import os
from dotenv import load_dotenv
from utils.t_manager import retrieve_token

class TestTelemetry(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        # Load environment variables from .env file
        load_dotenv()
        # Strictly fetch URLs from environment variables
        self.TESTING_URL = os.getenv('TESTING_URL')
        self.PRODUCTION_URL = os.getenv('PRODUCTION_URL')

        # Set docstrings for test functions
        self.test_valid_event_format.__func__.__doc__ = "Test for successful telemetry event posting."
        self.test_invalid_event_format.__func__.__doc__ = "Test for unsuccessful telemetry event posting."

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
            url = self.TESTING_URL + '/app/upload'
            token = retrieve_token('testing')
        else: 
            url = self.PRODUCTION_URL + '/app/upload'
            token = retrieve_token('production')

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'{token}'
        }

        # Make the request
        response = requests.post(url, json=data, headers=headers)

        return response

    def test_valid_event_format(self):
        """Test for successful telemetry event posting."""

        # Ensure URLs are set
        assert self.TESTING_URL is not None, "TESTING_URL environment variable is not set."
        assert self.PRODUCTION_URL is not None, "PRODUCTION_URL environment variable is not set."

        # Define the data payload for the successful test
        data = {
            "events": [
                {
                    "event_class": "READER",
                    "event_type": "DETAILS",
                    "data": {
                        "packet": "0102030405060708090A0B0C0D",
                        "coord_x": "123994.4040",
                        "coord_y": "499584.4499",
                        "rssi": "-50"
                    },
                    "client_id": "1234"
                },
                {
                    "event_class": "READER",
                    "event_type": "DETAILS",
                    "data": {
                        "config": "0102030405060708090A0B0C0D",
                        "coord_x": "123994.4040",
                        "coord_y": "499584.4499"
                    },
                    "client_id": "5678"
                },
                {
                    "event_class": "READER",
                    "event_type": "DETAILS",
                    "data": {
                        "download_token": "1234567890",
                        "result": "success"
                    },
                    "client_id": "6677"
                },
                {
                    "event_class": "READER",
                    "event_type": "DETAILS",
                    "data": {
                        "config": "CSN_MSB",
                        "coord_x": "123994.4040",
                        "coord_y": "499584.4499",
                        "result": "success"
                    },
                    "client_id": "4433"
                },
                {
                    "event_class": "BUNDLE",
                    "event_type": "DELETE",
                    "data": {
                        "download_token": "1234567890",
                        "result": "success"
                    },
                    "client_id": "90909"
                }
            ]
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

    def test_invalid_event_format(self):
        """Test for unsuccessful telemetry event posting."""

        # Ensure URLs are set
        assert self.TESTING_URL is not None, "TESTING_URL environment variable is not set."
        assert self.PRODUCTION_URL is not None, "PRODUCTION_URL environment variable is not set."

        # Define the data payload for the successful test
        data = {
            "events": [
                {
                    "event_class": "READER",
                    "event_type": "AAAA",
                    "data": {
                        "packet": "0102030405060708090A0B0C0D",
                        "coord_x": "123994.4040",
                        "coord_y": "499584.4499",
                        "rssi": "-50"
                    },
                    "client_id": "1234"
                },
                {
                    "event_class": "READER",
                    "event_type": "AAAA",
                    "data": {
                        "config": "0102030405060708090A0B0C0D",
                        "coord_x": "123994.4040",
                        "coord_y": "499584.4499"
                    },
                    "client_id": "5678"
                },
                {
                    "event_class": "READER",
                    "event_type": "AAAA",
                    "data": {
                        "download_token": "1234567890",
                        "result": "success"
                    },
                    "client_id": "6677"
                },
                {
                    "event_class": "READER",
                    "event_type": "AAAA",
                    "data": {
                        "config": "CSN_MSB",
                        "coord_x": "123994.4040",
                        "coord_y": "499584.4499",
                        "result": "success"
                    },
                    "client_id": "4433"
                },
                {
                    "event_class": "READER",
                    "event_type": "AAAA",
                    "data": {
                        "download_token": "1234567890",
                        "result": "success"
                    },
                    "client_id": "90909"
                }
            ]
        }

        try:
            # Test with the testing environment
            response = self.make_request('testing', data=data)
            self.assertNotEqual(response.status_code, 400, "Testing environment unexpected success")
        except AssertionError as e:
            error_message = f"Test Failed: {self._testMethodName} - {str(e)}"
            self.failure_reason = error_message
            raise

        try:
            # Test with the production environment
            response = self.make_request('production', data=data)
            self.assertNotEqual(response.status_code, 400, "Production environment unexpected success")
        except AssertionError as e:
            error_message = f"Test Failed: {self._testMethodName} - {str(e)}"
            self.failure_reason = error_message
            raise

if __name__ == "__main__":
    unittest.main()