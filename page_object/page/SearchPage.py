from selenium.webdriver.common.by import By

from page_object.page.BasePage import BasePage


class SearchPage(BasePage):
    _edit_locator=(By.CLASS_NAME, "android.widget.EditText")

    def search(self, key):
        self.find(self._edit_locator).send_keys(key)
        return self

    def add_to_selected(self, key):
        follow_button = (By.XPATH,
                         "//*[contains(@resource-id, 'stockCode') and contains(@text,'%s')]/../../.." % key +
                         "//*[contains(@resource-id, 'follow_btn')]")

        self.find(follow_button).click()
        return self

    def remove_from_selected(self, key):
        followed_button = (By.XPATH,
                         "//*[contains(@resource-id, 'stockCode') and contains(@text,'%s')]/../../.." % key +
                         "//*[contains(@resource-id, 'followed_btn')]")

        self.find(followed_button).click()
        return self

    def is_in_selected(self, key):
        follow_button=(By.XPATH,
                       "//*[contains(@resource-id, 'stockCode') and contains(@text,'%s')]/../../.." %key +
                       "//*[contains(@resource-id, 'follow')]")
        id=self.find(follow_button).get_attribute("resourceId")
        print(id)
        return "followed_btn" in id

    def cancel(self):
        self.find_by_text("取消").click()

    def search_by_user(self, key):
        # todo: 作业2
        pass

    def is_followed(self):
        # todo: 作业2
        pass
