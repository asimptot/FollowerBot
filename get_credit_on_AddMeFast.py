from time import sleep
import sys
sys.path.append(r'C:\\Projects\\Get_Free_Followers')
from init import *
from random import randint, sample

class AddMeFast:
    def setup(self):
        Setup.init(self)
        sleep(4)
        self.browser.get('https://addmefast.com')
        sleep(4)
        username = self.browser.find_element(By.XPATH, '//*[@id="wrapper"]/section[2]/div/div[4]/form/div[1]/div[1]/input[1]')
        username.send_keys(YOUR ADDMEFAST E-MAIL ADDRESS)

        password = self.browser.find_element(By.XPATH, '//*[@id="wrapper"]/section[2]/div/div[4]/form/div[1]/div[1]/input[2]')
        password.send_keys('YOUR ADDMEFAST PASSWORD)

        button = self.browser.find_element(By.NAME, 'login_button')
        button.click()
        sleep(6)

        if "Login" in self.browser.page_source:
            print('Something went wrong in Addmefast login process.')
        else:
            point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
            print('Logged in AddmeFast. Your current point is: ' + point.text)

    def no_content(self):
        self.browser.save_screenshot('no_content.png')
        sleep(4)
        self.browser.get('https://addmefast.com/bonus_points')
        sleep(4)

        need = self.browser.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[3]/center/div[2]/center/div/font/b')
        need = need.text
        sleep(2)

        try:
            if int(need) >= 100:
                print('Get your daily bonus')
                os._exit(0)
            else:
                sleep(1)
        except:
            sleep(1)
                           
    def login_gmail(self):
        self.browser.get('https://mail.google.com')
        sleep(5)

        actions = ActionChains(self.browser)
        actions.send_keys(YOUR GMAIL ADDRESS).perform()
        sleep(2)
        actions.send_keys(Keys.RETURN).perform()
        sleep(2)

        actions.send_keys(YOUR GMAIL PASSWORD).perform()
        sleep(2)
        actions.send_keys(Keys.RETURN).perform()

        sleep(10)
        if "Inbox" in self.browser.page_source:
            print('Logged in Gmail.')
        else:
            print('Something went wrong in Gmail login process.')

    def login_facebook(self):
        self.browser.get('https://www.facebook.com/')
        sleep(15)

        cookies = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, '_9xo5'))
        )
        cookies.click()
        sleep(5)

        username = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, "email"))
        )
        username.send_keys(YOUR FACEBOOK E-MAIL ADDRESS)

        password = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, "pass"))
        )
        password.send_keys(YOUR FACEBOOK PASSWORD)
        sleep(2)

        actions = ActionChains(self.browser)
        actions.send_keys(Keys.RETURN).perform()
        sleep(10)
        if "Log In" in self.browser.page_source:
            print('Something went wrong in Facebook login process.')
        else:
            print('Logged in Facebook.')

    def login_twitter(self):
        self.browser.get('https://twitter.com/i/flow/login')
        sleep(10)
        N = 3
        actions = ActionChains(self.browser)
        for _ in range(N):
            actions.send_keys(Keys.TAB).perform()
            sleep(2)
        actions.send_keys(YOUR TWITTER USERNAME).perform()
        sleep(2)

        actions.send_keys(Keys.RETURN).perform()
        sleep(2)

        actions.send_keys(YOUR TWITTER PASSWORD).perform()
        sleep(2)

        actions.send_keys(Keys.RETURN).perform()
        sleep(5)

        M = 2
        for _ in range(M):
            actions.send_keys(Keys.TAB).perform()
            sleep(2)
        actions.send_keys(Keys.RETURN).perform()
        sleep(5)
        if "Log in" in self.browser.page_source:
            print('Something went wrong in Twitter login process.')
        else:
            print('Logged in Twitter.')

    def login_instagram(self):
        self.browser.get('https://www.instagram.com/')
        sleep(5)

        cookies = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Only allow essential cookies')]"))
        )
        cookies.click()
        sleep(5)

        N = 2
        actions = ActionChains(self.browser)
        for _ in range(N):
            actions.send_keys(Keys.TAB).perform()
        sleep(2)
        actions.send_keys(Keys.RETURN).perform()
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

        actions.send_keys(Keys.RETURN).perform()
        sleep(10)
        if "Save" in self.browser.page_source:
            print('Logged in Instagram.')
        else:
            print('Something went wrong in Instagram login process.')

    def login_reddit(self):
        self.browser.get('https://www.reddit.com/login/?dest=https%3A%2F%2Fwww.reddit.com%2F')

        username = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        )
        username.send_keys(YOUR REDDIT USERNAME)
        sleep(2)

        password = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        )
        password.send_keys(YOUR REDDIT PASSWORD)
        sleep(2)

        actions = ActionChains(self.browser)
        actions.send_keys(Keys.RETURN).perform()
        sleep(10)

        if "LOG IN" in self.browser.page_source:
            print('Something went wrong in Reddit login process.')
        else:
            print('Logged in Reddit.')

    def login_pinterest(self):
        self.browser.get('https://www.pinterest.com/')
        sleep(4)

        N = 6
        actions = ActionChains(self.browser)
        for _ in range(N):
            actions.send_keys(Keys.TAB).perform()
        actions.send_keys(Keys.RETURN).perform()
        sleep(5)

        actions.send_keys(YOUR PINTEREST E-MAIL ADDRESS).perform()
        sleep(2)
        actions.send_keys(Keys.TAB).perform()
        sleep(2)
        actions.send_keys(YOUR PINTEREST PASSWORD).perform()
        sleep(2)
        actions.send_keys(Keys.RETURN).perform()
        sleep(10)

        if "Log In" in self.browser.page_source:
            print('Something went wrong in Pinterest login process.')
        else:
            print('Logged in Pinterest.')
    
    def login_reverbnation(self):
        self.browser.get('https://www.reverbnation.com/')
        sleep(4)

        sign_in = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Log In')]"))
        )
        sign_in.click()
        sleep(5)
        
        actions = ActionChains(self.browser)
        actions.send_keys(YOUR REVERBNATION E-MAIL ADDRESS).perform()
        sleep(2)
        actions.send_keys(Keys.TAB).perform()
        sleep(2)
        actions.send_keys(YOUR REVERBNATION PASSWORD).perform()
        sleep(2)
        actions.send_keys(Keys.RETURN).perform()
        sleep(10)

        if "Dashboard" in self.browser.page_source:
            print('Logged in Reverbnation.')
        else:
            print('Something went wrong in Reverbnation login process.')
    
    def login_okru(self):
        self.browser.get('https://ok.ru/')
        sleep(4)

        actions = ActionChains(self.browser)
        actions.send_keys(YOUR OKRU E-MAIL ADDRESS).perform()
        sleep(2)
        actions.send_keys(Keys.TAB).perform()
        sleep(2)
        actions.send_keys(YOUR OKRU PASSWORD).perform()
        sleep(2)
        actions.send_keys(Keys.RETURN).perform()
        sleep(10)

        if "Home" in self.browser.page_source:
            print('Logged in Okru.')
        else:
            print('Something went wrong in Ok.ru login process.')
        sleep(2)
                           
    def surf_website(self):
        self.browser.get('https://addmefast.com/websites')
        sleep(4)
        point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point = point.text

        sleep(25)
        point2 = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point2 = point2.text
        sleep(2)
        if point != point2:
            print('Web surfing process is successful. Your point is: ' + point2)
        else:
            print('Something went wrong in web surfing process.')

    def youtube_view(self):
        self.browser.get('https://addmefast.com/free_points/youtube_views')
        sleep(4)
        point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point = point.text
        watch = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "View Video"))
        )
        watch.click()
        WebDriverWait(self.browser, 100).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[1]/div[1]/div/strong[2]'))
        )

        point2 = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point2 = point2.text
        sleep(2)
        if point == point2:
            print('Something went wrong in Youtube view process.')
        else:
            print('Youtube view process is successful. Your point is: ' + point2)

    def instagram_like(self):
        self.browser.get('https://addmefast.com/free_points/instagram_likes')
        sleep(4)
        point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point = point.text
        like = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Like"))
        )
        like.click()
        sleep(4)
        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)

        do_like = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[starts-with(@id,"mount_0_0")]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div[1]/div[1]/article/div/div[3]/div/div/section[1]/span[1]/button'))
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
        point2 = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point2 = point2.text
        sleep(2)
        if point == point2:
            print('Something went wrong in Instagram like process.')
        else:
            print('Instagram like process is successful. Your point is: ' + point2)

    def instagram_follow(self):
        self.browser.get('https://addmefast.com/free_points/instagram')
        sleep(4)
        point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point = point.text
        follow = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Follow"))
        )
        follow.click()
        sleep(4)
        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)
        do_follow = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Follow')]"))
        )
        do_follow.click()
                           
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
        point2 = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point2 = point2.text
        sleep(2)
        if point == point2:
            print('Something went wrong in Instagram follow process.')
        else:
            print('Instagram follow process is successful. Your point is: ' + point2)

    def twitter_follow(self):
        self.browser.get('https://addmefast.com/free_points/twitter')
        sleep(4)
        point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point = point.text
        follow = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Follow"))
        )
        follow.click()
        sleep(7)
        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)
        actions = ActionChains(self.browser)
        actions.send_keys(Keys.RETURN).perform()
        sleep(9)
        self.browser.close()
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)
        sleep(2)
        confirm = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Confirm"))
        )
        confirm.click()
        sleep(20)
        point2 = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point2 = point2.text
        sleep(2)
        if point == point2:
            print('Something went wrong in Twitter follow process.')
        else:
            print('Twitter follow process is successful. Your point is: ' + point2)

    def twitter_like(self):
        self.browser.get('https://addmefast.com/free_points/twitter_likes')
        sleep(4)
        point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point = point.text
        like = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Like"))
        )
        like.click()
        sleep(8)
        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)
        actions = ActionChains(self.browser)
        actions.send_keys(Keys.RETURN).perform()
        sleep(9)
        self.browser.close()
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)
        sleep(2)
        confirm = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Confirm"))
        )
        confirm.click()
        sleep(20)
        point2 = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point2 = point2.text
        sleep(2)
        if point == point2:
            print('Something went wrong in Twitter like process.')
        else:
            print('Twitter like process is successful. Your point is: ' + point2)

    def twitter_retweet(self):
        self.browser.get('https://addmefast.com/free_points/twitter_retweets')
        sleep(4)
        point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point = point.text
        retweet = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Retweet"))
        )
        retweet.click()
        sleep(6.5)
        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)
        actions = ActionChains(self.browser)
        actions.send_keys(Keys.RETURN).perform()
        sleep(9)
        self.browser.close()
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)
        sleep(2)
        confirm = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Confirm"))
        )
        confirm.click()
        sleep(20)
        point2 = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point2 = point2.text
        sleep(2)
        if point == point2:
            print('Something went wrong in Twitter retweet process.')
        else:
            print('Twitter retweet process is successful. Your point is: ' + point2)

    def twitter_tweets(self):
        self.browser.get('https://addmefast.com/free_points/twitter_tweets')
        sleep(4)
        point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point = point.text
        tweet = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Tweet"))
        )
        tweet.click()
        sleep(10)
        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)

        tweet = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/div/div/div/div/div[3]/div/div'))
        )
        tweet.click()

        sleep(30)
        self.browser.close()
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)
        sleep(2)
        confirm = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Confirm"))
        )
        confirm.click()
        sleep(20)
        point2 = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point2 = point2.text
        sleep(2)
        if point == point2:
            print('Something went wrong in Twitter tweets process.')
        else:
            print('Twitter tweets process is successful. Your point is: ' + point2)
        self.browser.save_screenshot('twitter_tweets.png')
        sleep(2)

    def facebook_followers(self):
        self.browser.get('https://addmefast.com/free_points/facebook_subscribes')
        sleep(4)
        point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point = point.text
        like = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Follow"))
        )
        like.click()
        sleep(4)
        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)

        sleep(2)
        actions = ActionChains(self.browser)
        actions.send_keys(Keys.ESCAPE).perform()
        sleep(2)

        try:
            follow = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[starts-with(@id,"mount_0_0")]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div'))
            )
            follow.click()
            sleep(2)
            follow2 = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH,
                                            '//*[starts-with(@id,"mount_0_0")]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[3]/div/div/div'))
            )
            follow2.click()
            sleep(2)

        except:
            try:
                follow3 = WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable((By.XPATH,
                                                '//*[starts-with(@id,"mount_0_0")]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div[3]/div/div/div/div[2]/div/div/div[1]/div'))
                )
                follow3.click()
                sleep(2)
            except:
                try:
                    follow4 = WebDriverWait(self.browser, 10).until(
                        EC.element_to_be_clickable((By.XPATH,
                                                    '//*[starts-with(@id,"mount_0_0")]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[3]/div/div/div'))
                    )
                    follow4.click()
                    sleep(2)
                except:
                    try:
                        follow5 = WebDriverWait(self.browser, 10).until(
                            EC.element_to_be_clickable((By.XPATH,
                                                        '//*[starts-with(@id,"mount_0_0")]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div[1]/div[2]/div/div/div/div[3]/div/div/div/div/div'))
                        )
                        follow5.click()
                        sleep(2)
                    except:
                        try:
                            follow6 = WebDriverWait(self.browser, 10).until(
                                EC.element_to_be_clickable((By.XPATH,
                                                            '//*[starts-with(@id,"mount_0_0")]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div/div[1]/div[2]/div/div/div/div[4]/div/div/div[2]/div/div/div'))
                            )
                            follow6.click()
                            sleep(2)
                        except:
                            sleep(1)
        sleep(5)

        self.browser.close()
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)
        sleep(5)
        confirm = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Confirm"))
        )
        confirm.click()
        sleep(5)
        point2 = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point2 = point2.text
        sleep(2)

        if point == point2:
            print('Something went wrong in Facebook followers process.')
        else:
            print('Facebook followers process is successful. Your point is: ' + point2)

    def facebook_share(self):
        self.browser.get('https://addmefast.com/free_points/facebook_share')
        sleep(4)
        point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point = point.text
        like = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Share"))
        )
        like.click()
        sleep(8)

        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)

        N = 8
        actions = ActionChains(self.browser)
        for _ in range(N):
            actions.send_keys(Keys.TAB).perform()
        sleep(2)
        actions.send_keys(Keys.RETURN).perform()
        sleep(2)
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)
        sleep(15)

        point2 = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point2 = point2.text
        sleep(2)
        if point == point2:
            print('Something went wrong in Facebook share process.')
        else:
            print('Facebook share process is successful. Your point is: ' + point2)

    def facebook_post_like(self):
        self.browser.get('https://addmefast.com/free_points/facebook_post_like')
        sleep(4)
        point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point = point.text
        like = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn3"))
        )
        like.click()
        sleep(4)
        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)

        sleep(2)
        actions = ActionChains(self.browser)
        actions.send_keys(Keys.ESCAPE).perform()
        sleep(2)

        try:
            like = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Like')]"))
            )
            like.click()
        except:
            sleep(1)

        sleep(10)
        self.browser.close()
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)
        sleep(5)
        confirm = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Confirm"))
        )
        confirm.click()
        sleep(5)
        point2 = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point2 = point2.text
        sleep(2)

        if point == point2:
            print('Something went wrong in Facebook post like process.')
        else:
            print('Facebook post like process is successful. Your point is: ' + point2)

    def facebook_post_share(self):
        self.browser.get('https://addmefast.com/free_points/facebook_post_share')
        sleep(4)
        point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point = point.text
        share = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn3"))
        )
        share.click()
        sleep(4)
        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)

        sleep(2)
        actions = ActionChains(self.browser)
        actions.send_keys(Keys.ESCAPE).perform()
        sleep(2)

        try:
            share = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Share')]"))
            )
            share.click()
            sleep(2)

            now = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Post')]"))
            )
            now.click()
            sleep(2)

        except:
            sleep(1)

        sleep(10)
        self.browser.close()
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)
        sleep(5)
        confirm = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Confirm"))
        )
        confirm.click()
        sleep(10)
        point2 = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point2 = point2.text
        sleep(2)

        if point == point2:
            print('Something went wrong in Facebook post share process.')
        else:
            print('Facebook post share process is successful. Your point is: ' + point2)

    def reddit_members(self):
        self.browser.get('https://addmefast.com/free_points/reddit_members')
        sleep(4)
        point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point = point.text
        join = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Join"))
        )
        join.click()
        sleep(8)

        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)

        if "Joined" in self.browser.page_source:
            self.browser.close()
        else:
            do_join = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Join')]"))
            )
            do_join.click()
            sleep(15)
            self.browser.close()
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)
        sleep(20)

        point2 = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point2 = point2.text
        sleep(2)
        if point == point2:
            print('Something went wrong in Reddit members process.')
        else:
            print('Reddit members process is successful. Your point is: ' + point2)

    def reddit_upvotes(self):
        self.browser.get('https://addmefast.com/free_points/reddit_upvotes')
        sleep(4)
        point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point = point.text
        upvote = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Upvote"))
        )
        upvote.click()
        sleep(8)

        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)

        try:
            do_upvote = WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "voteButton "))
            )
            do_upvote.click()
        except:
            sleep(1)
        
        sleep(19)
        self.browser.close()
                
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)
        sleep(10)

        point2 = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point2 = point2.text
        sleep(2)
        if point == point2:
            print('Something went wrong in Reddit upvotes process.')
        else:
            print('Reddit upvotes process is successful. Your point is: ' + point2)

    def youtube_subscribe(self):
        self.browser.get('https://addmefast.com/free_points/youtube_subscribe')
        sleep(4)
        point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point = point.text
        subscribe = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Subscribe"))
        )
        subscribe.click()
        sleep(8)

        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)

        N = 9
        actions = ActionChains(self.browser)
        for _ in range(N):
            actions.send_keys(Keys.TAB).perform()
        sleep(2)
        actions.send_keys(Keys.RETURN).perform()

        sleep(9)
        self.browser.close()
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)
        sleep(20)

        point2 = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point2 = point2.text
        sleep(2)
        if point == point2:
            print('Something went wrong in Youtube subscribe process.')
        else:
            print('Youtube subscribe process is successful. Your point is: ' + point2)

    def pinterest_save(self):
        self.browser.get('https://addmefast.com/free_points/pinterest_save')
        sleep(4)
        point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point = point.text
        save = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Save"))
        )
        save.click()
        sleep(8)

        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)

        do_save = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Save')]"))
        )
        do_save.click()

        sleep(10)
        self.browser.close()
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)
        sleep(20)

        point2 = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point2 = point2.text
        sleep(2)
        if point == point2:
            print('Something went wrong in Pinterest save process.')
        else:
            print('Pinterest save process is successful. Your point is: ' + point2)

    def pinterest_followers(self):
        self.browser.get('https://addmefast.com/free_points/pinterest')
        sleep(4)
        point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point = point.text
        follow = WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Follow"))
        )
        follow.click()
        sleep(8)

        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)

        do_follow = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Follow')]"))
        )
        do_follow.click()

        sleep(10)
        self.browser.close()
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)
        sleep(20)

        point2 = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point2 = point2.text
        sleep(2)
        if point == point2:
            print('Something went wrong in Pinterest follow process.')
        else:
            print('Pinterest follow process is successful. Your point is: ' + point2)

    def reverbnation_fan(self):
        self.browser.get('https://addmefast.com/free_points/reverbnation_fan')
        sleep(4)
        point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point = point.text
        be_a_fan = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn3"))
        )
        be_a_fan.click()
        sleep(8)

        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)

        do_be_a_fan = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Become A Fan')]"))
        )
        do_be_a_fan.click()

        sleep(15)
        self.browser.close()
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)
        sleep(20)

        point2 = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point2 = point2.text
        sleep(2)
        if point == point2:
            print('Something went wrong in Reverbnation fan process.')
        else:
            print('Reverbnation fan process is successful. Your point is: ' + point2)

    def okru_join(self):
        self.browser.get('https://addmefast.com/free_points/ok_group_join')
        sleep(4)
        point = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point = point.text
        join = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "btn3"))
        )
        join.click()
        sleep(8)

        child = self.browser.window_handles[1]
        self.browser.switch_to.window(child)

        do_join = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Join')]"))
        )
        do_join.click()

        sleep(15)
        self.browser.close()
        parent = self.browser.window_handles[0]
        self.browser.switch_to.window(parent)
        sleep(20)

        point2 = self.browser.find_element(By.XPATH, '//*[@id="toppointsbalance"]')
        point2 = point2.text
        sleep(2)
        if point == point2:
            print('Something went wrong in Ok.Ru join process.')
        else:
            print('Ok.Ru join fan process is successful. Your point is: ' + point2)

    def close_browser(self):
        Setup.close_browser(self)

amf = AddMeFast()
amf.setup()

amf.login_facebook()
amf.login_gmail()
amf.login_instagram()
amf.login_okru()
amf.login_pinterest()
amf.login_reddit()
amf.login_reverbnation()
amf.login_twitter()

array = [amf.surf_website, amf.youtube_view, amf.twitter_like, amf.twitter_retweet, amf.twitter_follow,
         amf.twitter_tweets, amf.instagram_like, amf.instagram_follow, amf.facebook_followers, 
         amf.facebook_share, amf.facebook_post_like, amf.facebook_post_share, amf.reddit_members, amf.reddit_upvotes,
         amf.youtube_subscribe, amf.pinterest_save, amf.pinterest_followers, amf.reverbnation_fan, amf.okru_join]

while(True):
    list = sample(array, len(array))
    for i in range(len(array)):
        try:
            list[i]()
        except:
            amf.no_content()
            delay = randint(10, 30)
            print('We could not find a content to collect points. We are waiting ' + str(delay) + ' seconds...')
            sleep(delay)
