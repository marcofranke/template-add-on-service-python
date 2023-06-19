import requests

class PublicAPIServiceController:
    def __init__(self):
        self.base_url = "https://www.trick.ikap.biba.uni-bremen.de/public-api-service/"

    def invoke(self, function, input):
        url = self.base_url + "/invoke/" + function
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, input, headers=headers)
        return response.json()

    def config(self):
        url = self.base_url + "/config"
        response = requests.get(url)
        return response.text