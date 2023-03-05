
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver


class Driver:
    def __init__(self):
        self.service = Service(ChromeDriverManager().install())

        self.options = Options()

        driver = webdriver.Chrome(service=self.service, options=self.options)
        driver.maximize_window()
        self.driver = driver

    @staticmethod
    def get_driver_by(find_by: str):
        locating_elements = {
            "id": By.ID,
            "name": By.NAME,
            "xpath": By.XPATH,
            "class_name": By.CLASS_NAME,
            "css": By.CSS_SELECTOR,
            "tag_name": By.TAG_NAME,
        }
        return locating_elements[find_by.lower()]

    def get_element_text(self, find_by: str, locator: str):
        return self.driver.find_element(self.get_driver_by(find_by), locator).text

    def refresh_page(self):
        self.driver.refresh()

    def get_url(self, url: str) -> webdriver:
        self.driver.get(url)

    def quit_browser(self):
        self.driver.quit()
