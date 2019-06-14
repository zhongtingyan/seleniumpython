'''
管理员管理--帐号管理
'''
from selenium.webdriver.common.by import By
from Common.base_page import BasePage, InvalidPageException
from time import sleep


class Accounting(BasePage):
    # 管理员名称
    name = (By.ID, "name")
    # 停用状态  select下拉框
    loginflag = (By.ID, "loginFlag")
    # 开始时间  时间选择框
    startdate = (By.ID, "startdate")
    # 结束时间  时间选择框
    enddate = (By.ID, "enddate")
    # 电话号码
    phone = (By.ID, "phone")
    # 邮箱地址
    email = (By.ID, "email")
    # 管理员id
    adminid = (By.ID, "admin_id")
    # 角色  select下拉框
    role = (By.ID, "roleId")
    # 添加帐号
    btn_add = (By.XPATH, "")
    # 查询
    btn_find = (By.XPATH, "//button[@type='submit']")
    # btn_find = (By.XPATH, "//*[@id='adminForm']/div[3]/div/button[1]")
    # 重置
    btn_reset = (By.ID, "reset")

    def __init__(self, driver):
        super(Accounting, self).__init__(driver)

    # 验证页面是否加载成功
    def _validate_page(self):
        try:
            self.find_element(*self.name)
        except:
            raise InvalidPageException("accounting page not loaded")

    # 查询管理员名称
    def search_by_name(self, name):
        self.wait(3)
        self.type(*self.name, text=name)
        # self.click(*self.btn_find)
        self.retryingFindClick(*self.btn_find)
        self.sleep(5)

