from page_object.page.App import App
import pytest


class TestLogin(object):
    @classmethod
    def setup_class(cls):
        cls.profilePage = App.main().goto_profile()

    def setup_method(self):
        self.loginPage = self.profilePage.goto_login()

    @pytest.mark.parametrize("user, pw, msg", [
        ("156005347600", "111111", "手机号码"),
        ("15600534760", "111111", "密码错误")
    ])
    def test_login_password(self, user, pw, msg):
        self.loginPage.login_by_password(user, pw)
        assert msg in self.loginPage.get_error_msg()

    def teardown_method(self):
        self.loginPage.back()
