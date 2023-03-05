
from pages.classes_pages import *


class TestAll:

    def test_list_groups(self):
        hd_rezka = MainPage()
        hd_rezka.get_lists_groups()

        result = []
        for locator in BaseLocator.AR_GROUPS_SELECTORS:
            result.append(hd_rezka.get_element_text("xpath", locator))

        assert result == BaseLocator.ER_GROUPS_SELECTORS
