from math import floor
import requests
import smtplib

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

MY_EMAIL = "johntarou69420@gmail.com"
MY_PASSWORD = "jtarou69420"
MY_ADVANTAGE_API = "6IDJG2C5RGU9EFFE"
MY_NEWS_API = "1c61545707c44279bf06d400bf89f9c0"


def percentageDiff(a: float, b: float) -> float:
    diff = a - b
    ave = (a + b) / 2
    return diff / ave


advantage_params = {"function": "TIME_SERIES_DAILY", "symbol": STOCK_NAME, "apikey": MY_ADVANTAGE_API}
advantage_response = requests.get(STOCK_ENDPOINT, params=advantage_params)
advantage_response.raise_for_status()
advantage_data = [(key, value) for (key, value) in advantage_response.json()["Time Series (Daily)"].items()]
yesterday_closing = float(advantage_data[0][1]["4. close"])
two_days_before_closing = float(advantage_data[1][1]["4. close"])
percentage_difference = percentageDiff(yesterday_closing, two_days_before_closing)

if percentage_difference >= 0.05 or percentage_difference < -0.05:
    percentage = floor(percentage_difference*100)
    if percentage > 0:
        title = f"{STOCK_NAME}: 🔺{percentage}%"
    else:
        title = f"{STOCK_NAME}: 🔻{percentage}%"

    news_params = {"apiKey": MY_NEWS_API, "qInTitle": COMPANY_NAME}
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    news_data = news_response.json()["articles"][:3]
    news_articles = [{"title": article["title"], "description": article["description"]} for article in news_data]

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        for article in news_articles:
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:{title}\n\nHeadline: {article['title']}\nBrief: {article['description'].encode('utf-8')}"
            )
