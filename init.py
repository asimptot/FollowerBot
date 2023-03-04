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
import undetected_chromedriver as uc

class Setup:
    def init(self):
        chrome_options = uc.ChromeOptions()
        chrome_options.add_argument('--headless=new')
        self.browser = uc.Chrome(options=chrome_options, version_main=110)

    def close_browser(self):
        self.browser.close()
        
