import requests
import json

url = "https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json"
class GetRequester:

    def __init__(self, url):
        self.url = url
        self.response = requests.get(url)
    def get_response_body(self):
        return self.response.text

    def load_json(self):
        return json.loads(self.response.text)