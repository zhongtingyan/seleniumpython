from selenium.webdriver.common.by import By
from Common.base_page import BasePage, InvalidPageException


class LogoutPage(BasePage):
    # 设置button
    set_up_button = (By.ID, 'id-adminName')
    # 退出登录button
    logout_button = (By.XPATH, '//a[@href="/logout"]')

    def __init__(self, driver):
        super(LogoutPage, self).__init__(driver)

    # 验证页面是否加载成功
    def _validate_page(self):
        try:
            self.find_element(*self.set_up_button)
        except:
            raise InvalidPageException("logout page not loaded")

    # 退出登录
    def test_user_logout(self):
        self.retryingFindClick(*self.set_up_button)
        self.retryingFindClick(*self.logout_button)
        self.sleep(3)
