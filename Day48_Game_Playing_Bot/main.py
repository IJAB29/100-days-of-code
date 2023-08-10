from selenium import webdriver
from selenium.webdriver.common.by import By
import pprint
import time

chrome_driver = "C:\Dev\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver)
driver.get("https://orteil.dashnet.org/cookieclicker/")

# docs = driver.find_element(By.CSS_SELECTOR, value=".docs-meta a")
# print(docs.text)

# status = driver.find_element(by=By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[4]/a')
# print(status.get_attribute("a"))

# dates = driver.find_elements(by=By.CSS_SELECTOR,
#                              value="#content > div > section > div.list-widgets.row > "
#                                    "div.medium-widget.event-widget.last > div > ul > li > time")
# events = driver.find_elements(by=By.CSS_SELECTOR,
#                               value="#content > div > section > div.list-widgets.row > "
#                                     "div.medium-widget.event-widget.last > div > ul > li > a")
# dates_text = [date.text for date in dates]
# events_text = [event.text for event in events]
#
# upcoming_events = {index: {"date": dates_text[index], "name": events_text[index]}
#                    for index in range(0, len(events_text))}

# pprint.pprint(upcoming_events)
# fname_input = driver.find_element(By.NAME, "fName")
# fname_input.send_keys(first_name)
# lname_input = driver.find_element(By.NAME, "lName")
# lname_input.send_keys(last_name)
# email_input = driver.find_element(By.NAME, "email")
# email_input.send_keys(email)
# signup_btn = driver.find_element(By.CLASS_NAME, "btn-primary")
# signup_btn.click()

"""0-18 products"""


def buyProducts():
    products = driver.find_elements(By.CSS_SELECTOR, ".product.unlocked.enabled")[::-1]
    upgrades = driver.find_elements(By.CSS_SELECTOR, ".crate.upgrade.enabled")
    if len(upgrades) != 0:
        cheapest_upgrade = upgrades[0]
        cheapest_upgrade.click()
    elif len(products) != 0:
        most_expensive_product = products[0]
        most_expensive_product.click()
    products.clear()
    upgrades.clear()


time.sleep(5)
lang_eng = driver.find_element(By.ID, "langSelect-EN")
lang_eng.click()
time.sleep(5)
stop_time = time.time() + 60*5
shopping_time = time.time() + 5
cookie = driver.find_element(By.ID, "bigCookie")
while True:
    cookie.click()

    if time.time() > shopping_time:
        buyProducts()
        shopping_time = time.time() + 5

    if time.time() > stop_time:
        break

cookies_per_second = driver.find_element(By.XPATH, '//*[@id="cookiesPerSecond"]')
print(cookies_per_second.text)
driver.quit()
