from selenium.webdriver.common.by import By

from page_object.page.BasePage import BasePage
from page_object.page.ProfilePage import ProfilePage
from page_object.page.SearchPage import SearchPage
from page_object.page.SelectedPage import SelectedPage


class MainPage(BasePage):
    _profile_button=(By.ID, "user_profile_icon")
    _search_button = (By.ID, "home_search")

    def goto_selected(self):
        # 调用全局的driver对象使用webdriver api操纵app

        # self.driver.find_element(By.xpath, "//*[@text='自选']")
        zixuan = "自选"
        self.find_by_text(zixuan)
        # self.driver.find_element_by_xpath("//*[@text='自选']")
        self.find_by_text(zixuan).click()

        return SelectedPage()

    def goto_search(self) -> SearchPage:
        self.find(self._search_button).click()
        return SearchPage()

    def goto_profile(self):
        # self.find(MainPage._profile_button).click()
        self.load_steps("../data/MainPage.yaml", "goto_profile")
        return ProfilePage()
