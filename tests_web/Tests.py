__author__ = 'Ilham TM'
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from tests_web.Pages import SignInPage, FilterPage, ToCheckoutPage, CheckoutInformation, CheckoutOverview
from tests_web.Locators import Constants


class EnvironmentSetup(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=Constants.driver)
        self.driver.get(Constants.baseURL)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, timeout=30)
        self.action = webdriver.ActionChains(self.driver)
        self.SignInPage = SignInPage(self.driver)
        self.FilterPage = FilterPage(self.driver)
        self.ToCheckoutPage = ToCheckoutPage(self.driver)
        self.CheckoutInformation = CheckoutInformation(self.driver)
        self.CheckoutOverview = CheckoutOverview(self.driver)

    @classmethod
    def tearDown(self):
        self.driver.quit()

    def test_tokopedia(self):
        self.SignInPage.input_username("standard_user")
        self.SignInPage.input_password("secret_sauce")
        self.SignInPage.click_signin_button()
        self.FilterPage.filter_product()
        self.FilterPage.validate_high_price_select("Sauce Labs Fleece Jacket", "$49.99")
        self.ToCheckoutPage.click_add_to_cart_button()
        self.ToCheckoutPage.click_cart()
        self.ToCheckoutPage.verify_product_in_cart("Sauce Labs Fleece Jacket", "$49.99")
        self.ToCheckoutPage.click_checkout_button()
        self.CheckoutInformation.input_first_name("Ilham")
        self.CheckoutInformation.input_last_name("Tri Mulyawan")
        self.CheckoutInformation.input_postal_code("16610")
        self.CheckoutInformation.click_submit_information()
        self.CheckoutOverview.verify_detail_product_matched("Sauce Labs Fleece Jacket")
        self.CheckoutOverview.click_finish()
        self.CheckoutOverview.checkout_success()

if __name__ == '__main__':
    unittest.main()



