import requests
from bs4 import BeautifulSoup
import smtplib
import lxml
import time

URL = "https://www.amazon.com/ViewSonic-VX3276-MHD-Frameless-Widescreen-DisplayPort/dp/B0787WGCXT/ref=sr_1_6?crid=21GXK10LUXW3L&keywords=monitor&nav_sdd=aps&qid=1659864045&refinements=p_n_size_browse-bin%3A3547808011%2Cp_n_feature_two_browse-bin%3A23595225011%2Cp_72%3A1248879011&rnid=1248877011&s=pc&sprefix=monitor&sr=1-6&th=1"
MY_EMAIL = "johntarou69420@gmail.com"
MY_PASSWORD = "jtarou69420"

response = requests.get(URL, headers= {"User-Agent":"Defined"}).text
soup = BeautifulSoup(response, "lxml")

stop = False
while not stop:
    try:
        product_name = soup.find(name="span", id="productTitle").getText()
        print(product_name)
        price_whole = soup.select_one(selector="span .a-price-whole")
        price_fraction = soup.select_one(selector="span .a-price-fraction")
        full_price = float(f"{price_whole.get_text()}{price_fraction.get_text()}")
        print(full_price)
    except AttributeError:
        print("Error")
        time.sleep(5)
    else:
        stop = True

if full_price < 200:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Aazon Price Tracker\n\nThe price of {product_name} is currently {full_price}."
        )
    print("Mail Sent!")
