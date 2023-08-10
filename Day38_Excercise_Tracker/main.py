import requests
import datetime as dt
import os

APPLICATION_ID = "6080c1e7"
APPLICATION_KEY = "3afb9c72f82d12c2d1a30af9e36a9cfd"
SHEETY_TOKEN = "souiebasoukonomunenoana"
MY_GENDER = "male"
MY_AGE = 22
MY_HEIGHT = 160
MY_WEIGHT = 50

today = dt.datetime.now().strftime("%m/%d/%Y")
time_today = dt.datetime.now().strftime("%I:%M:%S %p")

sheety_endpoint = "https://api.sheety.co/ea40ce7228e314bfc5c48801938b3671/workoutTracking/workouts"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_headers = {
    "x-app-id": APPLICATION_ID,
    "x-app-key": APPLICATION_KEY,
}

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

parameters = {
    "query": input("What exercises did you do today? "),
    "gender": MY_GENDER,
    "weight_kg": MY_WEIGHT,
    "height_cm": MY_HEIGHT,
    "age": MY_AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=exercise_headers)
response_data = response.json()["exercises"]

for exercise in response_data:
    sheety_post_body = {
        "workout": {
            "date": today,
            "time": time_today,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheety_post = requests.post(url=sheety_endpoint, json=sheety_post_body, headers=sheety_headers)
