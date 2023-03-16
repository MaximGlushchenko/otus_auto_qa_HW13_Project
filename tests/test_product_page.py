import allure
import pytest
from locators import *
from page_objects.ProductPage import ProductPage
from UI_tests_data import USD_to_EUR_ratio, USD_to_GBP_ratio


@pytest.mark.UI
@pytest.mark.smoke
@allure.feature('UI tests')
@allure.story('Product page')
@allure.title('Check product page elements')
def test_check_product_page_elements(browser, base_url):
    product_page = ProductPage(browser)
    product_page.open(base_url)

    product_page.element(PP_BUTTON_CART)
    product_page.element(PP_INPUT_QUANTITY)
    product_page.element(PP_TWEET_LINK_TEXT)
    product_page.element(PP_ADD_TO_WISH_LIST)
    product_page.element(PP_COMPARE_THIS_PRODUCT)

@pytest.mark.UI
@pytest.mark.regress
@allure.feature('UI tests')
@allure.story('Product page')
@allure.title('Switch_currency')
def test_switch_currency(browser, base_url):
    product_page = ProductPage(browser)
    product_page.open(base_url)

    USD_price = product_page.get_product_price("USD")

    with allure.step('Check dropdown switch to USD'):
        try:
            assert product_page.element(MP_DROPDOWN_SWITCH_CURRENCY).text == "$ Currency "
        except:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise

    EUR_price = product_page.get_product_price("EUR")

    with allure.step('Check dropdown switch to EUR'):
        try:
            assert product_page.element(MP_DROPDOWN_SWITCH_CURRENCY).text == "€ Currency "
        except:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise

    with allure.step('Check transfer of USD to EUR'):
        try:
            assert EUR_price == round((USD_price * USD_to_EUR_ratio), 2)
        except:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise

    GBP_price = product_page.get_product_price("GBP")

    with allure.step('Check dropdown switch to GBP'):
        try:
            assert product_page.element(MP_DROPDOWN_SWITCH_CURRENCY).text == "£ Currency "
        except:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise

    with allure.step('Check transfer of USD to GBP'):
        try:
            assert GBP_price == round((USD_price * USD_to_GBP_ratio), 2)
        except:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise
