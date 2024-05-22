from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

SIMILAR_ACCOUNT = "https://www.instagram.com/X/followers"
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PW"]


class InstaFollower:

    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        chrome_options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        url = "https://www.instagram.com/accounts/login/"
        self.driver.get(url)
        time.sleep(6)

        decline_cookie = self.driver.find_element(By.XPATH, value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/'
                                                                  'div[2]/div/button[2]')
        if decline_cookie:
            decline_cookie.click()

        time.sleep(5)
        user_name = self.driver.find_element(by=By.NAME, value="username")
        pw = self.driver.find_element(by=By.NAME, value="password")

        user_name.send_keys(USERNAME)
        pw.send_keys(PASSWORD)
        time.sleep(2)
        pw.send_keys(Keys.ENTER)

        time.sleep(10)
        notifications = self.driver.find_element(by=By.XPATH, value='/html/body/div[3]/div[1]/div/div[2]/div/div/div/'
                                                                    'div/div[2]/div/div/div[3]/button[2]')
        notifications.click()
        time.sleep(3)

    def find_follower(self):
        self.driver.get(SIMILAR_ACCOUNT)
        time.sleep(7)
        follower_popup = self.driver.find_element(by=By.XPATH, value='/html/body/div[6]/div[1]/div/div[2]/div/div/div/'
                                                                     'div/div[2]/div/div/div[3]')

        for i in range(5):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', follower_popup)
            time.sleep(2)

        self.driver.execute_script("arguments[0].scrollTop = 0", follower_popup)

    def follow(self, number_of_clicks=5):
        follow_buttons = self.driver.find_elements(by=By.XPATH, value="//button[contains(@class, '_acan') and contains"
                                                                      "(@class, '_acap') and contains(@class, '_acas') "
                                                                      "and contains(@class, '_aj1-') and contains"
                                                                      "(@class, '_ap30')]")
        for button in follow_buttons[:number_of_clicks]:
            try:
                button.click()
                time.sleep(2)
            except Exception as e:
                print("Error", e)


instagram_bot = InstaFollower()
instagram_bot.login()
instagram_bot.find_follower()
instagram_bot.follow()
