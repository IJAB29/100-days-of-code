import requests
import datetime as dt
import smtplib
import time

MY_LONG = 125.540627
MY_LAT = 8.947538

parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}

hour_now = dt.datetime.now().hour
# hour_now = 8

response_sun = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response_sun.raise_for_status()
sunrise = int(response_sun.json()["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(response_sun.json()["results"]["sunset"].split("T")[1].split(":")[0])

response_ISS = requests.get("http://api.open-notify.org/iss-now.json")
response_ISS.raise_for_status()
ISS_long = float(response_ISS.json()["iss_position"]["longitude"])
ISS_lat = float(response_ISS.json()["iss_position"]["latitude"])
# ISS_long = 8
# ISS_lat = 125

while True:
    time.sleep(60)
    if MY_LONG - 5 <= ISS_long <= MY_LONG + 5 and MY_LAT - 5 <= ISS_lat <= MY_LAT + 5 and\
            sunset >= hour_now or hour_now >= sunrise:
        with open("../Day32_Email_Sender/account.txt") as f:
            account = f.readlines()
            my_email = account[0]
            my_password = account[1]

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:Look Up\n\nISS is above you in the sky."
            )
