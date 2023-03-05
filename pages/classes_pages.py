
from base_class.main_driver import Driver
from locators.locators_hd_rezka import BaseLocator
import time


class MainPage(Driver):

    def get_lists_groups(self):
        first_window = self.driver.window_handles[0]
        self.driver.switch_to.window(first_window)
        self.driver.get("https://rezka.ag/")
        time.sleep(2)


class RegistrationPage(Driver):
    def registration(self, temp_mail):
        first_window = self.driver.window_handles[0]
        self.driver.switch_to.window(first_window)
        self.driver.get("https://rezka.ag/")

        self.driver.find_element(Driver.get_driver_by("xpath"), BaseLocator.REGISTRATION_BUTTON_ON_MAIN_PAGE).click()
        time.sleep(1)
        self.driver.find_element(Driver.get_driver_by("xpath"), BaseLocator.POPUP_REG_EMAIL).send_keys(temp_mail)
        time.sleep(1)
        self.driver.find_element(Driver.get_driver_by("xpath"), BaseLocator.POPUP_REG_LOGIN).send_keys(
            temp_mail.split('@')[0])
        time.sleep(1)
        self.driver.find_element(Driver.get_driver_by("xpath"), BaseLocator.POPUP_REG_PASS).send_keys(temp_mail)
        time.sleep(1)
        self.driver.find_element(Driver.get_driver_by("xpath"), BaseLocator.POPUP_REGISTRATION_CONFIRM).click()
        time.sleep(3)
