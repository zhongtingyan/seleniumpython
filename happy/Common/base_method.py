import unittest
from selenium import webdriver
from configuration import URL


class BaseTestCase(unittest.TestCase):
    """docstring for BaseTestCase"""

    def setUp(self):
        # create a new Firefox session
        # profile_dir = r'C:\Users\czhou012\AppData\Roaming\Mozilla\Firefox\Profiles\iewanxoz.default'
        # profile = webdriver.FirefoxProfile(profile_dir)
        # self.driver = webdriver.Firefox(profile)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get(URL.url)

    def tearDown(self):
        # close the browser window
        self.driver.quit()

    '''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        cls.driver.get(URL.url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    '''
