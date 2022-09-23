import pytest
import re
from subprocess import Popen, PIPE
import signal
from time import sleep
import requests
import json


# Use this fixture to get the URL of the server.
@pytest.fixture
def url():
    url_re = re.compile(r' \* Running on ([^ ]*)')
    server = Popen(["python3", "simple.py"], stderr=PIPE, stdout=PIPE)
    line = server.stderr.readline()
    local_url = url_re.match(line.decode())
    if local_url:
        yield local_url.group(1)
        # Terminate the server
        server.send_signal(signal.SIGINT)
        waited = 0
        while server.poll() is None and waited < 5:
            sleep(0.1)
            waited += 0.1
        if server.poll() is None:
            server.kill()
    else:
        server.kill()
        raise Exception("Couldn't get URL from local server")

def test_url(url):
    '''
    A simple sanity test to check that your server is set up properly
    '''
    assert url.startswith("http")

def test_empty(url):
#Enter empty and get an empty list
    requests.post(f'{url}/name/add')
    empty = requests.get(f'{url}/names')
    assert empty.json() == []

def test_simple(url):
#Enter something and get the list
    requests.post(f'{url}/name/add?name=a')
    requests.post(f'{url}/name/add?name=b')
    requests.post(f'{url}/name/add?name=c')
    l = requests.get(f'{url}/names')
    assert l.json() == ['a', 'b', 'c']

def test_delete(url):
#Delete a name 
    requests.post(f'{url}/name/add?name=a')
    requests.post(f'{url}/name/add?name=b')
    requests.post(f'{url}/name/add?name=c')
    requests.delete(f'{url}/name/remove?name=b')
    l = requests.get(f'{url}/names')
    assert l.json() == ['a', 'c']
