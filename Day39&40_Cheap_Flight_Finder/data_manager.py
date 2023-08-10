import requests
import gspread

SHEETY_ENDPOINT = "https://api.sheety.co/ea40ce7228e314bfc5c48801938b3671/flightDeals/prices"


class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.data = {}

    def getSheetData(self):
        response = requests.get(SHEETY_ENDPOINT)
        response.raise_for_status()
        self.data = response.json()["price"]
        print(self.data)

    def updateSheetCodes(self):
        for d in self.data:
            new_data = {
                "prices": {
                    "iataCode": d["iataCode"]
                }
            }
            response = requests.put(f"{SHEETY_ENDPOINT}/{d['id']}", json=new_data)
            response.raise_for_status()
            print(response.text)

data = DataManager()
data.getSheetData()
