from time import sleep
import sys
sys.path.append(r'C:\\Projects\\Get_Free_Followers')
from init import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

username = input('What is your Instagram username?\n')
print('Getting followers... Please do not terminate the program.')

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

        element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[2]/div[1]/div/div/div[1]/div'))
        WebDriverWait(self.browser, 1000).until(element_present)

        if("Başarıyla Gönderildi" in self.browser.page_source):
            print(f"\n10 followers followed you!")
            self.browser.save_screenshot('followed.png')
        elif("Çok Hızlı İşlem Yapıyorsunuz" in self.browser.page_source):
            print(f"\nError! Do not run the program fast mode!")
            self.browser.save_screenshot('error.png')
        else:
            print(f"\nError! Your credits have been expired! Please change your Instagram username.")
            self.browser.save_screenshot('error.png')

    def close_browser(self):
        Setup.close_browser(self)

ig = Instagram()
j = 0
while(True):
    ig.setup()
    i = 0
    try:
        while(True):
            try:
                ig.go_to_website()
                i = i + 1
            except:
                ig.close_browser()
        j = j + 1
    except:
        print('An error has been occurred. Retrying...')
