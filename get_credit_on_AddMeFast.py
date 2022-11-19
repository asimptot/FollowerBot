from time import sleep
import sys
sys.path.append(r'C:\\Projects\\Get_Free_Followers')
from init import *

class AddMeFast:
    def setup(self):
        Setup.init(self)

    def go_to_website(self):
        sleep(4)
        self.browser.get('https://addmefast.com')
        sleep(4)

        username = self.browser.find_element(By.XPATH, '//*[@id="wrapper"]/section[2]/div/div[4]/form/div[1]/div[1]/input[1]')
        username.send_keys(YOUR ADDMEFAST E-MAIL ADDRESS)

        password = self.browser.find_element(By.XPATH, '//*[@id="wrapper"]/section[2]/div/div[4]/form/div[1]/div[1]/input[2]')
        password.send_keys(YOUR ADDMEFAST PASSWORD)

        button = self.browser.find_element(By.NAME, 'login_button')
        button.click()

        sleep(6)

        while(True):
            self.browser.get('https://addmefast.com/websites')
            if "No item" not in self.browser.page_source:
                sleep(25)

            elif "No item" in self.browser.page_source:
                while(True):
                    self.browser.get('https://addmefast.com/free_points/youtube_views')
                    view_video = WebDriverWait(self.browser, 5).until(
                        EC.presence_of_element_located((By.LINK_TEXT, "View Video"))
                    )
                    view_video.click()
                    sleep(35)

                    child = self.browser.window_handles[1]
                    self.browser.switch_to.window(child)
                    self.browser.close()
                    parent = self.browser.window_handles[0]
                    self.browser.switch_to.window(parent)
                    sleep(5)

    def close_browser(self):
        Setup.close_browser(self)

amf = AddMeFast()

while(True):
    amf.setup()
    try:
        amf.go_to_website()
    except:
        amf.close_browser()