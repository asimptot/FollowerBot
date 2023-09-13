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
from seleniumbase import Driver

class Setup:
    def init(self):
        self.browser = Driver(headless=True)

    def close_browser(self):
        self.browser.delete_all_cookies()
        self.browser.quit()
