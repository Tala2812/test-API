import pytest
from unittest.mock import Mock
import requests
from main import get_random_cat_image

def test_successful_request(mocker):

    mock_get = mocker.patch('requests.get')

    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{'url': 'https://example.com/cat.jpg'}]

    url = get_random_cat_image()
    assert url == 'https://example.com/cat.jpg'

def test_unsuccessful_request(mocker):
    # Создаем mock для requests.get
    mock_get = mocker.patch('requests.get')

    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = []


    url = get_random_cat_image()
    assert url is None