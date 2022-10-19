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
        self.browser.get('https://www.youlikehits.com/login.php')
        sleep(10)
        uid = self.browser.find_element(By.ID, 'username')
        uid.send_keys(YOUR YOULIKEHITS USERNAME)  
        sleep(2)
        pwd = self.browser.find_element(By.ID, 'password')
        pwd.send_keys(YOUR YOULIKEHITS PASSWORD)
        sleep(2)
        btn = self.browser.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/center/form/table/tbody/tr[3]/td/span/input')
        btn.click()
        sleep(2)
        #You must add your social media account to YouLikeHits system.
        print('Getting credits... Please do not terminate the program.')
        while (True):
            self.browser.get('https://www.youlikehits.com/youtubenew2.php')
            sleep(4)
            yt_view = self.browser.find_element(By.XPATH, '//*[@id="listall"]/center/a[1]')
            yt_view.click()
            sleep(130)

    def close_browser(self):
        Setup.close_browser(self)

ig = Instagram()
ig.setup()
ig.go_to_website()
ig.close_browser()
