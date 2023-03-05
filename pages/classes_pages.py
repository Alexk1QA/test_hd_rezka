
from base_class.main_driver import Driver
from locators.locators_hd_rezka import BaseLocator
import time


class MainPage(Driver):

    def get_lists_groups(self):
        first_window = self.driver.window_handles[0]
        self.driver.switch_to.window(first_window)
        self.driver.get("https://rezka.ag/")
        time.sleep(2)
