import unittest
import time
from selenium import webdriver

from pages.pages import DisplayItems


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=r'D:\New folder\Selinium CromeDriver\chromedriver.exe')

    def test_search_and_send_message(self):
        driver = self.driver
        driver.get('https://web.whatsapp.com/')
        time.sleep(15)
        try:
            print('successfully login Manualy')
            search_box = DisplayItems(driver)
            search_box.click_search_item_for_chat('oli')
            search_box.sent_write_message('This Message Sent By Chat Bot')
            time.sleep(5)
            search_box.verify_message_sent()

        except:
            print('Error')

    @classmethod
    def tearDown(cls):
        print('Test_003 Complete')
