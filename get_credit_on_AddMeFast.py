from time import sleep
import sys
sys.path.append(r'C:\\Projects\\Get_Free_Followers')
from init import *
from random import randint

class AddMeFast:
    def setup(self):
        Setup.init(self)
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

    def surf_website(self):
        self.browser.get('https://addmefast.com/websites')
        while("No item" not in self.browser.page_source):
            sleep(25)
            point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
            print('Your point is: ' + point.text)

    def youtube_view(self):
        self.browser.get('https://addmefast.com/free_points/youtube_views')
        while("No item" not in self.browser.page_source or "orientate" not in self.browser.page_source):
            sleep(4)
            watch = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "View Video"))
            )
            watch.click()
            WebDriverWait(self.browser, 100).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/div[1]/div/strong[2]'))
            )
            point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
            print('Your point is: ' + point.text)
            self.browser.refresh()

    def login_instagram(self):
        self.browser.get('https://www.instagram.com/')

        N = 6

        actions = ActionChains(self.browser)
        for _ in range(N):
            actions = actions.send_keys(Keys.TAB)
        actions.perform()
        actions.send_keys(Keys.RETURN)
        actions.perform()

        username = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username.send_keys(YOUR INSTAGRAM USERNAME)

        password = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password.send_keys(YOUR INSTAGRAM PASSWORD)
        sleep(2)

        actions.send_keys(Keys.RETURN)
        actions.perform()
        sleep(6)

    def instagram_like(self):
        self.browser.get('https://addmefast.com/free_points/instagram_likes')
        while("No item" not in self.browser.page_source):
            sleep(4)
            like = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Like"))
            )
            like.click()
            sleep(4)

            child = self.browser.window_handles[1]
            self.browser.switch_to.window(child)

            do_like = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, '_aamw'))
            )
            do_like.click()
            sleep(10)

            self.browser.close()
            parent = self.browser.window_handles[0]
            self.browser.switch_to.window(parent)
            sleep(2)

            confirm = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Confirm"))
            )
            confirm.click()
            sleep(20)

            point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
            print('Your point is: ' + point.text)
            self.browser.refresh()

    def close_browser(self):
        Setup.close_browser(self)

amf = AddMeFast()
amf.setup()
amf.login_instagram()
while(True):
    amf.surf_website()
    try:
        amf.youtube_view()
    except:
        try:
            amf.instagram_like()
        except:
            delay = randint(1, 300)
            print('We could not find a content to collect points. We are waiting ' + str(delay) + ' seconds...')
            sleep(delay)
