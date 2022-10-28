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
        self.browser.get('https://www.linkcollider.com/page/login')
        sleep(10)

        uid = self.browser.find_element(By.NAME, 'email')
        uid.send_keys('formaretro@gmail.com')
        sleep(2)
        pwd = self.browser.find_element(By.NAME, 'pw')
        pwd.send_keys('10061144')
        sleep(2)
        btn = self.browser.find_element(By.XPATH, '//*[@id="login"]/div[3]/div[3]/div[2]/button')
        btn.click()
        sleep(2)
        #You must add your social media account to YouLikeHits system.
        print('Getting credits... Please do not terminate the program.')
        self.browser.get('https://www.linkcollider.com/page/activity/autosurf')

    def close_browser(self):
        Setup.close_browser(self)

ig = Instagram()
ig.setup()
ig.go_to_website()
#ig.close_browser()