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

        try:
            uid = self.browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/form/div/div[1]/input')
            uid.send_keys(username)
            sleep(5)
            button = self.browser.find_element(By.XPATH, '/html/body/div[3]/div[2]/div[2]/form/div/div[3]/button')
            button.click()
            sleep(5)

            element_present = EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div[2]/div[1]/div/div/div[1]/div'))
            WebDriverWait(self.browser, 1000).until(element_present)
        except:
            print('\nSomething went wrong!\n')

        if("Başarıyla Gönderildi" in self.browser.page_source):
            print(f"\n20 followers followed you!")

        elif("Çok Hızlı İşlem Yapıyorsunuz" in self.browser.page_source):
            print(f"\nError! Do not run the program fast mode!")

    def close_browser(self):
        Setup.close_browser(self)

ig = Instagram()
ig.setup()

while(True):
    ig.go_to_website()
