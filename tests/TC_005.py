import unittest
import time

from selenium import webdriver

from pages.pages import DisplayItems


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'D:\New folder\Selinium CromeDriver\chromedriver.exe')

    def test_manualy_search(self):
        driver = self.driver
        driver.get('https://web.whatsapp.com/')
        time.sleep(15)
        print('successfully login Manualy')
        menu_bar = DisplayItems(driver)
        menu_bar.open_menu_bar()
        menu_bar.click_logout()
        print('LogOut Successfully')

    @classmethod
    def tearDown(cls):
        print('All Test Complete')


if __name__ == '__main__':
    unittest.main()