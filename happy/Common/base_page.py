import time
from abc import abstractmethod
from configuration.globalparameter import img_path

from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from Common import log


class BasePage(object):
    """
    定义一个页面基类，让所有页面都继承这个类，封装一些常用的页面操作方法到这个类
    """

    def __init__(self, driver):
        self.driver = driver
        self.mylog = log.log()

    @abstractmethod
    def _validate_page(self):
        '''
        使用了@abstractmethod进行装饰，基类不能被实例化
        只有当子类继承并且实现了该方法后子类才可以实例化
        这样可以对不同的页面进行不同的验证
        :return:
        '''
        return

    # quit browser and end testing
    def quit_browser(self):
        self.driver.quit()

    # 浏览器前进操作
    def forward(self):
        self.driver.forward()
        self.mylog.info("Click forward on current page.")

    # 浏览器后退操作
    def back(self):
        self.driver.back()
        self.mylog.info("Click back on current page.")

    # 隐式等待
    def wait(self, seconds):
        self.driver.implicitly_wait(seconds)
        self.mylog.info("wait for %d seconds." % seconds)

    # 点击关闭当前窗口
    def close(self):
        try:
            self.driver.close()
            self.mylog.info("Closing and quit the browser.")
        except NameError as e:
            self.mylog.error("Failed to quit the browser with %s" % e)

    '''
    # 保存图片
    def get_windows_img(self):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\image下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/image/'
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq + '.png'
        try:
            self.driver.get_screenshot_as_file(screen_name)
            self.mylog.info("Had take screenshot and save to folder : /image")
        except NameError as e:
            self.mylog.error("Failed to take screenshot! %s" % e)
            self.get_windows_img()
    '''

    # 截图
    # 直接使用配置文件的内容来保存截图
    def img_screenshot(self, img_name):
        try:
            self.driver.get_screenshot_as_file(img_path + img_name + '.png')
        except:
            self.mylog.error(u'截图失败：' + img_name)

    # 定位元素方法
    # def find_element(self, selector):
    #     """
    #      这个地方为什么是根据=>来切割字符串，请看页面里定位元素的方法
    #      submit_btn = "id=>su"
    #      login_lnk = "xpath => //*[@id='u1']/a[7]"  # 百度首页登录链接定位
    #      如果采用等号，结果很多xpath表达式中包含一个=，这样会造成切割不准确，影响元素定位
    #     :param selector:
    #     :return: element
    #     """
    #     element = ''
    #     if '=>' not in selector:
    #         return self.driver.find_element_by_id(selector)
    #     selector_by = selector.split('=>')[0]
    #     selector_value = selector.split('=>')[1]
    #
    #     if selector_by == "i" or selector_by == 'id':
    #         try:
    #             element = self.driver.find_element_by_id(selector_value)
    #             logging.info("Had find the element \' %s \' successful "
    #                          "by %s via value: %s " % (element.text, selector_by, selector_value))
    #         except NoSuchElementException as e:
    #             logging.error("NoSuchElementException: %s" % e)
    #             self.get_windows_img()  # take screenshot
    #     elif selector_by == "n" or selector_by == 'name':
    #         element = self.driver.find_element_by_name(selector_value)
    #     elif selector_by == "c" or selector_by == 'class_name':
    #         element = self.driver.find_element_by_class_name(selector_value)
    #     elif selector_by == "l" or selector_by == 'link_text':
    #         element = self.driver.find_element_by_link_text(selector_value)
    #     elif selector_by == "p" or selector_by == 'partial_link_text':
    #         element = self.driver.find_element_by_partial_link_text(selector_value)
    #     elif selector_by == "t" or selector_by == 'tag_name':
    #         element = self.driver.find_element_by_tag_name(selector_value)
    #     elif selector_by == "x" or selector_by == 'xpath':
    #         try:
    #             element = self.driver.find_element_by_xpath(selector_value)
    #             logging.info("Had find the element \' %s \' successful "
    #                          "by %s via value: %s " % (element.text, selector_by, selector_value))
    #         except NoSuchElementException as e:
    #             logging.error("NoSuchElementException: %s" % e)
    #             self.get_windows_img()
    #     elif selector_by == "s" or selector_by == 'selector_selector':
    #         element = self.driver.find_element_by_css_selector(selector_value)
    #     else:
    #         raise NameError("Please enter a valid type of targeting elements.")
    #
    #     return element

    #   重写find_element方法，增加定位元素的健壮性
    def find_element(self, *loc):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            self.mylog.error(u'找不到元素:' + str(loc))

    '''
    # 输入
    def type(self, selector, text):

        el = self.find_element(selector)
        el.clear()
        try:
            el.send_keys(text)
            logging.info("Had type \' %s \' in inputBox" % text)
        except NameError as e:
            logging.error("Failed to type in input box with %s" % e)
            self.get_windows_img()
    '''

    #   重写send_keys方法
    def type(self, *loc, text):
        try:
            self.find_element(*loc).clear()
            self.find_element(*loc).send_keys(text)
        except AttributeError:
            self.mylog.error(u'输入失败,loc=' + str(loc) + u';value=' + text)

    # 清除文本框
    def clear(self, selector):

        el = self.find_element(selector)
        try:
            el.clear()
            self.mylog.info("Clear text in input box before typing.")
        except NameError as e:
            self.mylog.error("Failed to clear in input box with %s" % e)
            self.get_windows_img()

    # 点击元素
    def click(self, *loc):

        el = self.find_element(*loc)
        try:
            el.click()
            self.mylog.info("The element \' %s \' was clicked." % el.text)
            # logging.info("The element \' %s \' was clicked." % el.text)
        except NameError as e:
            # logging.error("Failed to click the element with %s" % e)
            self.mylog.error("Failed to click the element with %s" % e)

    '''
    当报“Message: stale element reference: element is not attached to the page document”
    使用该方法来代替click事件
    '''

    def retryingFindClick(self, *loc):
        self.mylog.info("等待指定元素出现")
        result = False
        attempts = 0
        while attempts < 2:
            try:
                self.find_element(*loc).click()
                result = True
                break
            except StaleElementReferenceException:
                pass
            attempts += 1
            self.mylog.info("扫描开始，元素开始第" + attempts + "次扫描")
        self.mylog.info("扫描结束")
        return result

    # 或者网页标题
    def get_page_title(self):
        self.mylog.info("Current page title is %s" % self.driver.title)
        return self.driver.title

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
        # self.mylog.info("Sleep for %d seconds" % seconds)

    # 定位select下拉框，并通过index选择元素
    def sel_by_index(self, loc, index):
        try:
            loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
            Select(self.find_element(*loc)).select_by_index(index)
        except AttributeError:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    # 定位select下拉框，并通过value选择元素
    def sel_by_value(self, loc, value):
        try:
            loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
            Select(self.find_element(*loc)).select_by_value(value)
        except AttributeError:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    # 定位select下拉框，并通过选项文字选择元素
    def sel_by_visible_text(self, loc, text):
        try:
            loc = getattr(self, "_%s" % loc)  # getattr相当于实现self.loc
            Select(self.find_element(*loc)).select_by_visible_text(text)
        except AttributeError:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    '''
    使用self.driver.switch_to_frame(id)会提示 DeprecationWarning: use driver.switch_to.frame instead return self.driver.switch_to_frame(id)
    按照提示修改即可
    '''

    # 重写switch_frame方法
    def switch_frame(self, id):
        return self.driver.switch_to.frame(id)

    # 切回主文档
    # 切到frame中之后，便不能继续操作主文档的元素，这时如果想操作主文档内容，则需切回主文档
    def return_parent_frame(self):
        return self.driver.switch_to.default_content()

    # 定义script方法，用于执行js脚本，范围执行结果
    def script(self, src):
        self.driver.execute_script(src)


class InvalidPageException(Exception):
    '''throw this exception when you don't find the correct page'''
    pass
