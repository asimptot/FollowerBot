import sys
sys.path.append(r'C:\\Projects\\Get_Free_Followers')
from init import *

username = input('What is your Instagram username?\n')
print('Getting followers... Please do not terminate the program.')

class Instagram:
    def setup(self):
        Setup.init(self)

    def go_to_website(self):
        sleep(4)
        self.browser.get('https://tolinay.com/instagram-takipci-hilesi')
        sleep(4)

        uid = self.browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/form/div/div[1]/input')
        uid.send_keys(username)
        sleep(5)
        button = self.browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/form/div/div[3]/button')
        button.click()
        sleep(5)

        element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/div/div[1]/div'))
        WebDriverWait(self.browser, 1000).until(element_present)

        if("Başarıyla Gönderildi" in self.browser.page_source):
            print(f"\n10 followers followed you!")

        elif("Çok Hızlı İşlem Yapıyorsunuz" in self.browser.page_source):
            print(f"\nError! Do not run the program fast mode!")

        else:
            print(f"\nError! Your credits have been expired! Please change your Instagram username.")

    def login_gmail(self):
        self.browser.get('https://mail.google.com')
        sleep(5)

        actions = ActionChains(self.browser)
        actions.send_keys('YOUR GMAIL ADDRESS').perform()
        sleep(2)
        actions.send_keys(Keys.RETURN).perform()
        sleep(2)

        actions.send_keys('YOUR GMAIL PASSWORD').perform()
        sleep(2)
        actions.send_keys(Keys.RETURN).perform()
        sleep(10)
        self.browser.switch_to.new_window(WindowTypes.TAB)

    def close_browser(self):
        Setup.close_browser(self)

ig = Instagram()

while(True):
    ig.setup()
    ig.login_gmail()
    try:
        ig.go_to_website()
        ig.close_browser()
    except:
        print('An error has been occurred. Retrying...')
