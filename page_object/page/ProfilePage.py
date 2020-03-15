from page_object.page.BasePage import BasePage
from page_object.page.LoginPage import LoginPage


class ProfilePage(BasePage):
    def goto_login(self):
        # self.find_by_text("点击登录").click()
        self.load_steps("../data/ProfilePage.yaml", "goto_login")
        return LoginPage()
