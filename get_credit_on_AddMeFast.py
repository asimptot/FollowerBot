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
        username.send_keys(YOUR ADDMEFAST E-MAIL ADDRESS)

        password = self.browser.find_element(By.XPATH, '//*[@id="wrapper"]/section[2]/div/div[4]/form/div[1]/div[1]/input[2]')
        password.send_keys(YOUR ADDMEFAST PASSWORD)

        button = self.browser.find_element(By.NAME, 'login_button')
        button.click()
        sleep(6)
        print('Logged in AddmeFast!')

    def surf_website(self):
        self.browser.get('https://addmefast.com/websites')
        while("No item" not in self.browser.page_source):
            sleep(25)
            point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
            print('Web surfing process is successfull! Your point is: ' + point.text)

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
            print('Youtube view process is successfull! Your point is: ' + point.text)
            self.browser.refresh()

    def login_instagram(self):
        self.browser.get('https://www.instagram.com/')
        sleep(10)
        N = 2
        
        actions = ActionChains(self.browser)
        for _ in range(N):
            actions = actions.send_keys(Keys.TAB)
        actions.perform()
        actions.send_keys(Keys.RETURN)
        actions.perform()
        sleep(5)

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
        sleep(10)
        print('Logged in Instagram!')

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
                EC.presence_of_element_located((By.CLASS_NAME, '_aamw') or (By.XPATH, '//*[@id="mount_0_0_in"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[3]/div/div/section[1]/span[1]/button/div/span/svg/path')
                                               or (By.CLASS_NAME, '_ab6-') or (By.XPATH, '//*[@id="mount_0_0_0i"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[3]/div/div/section[1]/span[1]/button/div[2]/span/svg'))
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
            print('Instagram like process is successfull! Your point is: ' + point.text)
            self.browser.refresh()

    def login_twitter(self):
        self.browser.get('https://twitter.com/i/flow/login')

        N = 4
        actions = ActionChains(self.browser)
        for _ in range(N):
            actions.send_keys(Keys.TAB)
            actions.perform()
            sleep(2)
        actions.perform()
        sleep(5)
        actions.send_keys(YOUR TWITTER USERNAME')
        actions.perform()
        sleep(2)

        actions.send_keys(Keys.RETURN)
        actions.perform()
        sleep(2)

        actions.send_keys(YOUR TWITTER PASSWORD)
        actions.perform()
        sleep(2)

        actions.send_keys(Keys.RETURN)
        actions.perform()
        sleep(5)

        M = 2
        for _ in range(M):
            actions.send_keys(Keys.TAB)
            actions.perform()
            sleep(2)
        actions.perform()
        sleep(5)
        print('Logged in Twitter!')

    def twitter_follow(self):
        self.browser.get('https://addmefast.com/free_points/twitter')
        while("No item" not in self.browser.page_source):
            sleep(4)
            follow = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Follow"))
            )
            follow.click()
            sleep(10)

            child = self.browser.window_handles[1]
            self.browser.switch_to.window(child)

            actions = ActionChains(self.browser)
            actions.send_keys(Keys.RETURN)
            actions.perform()
            sleep(15)

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
            print('Twitter follow process is successfull! Your point is: ' + point.text)
            self.browser.refresh()

    def twitter_like(self):
        self.browser.get('https://addmefast.com/free_points/twitter_likes')
        while("No item" not in self.browser.page_source):
            sleep(4)
            like = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Like"))
            )
            like.click()
            sleep(10)

            child = self.browser.window_handles[1]
            self.browser.switch_to.window(child)

            actions = ActionChains(self.browser)
            actions.send_keys(Keys.RETURN)
            actions.perform()
            sleep(15)

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
            print('Twitter like process is successfull! Your point is: ' + point.text)
            self.browser.refresh()

    def twitter_retweet(self):
        self.browser.get('https://addmefast.com/free_points/twitter_retweets')
        while("No item" not in self.browser.page_source):
            sleep(4)
            retweet = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Retweet"))
            )
            retweet.click()
            sleep(10)

            child = self.browser.window_handles[1]
            self.browser.switch_to.window(child)

            actions = ActionChains(self.browser)
            actions.send_keys(Keys.RETURN)
            actions.perform()
            sleep(15)

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
            print('Retweet process is successfull! Your point is: ' + point.text)
            self.browser.refresh()

    def close_browser(self):
        Setup.close_browser(self)

amf = AddMeFast()
amf.setup()
amf.login_twitter()
amf.login_instagram()

while(True):
    amf.surf_website()
    try:
        amf.youtube_view()
    except:
        try:
            amf.twitter_follow()
        except:
            try:
                amf.twitter_like()
            except:
                try:
                    amf.twitter_retweet()
                except:
                    try:
                        amf.instagram_like()
                    except:
                        delay = randint(1, 300)
                        print('We could not find a content to collect points. We are waiting ' + str(delay) + ' seconds...')
                        sleep(delay)
