import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser: webdriver.Chrome, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def move(self, url):
        self.browser.get(url)

    def click_button(self, how, what):
        button = self.browser.find_element(how, what)
        button.click()

    def get_data_element(self, how, what, param):
        data_elem = self.browser.find_element(how, what)
        data = data_elem.get_attribute(param)
        return data

    def filling_input(self, how, what, text):
        inp = self.browser.find_element(how, what)
        inp.send_keys(text)

    def delete_all_fav(self, how, what):
        delete_list = self.browser.find_elements(how, what)
        for elem in delete_list:
            elem.click()
            time.sleep(1)