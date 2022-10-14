import pytest
import requests
from hw6.data.ya_example import YaDisc

token = 'token'


@pytest.fixture()
def teardown():
    yield
    url = YaDisc(token).url
    headers = YaDisc(token).headers
    params = {
        'path': 'my_folder',
        'disable_redirects': 'true'
    }
    requests.delete(url, params=params, headers=headers)


def test_create_folder(teardown):
    response = YaDisc(token).create_folder('my_folder')
    assert response.status_code == [200]
    return response

