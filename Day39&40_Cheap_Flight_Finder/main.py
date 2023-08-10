import requests
from pprint import pprint
from data_manager import DataManager
from flight_data import FlightData
from notification_manager import NotificationManager


data_manager = DataManager()
sheet_data = data_manager.getSheetData()

for data in sheet_data:
    if data["iataCode"] == "":
        from flight_search import FlightSearch
        flight_search = FlightSearch()
        data["iataCode"] = flight_search.getCodes(data["city"])

        data_manager.data = sheet_data
        data_manager.updateSheetCodes()
pprint(sheet_data)

