from selenium.webdriver.common.by import By
from Common.base_page import BasePage, InvalidPageException


class LoginPage(BasePage):
    # 账号input
    username_input = (By.ID, 'phoneNum')
    # 密码input
    password_input = (By.NAME, 'password')
    # 登录button
    submit_button = (By.CLASS_NAME, 'login100-form-btn')

    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    # 验证页面是否加载成功
    def _validate_page(self):
        try:
            self.find_element(*self.username_input)
            self.find_element(*self.password_input)
        except:
            raise InvalidPageException("login page not loaded")

    def test_user_login(self, username, password):
        self.wait(3)
        self.type(*self.username_input, text=username)
        self.type(*self.password_input, text=password)
        self.click(*self.submit_button)
        self.sleep(5)
