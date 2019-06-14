from selenium.webdriver.common.by import By
from Common.base_page import BasePage, InvalidPageException


class HomePage(BasePage):
    adminManager = (By.XPATH, "//*[@id='3']")

    accounting = (By.NAME, "/admin/adminUser/list")
    accounting_frame = (By.XPATH, '//*[@id="if_16")]')

    role = (By.NAME, "/admin/role/list")
    permission = (By.NAME, "/admin/permission/list")
    allPermission = (By.NAME, "/admin/adminPermission/allPermission")

    def __init__(self, driver):
        super(HomePage, self).__init__(driver)

    # 验证页面是否加载成功
    def _validate_page(self):
        try:
            self.find_element(*self.adminManager)
        except:
            raise InvalidPageException("home page not loaded")

    def click_admin_management_down_accounting(self):
        self.click(*self.adminManager)
        self.click(*self.accounting)
        self.sleep(3)

    def click_admin_management_down_role(self):
        self.click(*self.adminManager)
        self.click(*self.role)
        self.sleep(3)

    def click_admin_management_down_permission(self):
        self.click(*self.adminManager)
        self.click(*self.permission)
        self.sleep(3)

    def click_admin_management_down_all_permission(self):
        self.click(*self.adminManager)
        self.click(*self.allPermission)
        self.sleep(3)

    # 切换框架
    # 通过iframe的id来查询
    def exchange_iframe(self, id):
        self.switch_frame(id)
        self.sleep(3)

    # 返回上一个iframe框架
    def return_parent(self):
        self.return_parent_frame()
        self.sleep(2)
