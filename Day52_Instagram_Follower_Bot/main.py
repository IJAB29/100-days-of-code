import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

DRIVER_PATH = "C:\Dev\chromedriver.exe"
INSTAGRAM = "https://www.instagram.com/?hl=en"

driver = selenium.webdriver.Chrome(DRIVER_PATH)
driver.get(INSTAGRAM)
