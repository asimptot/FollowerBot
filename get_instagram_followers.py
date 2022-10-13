from time import sleep
import sys
sys.path.append(r'C:\\Projects\\Get_Free_Followers')
from init import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

username = input('What is your username?\n')

class Instagram:

    def setup(self):
        Setup.init(self)

    def go_to_website(self):
        sleep(4)
        self.browser.get('https://tolinay.com/instagram-takipci-hilesi')
        sleep(4)

        uid = self.browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/form/div/div[1]/input')
        uid.send_keys(username)
        sleep(2)

        button = self.browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/form/div/div[3]/button')
        button.click()

        print('Please wait for 1000 seconds...')
        sleep(1000)

        if("Başarıyla Gönderildi" in self.browser.page_source):
            print(f"\n10 followers followed you!")
            self.browser.save_screenshot('followed.png')
        else:
            print(f"\nAn error occured!")
            self.browser.save_screenshot('error.png')

    def close_browser(self):
        Setup.close_browser(self)

ig = Instagram()
ig.setup()

while(True):
    ig.go_to_website()
ig.close_browser()
