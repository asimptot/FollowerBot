from time import sleep
import sys
sys.path.append(r'C:\\Projects\\Get_Free_Followers')
from init import *

class KingdomLikes:
    def setup(self):
        Setup.init(self)

    def go_to_website(self):
        sleep(4)
        self.browser.get('https://kingdomlikes.com/')
        sleep(5)

        uid = self.browser.find_element(By.NAME, 'email')
        uid.send_keys(YOUR KINGDOMLIKES EMAIL ADDRESS)
        sleep(2)
        pwd = self.browser.find_element(By.NAME, 'password')
        pwd.send_keys(YOUR KINGDOMLIKES PASSWORD)
        sleep(2)
        btn = self.browser.find_element(By.ID, 'buttonmobile')
        btn.click()
        sleep(2)
        #You must add your social media account to KingdomLikes system.
        print('Getting credits... Please do not terminate the program.')
        while (True):
            self.browser.get('https://kingdomlikes.com/free_points/youtube-views')
            try:
                sleep(4)
                yt_view = self.browser.find_element(By.XPATH, '//*[@id="idpage5"]/div/div[5]/button')
                yt_view.click()
                element_present = EC.presence_of_element_located(
                    (By.XPATH, '//*[@id="idpage6"]/div/div[5]/button'))
                WebDriverWait(self.browser, 350).until(element_present)
            except:
                while(True):
                    self.browser.get('https://kingdomlikes.com/free_points/web-traffic')
                    sleep(4)
                    surf = self.browser.find_element(By.XPATH, '//*[@id="idpage5"]/div/div[5]/button')
                    surf.click()
                    element_present = EC.presence_of_element_located(
                        (By.XPATH, '//*[@id="idpage6"]/div/div[5]/button'))
                    WebDriverWait(self.browser, 350).until(element_present)

    def close_browser(self):
        Setup.close_browser(self)

kl = KingdomLikes()
while(True):
    kl.setup()
    try:
        kl.go_to_website()
    except:
        kl.close_browser()
