import json
from selenium import webdriver
from selenium.webdriver.support.abstract_event_listener import AbstractEventListener
from selenium.webdriver.support.ui import WebDriverWait
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

    def is_not_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
            element = WebDriverWait(self.browser, 3).until_not(EC.presence_of_element_located((how, what)))
            return element
        finally:
            return False

    def click_button(self, how, what):
        button = self.browser.find_element(how, what)
        button.click()

    def get_data_element(self, how, what, param):
        data_elem = self.browser.find_element(how, what)
        data = json.loads(data_elem.get_attribute(param))
        return data[0]['args'][2]['label/label']

    def get_text_from_param(self, how, what, param):
        data_elem = self.browser.find_element(how, what)
        data = data_elem.get_attribute(param)
        return data

    def get_text_element(self, how, what):
        data = self.browser.find_element(how, what)
        return data.text

    def get_current_url(self):
        url = self.browser.current_url
        return url

    def filling_input(self, how, what, text):
        inp = self.browser.find_element(how, what)
        inp.send_keys(text)

    def delete_all_fav(self, how, what):
        delete_list = self.browser.find_elements(how, what)
        for elem in delete_list:
            elem.click()

    def get_favorites_count(self, how, what):
        count = self.browser.find_element(how, what)
        return int(count.text)

    def reload_page(self):
        self.browser.refresh()

    def go_back(self):
        self.browser.back()

    def go_to_faforites(self):
        self.browser.get('https://my.prom.ua/cabinet/user/favorites')
