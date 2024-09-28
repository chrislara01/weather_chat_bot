import unittest
from utils.api_utils import api_calling
import requests

class TestApiUtils(unittest.TestCase):
    def test_get_flowise_data(self):
        # Mock the API response
        mock_response = {"response": "Mocked response"}
        
        # Replace the actual API call with the mocked response
        original_get = requests.get
        requests.get = lambda url, params=None: unittest.mock.Mock(return_value=mock_response)
        
        result = api_calling()
        
        self.assertEqual(result, mock_response)
        
        # Restore the original get method
        requests.get = original_get

if __name__ == '__main__':
    unittest.main()