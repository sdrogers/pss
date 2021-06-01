import pytest
from mock import patch
from pss_app import create_app
from pss_app import pss_players


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    rv = client.get('/')
    assert b"Hello" in rv.data


# Utility method to check that the initiak
# cookies are correct
#
# skip allows some expected cookie elements
# to be skipped
def check_initial_cookies(cookie_jar, skip=[]):
    cookies = set()
    for cookie in cookie_jar:
        cookies.add((cookie.name, cookie.value))

    expected_cookies = [('name', 'simon'),
                        ('ai_total', '0'),
                        ('user_total', '0'),
                        ('history', '"[]"')]

    for expected_cookie in expected_cookies:
        if expected_cookie[0] in skip:
            continue
        assert expected_cookie in cookies


def test_initial_cookies(client):
    _ = client.post('/addname', data=dict(name='simon'))
    check_initial_cookies(client.cookie_jar)


def test_reset_cookies(client):
    _ = client.get('/reset_scores')
    # skip the name because it is not set in this view
    check_initial_cookies(client.cookie_jar, skip=['name'])


def get_cookie_dict(client):
    cookies = {}
    for cookie in client.cookie_jar:
        cookies[cookie.name] = cookie.value    
    return cookies

# Test that a game of multiple rounds happens correctly
@patch('pss_app.game.pick_move')
def test_round(pick_move_random_mock, client):

    # moves the user will make    
    user_moves = ['1','2','0','1']
    # moves the ai will make (note ints)
    ai_moves = [1, 1, 1, 2]
    expected_user_scores = ['0','1','1','1']
    expected_ai_scores = ['0','0','1','2']

    expected_cookies = {'ai_total': '0', 'user_total': '0'}
    for i, user_move in enumerate(user_moves):
        # mock the ai method to return the correct value
        pick_move_random_mock.return_value = ai_moves[i]
        _ = client.post('/submit_move', data=dict(move=user_move))
        expected_cookies['ai_total'] = expected_ai_scores[i]
        expected_cookies['user_total'] = expected_user_scores[i] 
        cookies = get_cookie_dict(client)
        for k,v in expected_cookies.items():
            assert cookies[k] == v
