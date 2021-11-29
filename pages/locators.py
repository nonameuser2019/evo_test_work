from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_URL = 'https://prom.ua/'
    favorites_btn = (By.CSS_SELECTOR, 'button[data-qaid="favorite_cabinet_button"]')


class BasePageLocators:
    sign_in_link = (By.CSS_SELECTOR, 'button[data-qaid="sign-in"]')


class SignInLocators:
    sign_in_by_email = (By.CSS_SELECTOR, 'div[data-qaid="email_btn"]>a')
    email_input = (By.CSS_SELECTOR, 'input[data-qaid="input_field"]')
    sign_form_next_btn = (By.CSS_SELECTOR, 'button[data-qaid="submit_btn"]')
    pass_input = (By.CSS_SELECTOR, 'input[data-qaid="password"]')
    sabmit_btn = (By.CSS_SELECTOR, 'button[data-qaid="submit_btn"]')


class CatalogLocators:
    favorits_btn = (By.CSS_SELECTOR, 'span[data-qaid="add_favorite"]')


class FavoritePageLocators:
    delete_btn = (By.CSS_SELECTOR, 'span[data-qaid="delete_icon"]')