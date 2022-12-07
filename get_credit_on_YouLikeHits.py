from time import sleep
import sys
sys.path.append(r'C:\\Projects\\Get_Free_Followers')
from init import *

class YouLikeHits:
    def setup(self):
        Setup.init(self)

    def get_point(self):
        point = self.browser.find_element(By.ID, 'currentpoints')
        print('Your point is: ' + point.text)
        return point

    def go_to_website(self):
        sleep(4)
        self.browser.get('https://www.youlikehits.com/login.php')
        sleep(5)
        uid = self.browser.find_element(By.ID, 'username')
        uid.send_keys(YOUR YOULIKEHITS USERNAME)
        pwd = self.browser.find_element(By.ID, 'password')
        pwd.send_keys(YOUR YOULIKEHITS PASSWORD)
        sleep(2)
        btn = self.browser.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/center/form/table/tbody/tr[3]/td/span/input')
        btn.click()
        sleep(2)

        print('Getting credits... Please do not terminate the program.')
        while(True):
            try:
                self.browser.get('https://www.youlikehits.com/youtubenew2.php')
                sleep(4)
                yt_view = self.browser.find_element(By.XPATH, '//*[@id="listall"]/center/a[1]')
                yt_view.click()

                element_present = EC.presence_of_element_located(
                    (By.XPATH, "//*[contains(text(), 'Points Added')]"))
                WebDriverWait(self.browser, 1000).until(element_present)

            except:
                while(True):
                    self.browser.get('https://www.youlikehits.com/websites.php')
                    sleep(4)
                    surf = WebDriverWait(self.browser, 10).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "Visit"))
                    )
                    surf.click()
                    sleep(25)
                    child = self.browser.window_handles[1]
                    self.browser.switch_to.window(child)
                    self.browser.close()
                    parent = self.browser.window_handles[0]
                    self.browser.switch_to.window(parent)
                    sleep(2)

    def close_browser(self):
        Setup.close_browser(self)

ylh = YouLikeHits()
while(True):
    try:
        ylh.setup()
        ylh.go_to_website()
    except:
        ylh.get_point()
        print('Content not found to watch or surf. Refreshing webpage...')
        ylh.close_browser()
