
from pages.classes_pages import *


class TestAll:

    def test_list_groups(self):
        hd_rezka = MainPage()
        hd_rezka.get_lists_groups()

        result = []
        for locator in BaseLocator.AR_GROUPS_SELECTORS:
            result.append(hd_rezka.get_element_text("xpath", locator))

        assert result == BaseLocator.ER_GROUPS_SELECTORS

    def test_registration(self, get_temp_mail_io):

        hd_rezka = RegistrationPage()
        hd_rezka.registration(get_temp_mail_io)

        assert hd_rezka.get_element_text("xpath", BaseLocator.AR_ACCEPT_REG) == BaseLocator.ER_ACCEPT_REG

    def test_login(self):

        hd_rezka = LoginPage()
        hd_rezka.login()

        assert hd_rezka.get_element_text("xpath", BaseLocator.AR_ACCEPT_LOG) == BaseLocator.ER_ACCEPT_LOG




