from selenium import webdriver
from selenium.common.exceptions import *
import pytest
from pages.locators import *
from pages.base_page import BasePage
from pages.product_card_page import ProductCardPage
import time
from utils.support import *


BIKES_TIRES_ULR = 'https://prom.ua/Velosipednye-shiny'
PRODUCT_CARD_URL = 'https://prom.ua/p608430629-pokrishka-schwalbe-thunder.html?'


# all tests in catalog page
@pytest.mark.smoke
def test_check_possibility_to_add_to_fav_from_catalog(browser, log_in_delete_all_favorites):
    page = BasePage(browser, BIKES_TIRES_ULR)
    page.open()
    page.add_to_fav(*CatalogLocators.favorits_btn)
    data = page.get_data_element(*CatalogLocators.favorits_btn, 'data-tg-clicked')
    assert data == 'on', "Pictogram doesn't change style"


@pytest.mark.smoke
def test_check_favorites_count_before_added_from_catalog(browser, log_in_delete_all_favorites):
    page = BasePage(browser, BIKES_TIRES_ULR)
    page.open()
    page.add_to_fav(*CatalogLocators.favorits_btn)
    fav_count = page.get_favorites_count(*CatalogLocators.favorites_count)
    assert fav_count == 1, f'Wrong favorites count. Expected result: 1. Actual result: {fav_count}'


def test_check_pict_color_after_reload_page(browser, log_in_delete_all_favorites):
    page = BasePage(browser, BIKES_TIRES_ULR)
    page.open()
    page.add_to_fav(*CatalogLocators.favorits_btn)
    page.reload_page()
    data = page.get_data_element(*CatalogLocators.favorits_btn, 'data-tg-clicked')
    assert data == 'off', "Pictogram doesn't change style"


def test_check_pict_color_in_product_card(browser, log_in_delete_all_favorites):
    page = BasePage(browser, BIKES_TIRES_ULR)
    page.open()
    page.add_to_fav(*CatalogLocators.favorits_btn)
    page.go_to_product_page(*CatalogLocators.product_link)
    data = page.get_data_element(*CatalogLocators.favorits_btn, 'data-tg-clicked')
    assert data == 'off', "Pictogram doesn't change style"


def test_check_pict_before_go_back_from_card(browser, log_in_delete_all_favorites):
    page = BasePage(browser, BIKES_TIRES_ULR)
    page.open()
    page.add_to_fav(*CatalogLocators.favorits_btn)
    page.go_to_product_page(*CatalogLocators.product_link)
    page.go_back()
    data = page.get_data_element(*CatalogLocators.favorits_btn, 'data-tg-clicked')
    assert data == 'off', "Pictogram doesn't change style"


def test_check_fav_count_in_prod_card(browser, log_in_delete_all_favorites):
    page = BasePage(browser, BIKES_TIRES_ULR)
    page.open()
    page.add_to_fav(*CatalogLocators.favorits_btn)
    page.go_to_product_page(*CatalogLocators.product_link)
    try:
        fav_count = page.get_favorites_count(*CatalogLocators.favorites_count)
        assert fav_count == 1, f'Wrong favorites count. Expected result: 1. Actual result: {fav_count}'
    except NoSuchElementException:
        raise AssertionError('Page does not have favorites count')


def test_comparing_product_name_in_favorites_page(browser, log_in_delete_all_favorites):
    page = BasePage(browser, BIKES_TIRES_ULR)
    page.open()
    page.click_button(*CatalogLocators.favorits_btn)
    product_tile = page.get_text_from_param(*CatalogLocators.product_title, 'title')
    page.click_button(*CatalogLocators.fav_cabinet_btn)
    product_tile_fav = page.get_text_element(*FavoritePageLocators.product_tile)
    assert product_tile_fav == product_tile, 'Wrong product title in favorites page'


def test_check_fav_count_in_fav_pages(browser, log_in_delete_all_favorites):
    page = BasePage(browser, BIKES_TIRES_ULR)
    page.open()
    page.add_to_fav(*CatalogLocators.favorits_btn)
    page.go_to_faforites()
    fav_count = page.get_favorites_count(*FavoritePageLocators.favorites_count)
    assert fav_count == 1, f'Wrong favorites count. Expected result: 1. Actual result: {fav_count}'


def test_check_pict_after_del_from_fav_page(browser, log_in_delete_all_favorites):
    page = BasePage(browser, BIKES_TIRES_ULR)
    page.open()
    page.add_to_fav(*CatalogLocators.favorits_btn)
    page.go_to_faforites()
    page.delete_all_fav(*FavoritePageLocators.delete_btn)
    count = page.is_not_element_present(*FavoritePageLocators.favorites_count)
    assert count is False, 'Favorites count error, element is present before deleted'


# all tests for product card page
@pytest.mark.smoke
def test_check_pict_style_before_added(browser, log_in_delete_all_favorites):
    page = ProductCardPage(browser, PRODUCT_CARD_URL)
    page.open()
    page.add_to_fav(*ProductPageLocators.favorits_btn)
    data = page.get_data_element(*ProductPageLocators.favorits_btn, 'data-tg-clicked')
    assert data == 'off', "Pictogram doesn't change style"


@pytest.mark.smoke
def test_check_fav_count_before_added(browser, log_in_delete_all_favorites):
    page = ProductCardPage(browser, PRODUCT_CARD_URL)
    page.open()
    page.add_to_fav(*ProductPageLocators.favorits_btn)
    count = page.get_favorites_count(*ProductPageLocators.favorites_count)
    assert count == 1, f'Wrong favorites count. Expected result: 1. Actual result: {count}'


def test_check_fav_count_before_deleted(browser, log_in_delete_all_favorites):
    page = ProductCardPage(browser, PRODUCT_CARD_URL)
    page.open()
    page.add_to_fav(*ProductPageLocators.favorits_btn)
    page.dell_from_fav(*ProductPageLocators.favorits_btn)
    count = page.is_not_element_present(*ProductPageLocators.favorites_count)
    assert count is False, 'Favorites count error, element is present before deleted'


@pytest.mark.test
@pytest.mark.parametrize('url, result', product_card_url_list)
def test_check_pict_style_before_deleted(browser, log_in_delete_all_favorites, url, result):
    page = ProductCardPage(browser, url)
    page.open()
    page.add_to_fav(*ProductPageLocators.favorits_btn)
    page.dell_from_fav(*ProductPageLocators.favorits_btn)
    data = page.get_data_element(*ProductPageLocators.favorits_btn, 'data-tg-clicked')
    time.sleep(2)
    assert data == result, "Pictogram doesn't change style"
