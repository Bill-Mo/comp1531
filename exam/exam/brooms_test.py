'''
Tests
'''
from brooms import send_message, get_messages, clear, get_users, add_user
import pytest

def test_simple():
    clear()
    add_user("Hayden")
    assert(get_users() == {"users":["Hayden"]})
    add_user("Rob")
    assert(get_users() == {"users":["Rob", "Hayden"]})
    send_message("Hayden", "Rob", "Hello!")
    send_message("Hayden", "Rob", "Goodbye!")
    assert get_messages() == {
        "messages": [
            {"from": "Hayden", "to": "Rob", "message": "Hello!"},
            {"from": "Hayden", "to": "Rob", "message": "Goodbye!"},
        ]
    }

def test_error():
    clear()
    add_user("Hayden")
    with pytest.raises(KeyError):
        add_user("Hayden")
    with pytest.raises(KeyError):
        send_message('Hayden', 'Rob', 'abc')
    with pytest.raises(KeyError):
        send_message('Rob', 'Hayden', 'abc')
