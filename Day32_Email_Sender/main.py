import smtplib
import datetime as dt
from random import choice
from os import listdir
import pandas as pd

now = dt.datetime.now()
match = False

data = pd.read_csv("birthdays.csv").to_dict(orient="index")

for key, val in data.items():
    if val["month"] == now.month and val["day"] == now.day:
        celebrant_name = val["name"]
        celebrant_email = val["email"]
        match = True

with open(f'letter_templates/{choice(listdir("letter_templates/"))}') as f:
    letter_template = f.read()

if match:
    with open("account.txt") as f:
        account_details = f.readlines()
        my_email = account_details[0]
        my_password = account_details[1]

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(
            user=my_email,
            password=my_password
        )
        connection.sendmail(
            from_addr=my_email,
            to_addrs=celebrant_email,
            msg=f"Subject:Happy Birthday!\n\n{letter_template.replace('[NAME]', celebrant_name)}"
        )
