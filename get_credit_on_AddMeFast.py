from time import sleep
import sys
sys.path.append(r'C:\\Projects\\Get_Free_Followers')
from init import *
from random import randint

class AddMeFast:
    def setup(self):
        Setup.init(self)

    def go_to_website(self):
        sleep(4)
        self.browser.get('https://addmefast.com')
        sleep(4)

        username = self.browser.find_element(By.XPATH, '//*[@id="wrapper"]/section[2]/div/div[4]/form/div[1]/div[1]/input[1]')
        username.send_keys(YOUR ADDMEFAST USERNAME)

        password = self.browser.find_element(By.XPATH, '//*[@id="wrapper"]/section[2]/div/div[4]/form/div[1]/div[1]/input[2]')
        password.send_keys(YOUR ADDMEFAST PASSWORD)

        button = self.browser.find_element(By.NAME, 'login_button')
        button.click()
        sleep(6)

        self.browser.get('https://addmefast.com/websites')
        while("No item" not in self.browser.page_source):
            sleep(25)
        delay = randint(1, 300)
        sleep(delay)

    def close_browser(self):
        Setup.close_browser(self)

amf = AddMeFast()

while(True):
    amf.setup()
    try:
        amf.go_to_website()
    except:
        amf.close_browser()
