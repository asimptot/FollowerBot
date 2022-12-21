from time import sleep
import sys
sys.path.append(r'C:\\Projects\\Get_Free_Followers')
from init import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

post_link = input('What is your post link?\n')

class Instagram:
    def setup(self):
        Setup.init(self)

    def go_to_website(self):
        sleep(4)
        self.browser.get('https://tolinay.com/instagram-begeni-hilesi')
        sleep(4)

        uid = self.browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/form/div/div[1]/input')
        uid.send_keys(post_link)
        sleep(2)

        button = self.browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[2]/form/div/div[3]/button')
        button.click()

        element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div'))
        WebDriverWait(self.browser, 1000).until(element_present)

        if("Başarıyla Gönderildi" in self.browser.page_source):
            print(f"\nYou got 10 likes!")
            self.browser.save_screenshot('liked.png')
        elif("Çok Hızlı İşlem Yapıyorsunuz" in self.browser.page_source):
            print(f"\nError! Do not run the program fast mode!")
            self.browser.save_screenshot('error.png')
        else:
            print(f"\nError! Your credits have been expired! Please change your Instagram username.")
            self.browser.save_screenshot('error.png')

    def close_browser(self):
        Setup.close_browser(self)

ig = Instagram()
while(True):
    ig.setup()
    ig.go_to_website()
    ig.close_browser()
