import requests

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "aZDX1wEvMuhWvWH9LvcWIRfwRcB4dJh7"
HEADER = {"apikey": TEQUILA_API_KEY}


class FlightSearch:

    #This class is responsible for talking to the Flight Search API.
    def getCodes(self, city):
        params = {"term": city, "location_types": "city"}
        response = requests.get(f"{TEQUILA_ENDPOINT}/locations/query", params=params, headers=HEADER)
        data = response.json()["locations"]
        return data[0]["code"]
