import json
import pytest
import requests
from API_tests_data import *
from conftest import get_data
from random import randint, choice


def test_creatе_api_session(api_session, base_url):
    response = api_session.post(
        f'{base_url}/index.php?route=api/login',
        data={'username': api_username, 'key': api_key}
    )
    assert response.status_code == 200
    assert 'api_token' in response.json()
    assert 'Success: API session successfully started!' in response.json()['success']


@pytest.mark.parametrize('currency', CURRENCY_LIST)
def test_currency_change(api_session, api_token, base_url, currency):
    response = api_session.post(
        f'{base_url}/index.php?route=api/currency',
        params={'api_token': api_token},
        data={'currency': currency}
    )
    assert response.status_code == 200
    assert response.json()['success'] == 'Success: Your currency has been changed!'


@pytest.mark.parametrize('product_id, quantity', PRODUCT_ID_AND_QUANTITY_LIST)
def test_add_product_in_cart(api_session, api_token, base_url, product_id, quantity):
    response = api_session.post(
        f'{base_url}/index.php?route=api/cart/add',
        params={'api_token': api_token},
        data={
            'product_id': product_id,
            'quantity': quantity
        }
    )
    assert response.status_code == 200
    assert response.json()['success'] == 'Success: You have modified your shopping cart!'


@pytest.mark.parametrize('key, quantity', KEY_AND_QUANTITY_LIST)
def test_edit_quantity_products_in_cart(api_session, api_token,base_url, key, quantity):
    response = api_session.post(
        f'{base_url}/index.php?route=api/cart/edit',
        params={'api_token': api_token},
        data={
            'key': key,
            'quantity': quantity
        }
    )
    assert response.status_code == 200
    assert response.json()['success'] == 'Success: You have modified your shopping cart!'


@pytest.mark.parametrize('key', KEY_LIST)
def test_remove_product_from_cart(api_session, api_token,base_url, key):
    response = api_session.post(
        f'{base_url}/index.php?route=api/cart/remove',
        params={'api_token': api_token},
        data={
            'key': key
        }
    )
    assert response.status_code == 200
    assert response.json()['success'] == 'Success: You have modified your shopping cart!'


@pytest.mark.parametrize('product_id, quantity', PRODUCT_ID_AND_QUANTITY_LIST)
def test_get_product_list_from_cart(api_session, api_token,base_url, product_id, quantity):
    add_product_response = api_session.post(
                f'{base_url}/index.php?route=api/cart/add',
                params={'api_token': api_token},
                data={
                    'product_id': product_id,
                    'quantity': quantity
                }
            )
    response = api_session.post(
        f'{base_url}/index.php?route=api/cart/products',
        params={'api_token': api_token}
    )
    assert response.status_code == 200
    assert 'products' in response.json()
    assert response.json()["products"][0]["quantity"] == quantity


@pytest.mark.parametrize('coupon', COUPON_LIST)
def test_coupon_add(api_session, api_token,base_url, coupon):
    """Купоны в COUPON_LIST действительны до 01/01/2025.При необходимости
     их можно продлить или создать заново в разделе администрирования"""

    response = api_session.post(
        f'{base_url}/index.php?route=api/coupon',
        params={'api_token': api_token},
        data={
            'coupon': coupon
        }
    )
    assert response.status_code == 200
    assert response.json()['success'] == 'Success: Your coupon discount has been applied!'


def test_set_shipping_address(api_session, api_token, base_url):
    data = {
        'firstname': f'{get_data("firstname")}',
        'lastname': f'{get_data("lastname")}',
        'address_1': f'{get_data("address")}',
        'city': f'{get_data("city")}',
        'country_id': f'{get_data("country_id")}',
        'zone_id': f'{get_data("zone_id")}'
    }
    response = api_session.post(
        f'{base_url}/index.php?route=api/payment/address',
         params={'api_token': api_token},
         data = data
    )
    assert response.status_code == 200
    assert response.json().get('success') == 'Success: Payment address has been set!'


