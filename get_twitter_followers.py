from time import sleep
import sys
sys.path.append(r'C:\\Projects\\Get_Free_Followers')
from init import *
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

username = input('What is your username?\n')

class Twitter:

    def setup(self):
        Setup.init(self)

    def go_to_website(self):
        sleep(4)
        self.browser.get('https://www.youlikehits.com/login.php')
        sleep(10)

        uid = self.browser.find_element(By.ID, 'username')
        uid.send_keys('maguire_reyiz') #tewep47442@haboty.com
        sleep(2)

        pwd = self.browser.find_element(By.ID, 'password')
        pwd.send_keys('123abc123ABC*')
        sleep(2)

        btn = self.browser.find_element(By.XPATH, '/html/body/table[2]/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[2]/td/center/form/table/tbody/tr[3]/td/span/input')
        btn.click()
        sleep(2)

        self.browser.get('https://www.youlikehits.com/newaddtwitter.php')
        sleep(5)

        actions = ActionChains(self.browser)

        tid = self.browser.find_element(By.ID, 'username')
        tid.send_keys(username)
        sleep(2)

        tid_btn = self.browser.find_element(By.CLASS_NAME, 'followbutton')
        tid_btn.click()
        sleep(2)

        self.browser.refresh()
        sleep(5)

        N = 15  # number of times you want to press TAB

        for _ in range(N):
            actions = actions.send_keys(Keys.TAB)
        actions.perform()
        sleep(2)

        actions.send_keys(Keys.RETURN)
        actions.perform()
        sleep(2)

        self.browser.get('https://www.youlikehits.com/newaddtwitter.php')
        sleep(5)

        N = 14  # number of times you want to press TAB

        for _ in range(N):
            actions = actions.send_keys(Keys.TAB)
        actions.perform()
        sleep(2)

        actions.send_keys(Keys.RETURN)
        actions.perform()
        sleep(2)

        actions.send_keys('30')
        actions.perform()
        sleep(2)

        actions.send_keys(Keys.RETURN)
        actions.perform()
        sleep(2)

        self.browser.get('https://www.youlikehits.com/websites.php')

        while(True):
            N = 15  # number of times you want to press TAB
            sleep(5)

            for _ in range(N):
                actions = actions.send_keys(Keys.TAB)
            actions.perform()
            sleep(2)

            actions.send_keys(Keys.RETURN)
            actions.perform()
            sleep(30)

            self.browser.switch_to.window(self.browser.window_handles[1])
            self.browser.close()
            sleep(5)
            self.browser.switch_to.window(self.browser.window_handles[0])
            self.browser.refresh()

    def close_browser(self):
        Setup.close_browser(self)

twt = Twitter()
twt.setup()

while(True):
    twt.go_to_website()
twt.close_browser()