import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from tests_web.Locators import  SignInElements, FilterProducts, ToCheckout, CheckoutInformations, CheckoutOverviews

class BasePage(object):
    def __init__(self, driver):
        self.driver=driver

    def scroll_to(self, by_locator):
        ActionChains(self.driver).move_to_element(self.driver.find_element_by_id(by_locator)).perform()

    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def assert_element_text(self, by_locator, element_text):
        web_element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    def assert_element(self, by_locator1, by_locator2):
        web_element_1 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator1))
        web_element_2 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator2))
        assert web_element_1.text == web_element_2.text

    def enter_text(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def is_present(self, by_locator):
        elements = self.driver.find_elements(*by_locator)
        assert len(elements) != 0

class FilterPage(BasePage):
    def filter_product(self):
        self.click(FilterProducts.FILTER_ICON)
        self.click(FilterProducts.OPTION_FILTER_HILO)

    def validate_high_price_select(self, nameproduct, priceproduct):
        time.sleep(3)
        nameproduct_value = FilterProducts.ASSERT_FILTER_NAME
        priceproduct_value = FilterProducts.ASSERT_FILTER_PRICE
        self.assert_element_text(FilterProducts.ASSERT_FILTER_NAME, nameproduct)
        self.assert_element_text(FilterProducts.ASSERT_FILTER_PRICE, priceproduct)

class SignInPage(BasePage):
    def assert_signin_form(self):
        self.assert_element_text(SignInElements.ASSERT_SIGNIN_FORM, "Silakan masuk ke dalam akun kamu")

    def input_username(self, username):
        self.enter_text(SignInElements.FIELD_USERNAME, username)

    def input_password(self, password):
        self.enter_text(SignInElements.FIELD_PASSWORD, password)

    def click_signin_button(self):
        self.click(SignInElements.SIGNIN_BUTTON)
        time.sleep(3)
        elements = self.driver.find_elements(*SignInElements.ASSERT_SIGNIN)
        if len(elements) != 0:
            pass

    def login_user(self, username, password):
        self.SignInPage = SignInPage(self.driver)
        self.SignInPage.input_username(username)
        self.SignInPage.input_password(password)
        self.SignInPage.click_signin_button()

class ToCheckoutPage(BasePage):
    def click_add_to_cart_button(self):
        self.click(ToCheckout.ADD_TO_CART)
        time.sleep(3)

    def click_cart(self):
        self.click(ToCheckout.CART_ICON)
        time.sleep(3)

    def verify_product_in_cart(self, name_product, price_product):
        self.assert_element_text(ToCheckout.NAME_PRODUCT, name_product)
        self.assert_element_text(ToCheckout.PRICE_PRODUCT, price_product)

    def click_checkout_button(self):
        self.click(ToCheckout.CHECKOUT_BUTTON)

class CheckoutInformation(BasePage):
    def input_first_name(self, first_name):
        time.sleep(3)
        self.enter_text(CheckoutInformations.FIELD_FIRST_NAME, first_name)

    def input_last_name(self, last_name):
        self.enter_text(CheckoutInformations.FIELD_LAST_NAME, last_name)

    def input_postal_code(self, postal_code):
        self.enter_text(CheckoutInformations.FIELD_POSTAL_CODE, postal_code)

    def click_submit_information(self):
        self.click(CheckoutInformations.SUBMIT_BUTTON)

class CheckoutOverview(BasePage):
    def verify_detail_product_matched(self, name_product):
        time.sleep(3)
        self.assert_element_text(CheckoutOverviews.NAME_PRODUCT_CO, name_product)

    def click_finish(self):
        self.scroll_to("finish")
        self.click(CheckoutOverviews.FINISH_BUTTON)

    def checkout_success(self):
        time.sleep(3)
        self.is_present(CheckoutOverviews.CHECKOUT_COMPLETE_CHECK)
