from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import warnings

class Setup:
    def init(self):
        warnings.filterwarnings("ignore")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1036, 674')
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_argument('--headless')
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 1
        })
        self.browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chrome_options, )

    def close_browser(self):
        self.browser.close()
