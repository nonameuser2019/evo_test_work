from selenium import webdriver
import pytest
from pages.locators import *
from pages.base_page import BasePage
import time
import json


BIKES_TIRES_ULR = 'https://prom.ua/Velosipednye-shiny'



def test_check_possibility_to_add_to_fav_from_catalog(browser, log_in_delete_all_favorites):
    page = BasePage(browser, BIKES_TIRES_ULR)
    page.open()
    page.click_button(*CatalogLocators.favorits_btn)
    data = json.loads(page.get_data_element(*CatalogLocators.favorits_btn, 'data-tg-clicked'))
    assert data[0]['args'][2]['label/label'] == 'off', "Did't marked favorit's piktogram"
