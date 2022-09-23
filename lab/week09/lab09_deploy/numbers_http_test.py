import pytest
import requests
import json

URL = 'http://127.0.0.1:8000/'

def test_rtiply_by_two():
    r = requests.get(URL + 'multiply', json={
        'number': 4,
    })
    assert r.status_code == 200

def test_print_message():
    r = requests.get(URL + 'print', json={
        'message': 'Today is Thursday.'
    })
    assert r.status_code == 200

def test_sum_list_of_numbers():
    r = requests.get(URL + 'sum/list', json={
        'number': [1, 3, 5, 20],
    })
    assert r.status_code == 200

def test_sum_iterable_of_numbers():
    r = requests.get(URL + 'sum/iterable', json={
        'number': [100, 5, 4, 32],
    })
    assert r.status_code == 200
def test_is_in():
    r = requests.get(URL + 'is/in', json={
        'needle': 4,
        'haystack': [1, 6, 4, 7]
    })
    assert r.status_code == 200
    
    r = requests.get(URL + 'is/in', json={
        'needle': 7,
        'haystack': [1, 6, 4, 8]
    })
    assert r.status_code == 200

def test_index_of_number():
    r = requests.get(URL + 'index', json={
        'item': 4,
        'numbers': [1, 6, 4, 7]
    })
    assert r.status_code == 200
