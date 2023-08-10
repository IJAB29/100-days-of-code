import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os
from selenium.webdriver.common.by import By

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3205140090&f_AL=true&geoId=103121230&keywords=python%20developer&location=Philippines&refresh=true"
DRIVER = "C:\Dev\chromedriver.exe"

driver = webdriver.Chrome(DRIVER)
driver.get(URL)

delay = 2
phone_num = 123456789
jobs_class = "disabled ember-view job-card-container__link job-card-list__title"
next_btn_class = "artdeco-button artdeco-button--2 artdeco-button--primary ember-view"
apply_btn_class = "jobs-apply-button artdeco-button artdeco-button--3 artdeco-button--primary ember-view"
close_btn_class = "artdeco-modal__dismiss artdeco-button artdeco-button--circle artdeco-button--muted artdeco-button--2 artdeco-button--tertiary ember-view"
save_btn_class = "artdeco-modal__confirm-dialog-btn artdeco-button artdeco-button--2 artdeco-button--primary ember-view"
number_input_class = "ember-text-field ember-view fb-single-line-text__input"


time.sleep(delay)
sign_in = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
sign_in.click()

time.sleep(delay)
email = driver.find_element(By.ID, "username")
email.send_keys(os.environ.get("EMAIL"), Keys.TAB, os.environ.get("PASSWORD"), Keys.ENTER)
# password = driver.find_element((By.ID, "password"))
# password.send_keys(os.environ.get("PASSWORD"))
# password.send_keys(Keys.ENTER)

time.sleep(delay)
all_jobs = driver.find_elements(By.CLASS_NAME, jobs_class.replace(" ", "."))
print(all_jobs)
for job in all_jobs:
    job.click()
    time.sleep(delay)
    save = driver.find_element(By.CLASS_NAME, "jobs-save-button artdeco-button artdeco-button--3 artdeco-button--secondary".replace(" ", "."))
    save.click()
    # apply_btn = driver.find_element(By.CLASS_NAME, apply_btn_class.replace(" ", "."))
    # apply_btn.click()
    # number = driver.find_element(By.CLASS_NAME, number_input_class.replace(" ", "."))
    # number.send_keys(phone_num)
    # next_btn = driver.find_element(By.CLASS_NAME, next_btn_class.replace(" ", "."))
    # next_btn.click()
    # exit_btn = driver.find_element(By.CLASS_NAME, close_btn_class.replace(" ", "."))
    # exit_btn.click()
    # save_btn = driver.find_element(By.CLASS_NAME, save_btn_class.replace(" ", "."))
    # save_btn.click()
    # time.sleep(delay)
