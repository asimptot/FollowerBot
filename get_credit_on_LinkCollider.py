from time import sleep
import sys
sys.path.append(r'C:\\Projects\\Get_Free_Followers')
from init import *

class LinkCollider:
    def setup(self):
        Setup.init(self)

    def go_to_website(self):
        sleep(4)
        self.browser.get('https://www.linkcollider.com/page/login')
        sleep(10)

        uid = self.browser.find_element(By.NAME, 'email')
        uid.send_keys('YOUR LINKCOLLIDER USERNAME')
        sleep(2)
        pwd = self.browser.find_element(By.NAME, 'pw')
        pwd.send_keys('YOUR LINKCOLLIDER PASSWORD')
        sleep(2)
        btn = self.browser.find_element(By.XPATH, '//*[@id="login"]/div[3]/div[3]/div[2]/button')
        btn.click()
        sleep(2)

        print('Getting credits... Please do not terminate the program.')

        for i in range(20):
            self.browser.get('https://www.linkcollider.com/page/activity/autosurf')
            sleep(35)

    def close_browser(self):
        Setup.close_browser(self)

lc = LinkCollider()
lc.setup()
lc.go_to_website()
lc.close_browser()
