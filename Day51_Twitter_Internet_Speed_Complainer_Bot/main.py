from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os


class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 0
        self.up = 0
        self.isp = ""
        self.driver = webdriver.Chrome(CHROMEDRIVER)

    def getInternetSpeed(self):
        self.driver.get(SPEEDTEST)
        start_btn = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        start_btn.click()
        time.sleep(45)
        self.down = self.driver.find_element(By.XPATH,
                                             '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        self.up = self.driver.find_element(By.XPATH,
                                           '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        self.isp = self.driver.find_element(By.XPATH,
                                            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[4]/div/div/div[1]/div[3]/div[2]').text

    def tweetAtProvider(self):
        self.driver.get(TWITTER)
        time.sleep(3)
        tweet = f"Hey {self.isp}, why is my internet speed {self.down}down/{self.up}up " \
                f"when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        sign_in = self.driver.find_element(By.XPATH,
                                           '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a')
        sign_in.click()
        time.sleep(5)
        email = self.driver.find_element(By.XPATH,
                                         '//input[@autocomplete="username"]')
        email.send_keys(os.environ.get("GMAIL"), Keys.ENTER)
        time.sleep(5)
        password = self.driver.find_element(By.XPATH,
                                            '//input[@autocomplete="current-password"]')
        password.send_keys(os.environ.get("PASSWORD"), Keys.ENTER)
        tweet_btn = self.driver.find_element(By.XPATH,
                                                 '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        tweet_btn.click()
        compose_tweet = self.driver.find_element(By.XPATH,
                                                 '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')
        compose_tweet.send_keys(tweet)



CHROMEDRIVER = "C:\Dev\chromedriver.exe"
TWITTER = "https://twitter.com"
SPEEDTEST = "https://www.speedtest.net"

PROMISED_DOWN = 150
PROMISED_UP = 10

bot = InternetSpeedTwitterBot()

bot.getInternetSpeed()
bot.tweetAtProvider()
