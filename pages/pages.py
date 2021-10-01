from selenium.webdriver.common.keys import Keys


class DisplayItems():

    def __init__(self, driver):
        self.driver = driver
        self.search_bar = '//*[@id="side"]/div[1]/div/label/div/div[2]'
        self.msg_bar = '//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]'
        self.msg_status = '//*[@id="main"]/footer/div[1]/div[3]/button/span'
        self.menu_bar = '//*[@id="side"]/header/div[2]/div/span/div[3]/div'
        self.logout = '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div[1]/ul/li[5]/div[1]'

    def enter_search_keyword(self, keyword):
        self.driver.find_element_by_xpath(self.search_bar).clear()
        self.driver.find_element_by_xpath(self.search_bar).send_keys(keyword)

    def click_search_item_for_chat(self, keyword):
        self.driver.find_element_by_xpath(self.search_bar).clear()
        search_box = self.driver.find_element_by_xpath(self.search_bar)
        search_box.send_keys(keyword)
        search_box.send_keys(Keys.ENTER)

    def sent_write_message(self, msg):
        msg_box = self.driver.find_element_by_xpath(self.msg_bar)
        msg_box.send_keys(msg)
        msg_box.send_keys(Keys.ENTER)

    def verify_message_sent(self):
        message = self.driver.find_element_by_xpath(self.msg_status)
        message.click()

    def open_menu_bar(self):
        menu = self.driver.find_element_by_xpath(self.menu_bar)
        menu.send_keys(Keys.ENTER)

    def click_logout(self):
        logout_select = self.driver.find_element_by_xpath(self.logout)
        logout_select.click()
