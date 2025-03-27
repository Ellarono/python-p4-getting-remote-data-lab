import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # Perform a GET request and return the raw response content
        response = requests.get(self.url)
        response.raise_for_status()  # Raise an HTTPError if the response contains an error status code
        return response.content  # Return raw response content (bytes)

    def load_json(self):
        # Load JSON data from the raw response content
        response_body = self.get_response_body()
        return json.loads(response_body)  # Convert bytes to a Python dictionary or list
