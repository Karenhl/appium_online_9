from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from page_object.driver.Client import AndroidClient
from page_object.page.BasePage import BasePage


class SelectedPage(BasePage):
    def add_default(self):
        return self

    def goto_hs(self):
        self.find_by_text("沪深").click()
        return self

    def get_price_by_name(self, name) -> float:
        priceLocator = (MobileBy.XPATH, "//*[contains(@resource-id, 'stockName') and @text='%s']" %name +
             "/../../..//*[contains(@resource-id, 'currentPrice')]")
        price = self.find(priceLocator).text
        return float(price)
