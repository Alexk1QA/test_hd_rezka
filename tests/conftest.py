
from locators.locators_hd_rezka import BaseLocator
from base_class.main_driver import *
import pytest as pytest
import pyperclip


@pytest.fixture()
def get_temp_mail_io():
    service = Service(ChromeDriverManager().install())

    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(service=service, chrome_options=options)

    driver.get("https://tempmail.io/")
    driver.find_element(Driver.get_driver_by("xpath"), BaseLocator.TEMPMAILIO).click()
    driver.quit()
    return pyperclip.paste()
