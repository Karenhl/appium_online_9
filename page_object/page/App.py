from page_object.driver.Client import AndroidClient
from page_object.page.BasePage import BasePage
from page_object.page.MainPage import MainPage


class App(BasePage):
    @classmethod
    def main(cls):
        cls.get_client().restart_app()
        return MainPage()
