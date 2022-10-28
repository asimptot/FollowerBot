from time import sleep
import sys
sys.path.append(r'C:\\Projects\\Get_Free_Followers')
from init import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Instagram:
    def setup(self):
        Setup.init(self)

    def go_to_website(self):
        sleep(4)
        self.browser.get('https://likestool.com/site/login')
        sleep(10)

        uid = self.browser.find_element(By.NAME, 'LoginForm[username]')
        uid.send_keys('formaretro@gmail.com')
        sleep(2)
        pwd = self.browser.find_element(By.NAME, 'LoginForm[password]')
        pwd.send_keys('10061144')
        sleep(2)
        btn = self.browser.find_element(By.XPATH, '//*[@id="login_form"]/div[4]/input')
        btn.click()
        sleep(2)
        #You must add your social media account to YouLikeHits system.
        print('Getting credits... Please do not terminate the program.')
        self.browser.get('https://likestool.com/campaign/YOUTUBE_VIEWS')
        sleep(8)

        yt_view1 = self.browser.find_element(By.CSS_SELECTOR, '#campaign-container > div:nth-child(1) > div > div.form-inline.like-buttons > a')
        yt_view1.click()


        while (True):

            sleep(50)
            yt_view = self.browser.find_element(By.XPATH, '//*[@id="campaign-container"]/div[1]/div/div[3]/a')
            yt_view.click()

    def close_browser(self):
        Setup.close_browser(self)

ig = Instagram()
ig.setup()
ig.go_to_website()
ig.close_browser()