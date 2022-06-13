from selenium.webdriver.common.by import By


# constans
class Constants():
    driver = r"/Users/bukalapak/Documents/PerTestan/reps/ToBL/bl-pretest-master/chromedriver"
    baseURL = "https://www.saucedemo.com/"


# locators
class SignInElements():
    FIELD_USERNAME = (By.ID, "user-name")
    FIELD_PASSWORD = (By.ID, "password")
    SIGNIN_BUTTON = (By.ID, "login-button")
    ASSERT_SIGNIN = (By.CSS_SELECTOR, ".tittle")

class FilterProducts():
    FILTER_ICON = (By.CSS_SELECTOR, ".product_sort_container")
    OPTION_FILTER_HILO = (By.XPATH, "//option[@value='hilo']")
    ASSERT_FILTER_NAME = (By.XPATH, "//*[@class='inventory_item'][1]/descendant::*[contains(@class,'inventory_item_name')]")
    ASSERT_FILTER_PRICE = (By.XPATH, "//*[@class='inventory_item'][1]/descendant::*[contains(@class,'inventory_item_price')]")

class ToCheckout():
    ADD_TO_CART = (By.XPATH, "//*[@class='inventory_item'][1]/descendant::*[contains(@class,'btn_inventory')]")
    NAME_PRODUCT = (By.XPATH, "//*[@class='cart_item_label'][1]/descendant::*[contains(@class,'inventory_item_name')]")
    PRICE_PRODUCT = (By.XPATH, "//*[@class='cart_item_label'][1]/descendant::*[contains(@class,'inventory_item_price')]")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ICON = (By.ID, "shopping_cart_container")

class CheckoutInformations():
    FIELD_FIRST_NAME = (By.ID, "first-name")
    FIELD_LAST_NAME = (By.ID, "last-name")
    FIELD_POSTAL_CODE = (By.ID, "postal-code")
    SUBMIT_BUTTON = (By.ID, "continue")

class CheckoutOverviews():
    NAME_PRODUCT_CO = (By.XPATH, "//*[@class='cart_item_label'][1]/descendant::*[contains(@class,'inventory_item_name')]")
    PRICE_PRODUCT_CO = (By.XPATH, "//*[@class='cart_item_label'][1]/descendant::*[contains(@class,'inventory_item_price')]")
    FIELD_POSTAL_CODE = (By.ID, "postal-code")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, ".submit_button")
    FINISH_BUTTON = (By.ID, "finish")
    CHECKOUT_COMPLETE_CHECK = (By.ID, "back-to-products")
