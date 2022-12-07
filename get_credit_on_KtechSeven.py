from time import sleep
import sys
sys.path.append(r'C:\\Projects\\Get_Free_Followers')
from init import *

class KtechSeven:
    def setup(self):
        Setup.init(self)
        sleep(4)
        self.browser.get('https://ktechseven.com/')
        sleep(5)
        uid = self.browser.find_element(By.NAME, 'login')
        uid.send_keys(YOUR KTECHSEVEN USERNAME)
        pwd = self.browser.find_element(By.NAME, 'pass')
        pwd.send_keys(YOUR KTECHSEVEN PASSWORD)
        sleep(2)
        btn = self.browser.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div[1]/form/div[1]/input')
        btn.click()
        sleep(2)

    def get_point(self):
        point = self.browser.find_element(By.ID, 'c_coins')
        print('Your point is: ' + point.text)
        return point

    def go_to_website(self):
        print('Getting credits... Please do not terminate the program.')
        for i in range(2):
            self.browser.get('https://ktechseven.com/p.php?p=youtube')
            sleep(4)
            yt_view = self.browser.find_element(By.CLASS_NAME, 'followbutton')
            yt_view.click()
            sleep(2)
        N = 26
        play = ActionChains(self.browser)
        for _ in range(N):
            play.send_keys(Keys.TAB).perform()
        sleep(2)
        play.send_keys(Keys.RETURN).perform()
        sleep(70)

    def close_browser(self):
        Setup.close_browser(self)

ks = KtechSeven()
ks.setup()
while(True):
    try:
        ks.go_to_website()
        ks.get_point()
    except:
        print('Content not found to watch or surf. Refreshing webpage...')
        sleep(60)
