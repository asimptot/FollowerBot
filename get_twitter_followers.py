from time import sleep
import sys
sys.path.append(r'C:\\Projects\\Get_Free_Followers')
from init import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

username = input('What is your twitter username?\n')

class Twitter:
    def setup(self):
        Setup.init(self)
        print('Followers are sending... Please do not terminate the program.')

    def increase_credit(self):
        # You must add your Twitter account to YouLikeHits system.
        while (True):
            self.browser.get('https://www.youlikehits.com/youtubenew2.php')
            sleep(4)

            yt_view = self.browser.find_element(By.XPATH, '//*[@id="listall"]/center/a[1]')
            yt_view.click()
            sleep(130)

    def close_browser(self):
        Setup.close_browser(self)

twt = Twitter()
twt.setup()
twt.increase_credit()
twt.close_browser()
