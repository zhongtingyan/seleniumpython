from PageObjects.login_page import LoginPage
from PageObjects.home_page import HomePage
from PageObjects.loginout_page import LogoutPage
from PageObjects.accounting_page import Accounting
from Common.base_method import BaseTestCase
import unittest


class Test(BaseTestCase):

    def test_1_login_page(self):
        # loginPage实例化
        self.loginPage1 = LoginPage(self.driver)
        # 登录
        self.loginPage1.test_user_login("18923706040", "123456")

        # 总后台首页实例化
        self.homePage1 = HomePage(self.loginPage1.driver)
        # 点击导航栏菜单
        self.homePage1.click_admin_management_down_accounting()
        self.homePage1.img_screenshot(u"测测")

        # 切换框架
        self.homePage1.exchange_iframe("if_16")
        # 实例化帐号管理页面
        self.accountingPage1 = Accounting(self.loginPage1.driver)
        self.accountingPage1.search_by_name("admin")

        # 切换回上一个框架
        self.homePage1.return_parent_frame()

        self.logoutPage1 = LogoutPage(self.loginPage1.driver)
        # 退出登录
        self.logoutPage1.test_user_logout()


if __name__ == "__main__":
    unittest.main(verbosity=2)
