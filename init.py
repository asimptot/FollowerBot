from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import warnings
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from random import randint, sample, choice
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.window import WindowTypes
import undetected_chromedriver as uc
import sys

class Setup:
    def init(self):
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--mute-audio")
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-translate')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--no-sandbox')
        prefs = {"credentials_enable_service": False,
                 "profile.password_manager_enabled": False}
        chrome_options.add_experimental_option("prefs", prefs)
        self.browser = uc.Chrome(options=chrome_options, version_main=110)

    def close_browser(self):
        self.browser.quit()
