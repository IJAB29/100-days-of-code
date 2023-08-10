import requests
import smtplib

my_api = "67260fbf0c4d7c3c2c35511bbf978f02"
my_lat = 8.947538
my_long = 125.540627

parameters = {"lat": my_lat, "lon": my_long, "appid": my_api, "exclude": "current,minutely,daily"}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
hourly_data = response.json()["hourly"]

possible_rain = False

for hour in hourly_data[:12]:
    hourly_weather = hour["weather"][0]["id"]
    if hourly_weather < 700:
        possible_rain = True

if possible_rain:
    with open("../Day32_Email_Sender/account.txt") as f:
        account = f.readlines()
        email = account[0]
        password = account[1]

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f"Subject:Rain Notification App\n\nIt's going to rain today, remember to bring an umbrella."
        )
