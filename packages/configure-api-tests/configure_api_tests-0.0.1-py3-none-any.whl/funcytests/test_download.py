import unittest
import requests
import os
from dotenv import load_dotenv
from utils.t_manager import retrieve_token

class TestDownloadProfile(unittest.TestCase):

    def setUp(self):
        """Set up the test environment."""
        # Load environment variables from .env file
        load_dotenv()
        
        # Strictly fetch URLs from environment variables
        self.TESTING_URL = os.getenv('TESTING_URL')
        self.PRODUCTION_URL = os.getenv('PRODUCTION_URL')

        # Set docstrings for test functions
        self.test_successful_download.__func__.__doc__ = "Test for successful profile download."
        self.test_unsuccessful_download.__func__.__doc__ = "Test for unsuccessful profile download."

    def make_request(self, environment, download_token):
        """
        Helper method to make a request based on the environment.

        Parameters:
        - environment (str): The environment ('testing' or 'production').
        - download_token (str): The download token for the request.

        Returns:
        - response: The response object from the request.
        """
        if environment == 'testing':
            url = self.TESTING_URL + '/app/download'
            token = retrieve_token('testing')
        else:  # 'production'
            url = self.PRODUCTION_URL + '/app/download'
            token = retrieve_token('production')

        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'{token}'
        }
        data = {
            "download_token": download_token,
            "job_token": "1"
        }

        response = requests.post(url, json=data, headers=headers)

        return response

    def test_successful_download(self):
        """Test for successful profile download."""
        testing_token = "s7cD6oVo"
        production_token = "5fXJLHmd"

        # Ensure URLs are set
        assert self.TESTING_URL is not None, "TESTING_URL environment variable is not set."
        assert self.PRODUCTION_URL is not None, "PRODUCTION_URL environment variable is not set."

        try:
            # Test with the testing environment
            response = self.make_request('testing', testing_token)
            self.assertEqual(response.status_code, 200, "Testing environment failed")
        except AssertionError as e:
            error_message = f"Test Failed: {self._testMethodName} - {str(e)}"
            self.failure_reason = error_message
            raise

        try:
            # Test with the production environment
            response = self.make_request('production', production_token)
            self.assertEqual(response.status_code, 200, "Production environment failed")
        except AssertionError as e:
            error_message = f"Test Failed: {self._testMethodName} - {str(e)}"
            self.failure_reason = error_message
            raise

    def test_unsuccessful_download(self):
        """Test for un-successful successful profile download."""
        testing_invalid_token = "aaaaaa"
        production_invalid_token = "bbbbbb"

        # Ensure URLs are set
        assert self.TESTING_URL is not None, "TESTING_URL environment variable is not set."
        assert self.PRODUCTION_URL is not None, "PRODUCTION_URL environment variable is not set."

        try:
            # Test with the testing environment
            response = self.make_request('testing', testing_invalid_token)
            self.assertNotEqual(response.status_code, 200, "Testing environment unexpected success")
        except AssertionError as e:
            error_message = f"Test Failed: {self._testMethodName} - {str(e)}"
            self.failure_reason = error_message
            raise

        try:
            # Test with the production environment
            response = self.make_request('production', production_invalid_token)
            self.assertNotEqual(response.status_code, 200, "Production environment unexpected success")
        except AssertionError as e:
            error_message = f"Test Failed: {self._testMethodName} - {str(e)}"
            self.failure_reason = error_message
            raise

if __name__ == "__main__":
    unittest.main()
