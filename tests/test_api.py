import json
import requests
import pytest
from conftest import api_key, api_username

def test_create_user(base_url):
    s = requests.Session()

    response = s.post(
        f'{base_url}/index.php?route=api/login',
        data={'username': api_username, 'key': api_key}
    )

    assert response.status_code == 200
    assert 'api_token' in response.json()
    assert 'Success: API session successfully started!' in response.json()['success']


@pytest.mark.parametrize('currency', ['USD', 'EUR', 'GBP'])
def test_create_user2(base_url, currency):
    s = requests.Session()

    api_token = json.loads(s.post(
        f'{base_url}/index.php?route=api/login',
        data={'username': api_username, 'key': api_key}
    ).text)['api_token']

    response = s.post(
        f'{base_url}/index.php?route=api/currency',
        params={'api_token': api_token},
        data={'currency': currency}
    )

    assert response.status_code == 200
    assert response.json()['success'] == 'Success: Your currency has been changed!'







