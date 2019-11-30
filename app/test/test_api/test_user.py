import json
import pytest
from app import cache


test_users = [
        {"id": 1, "username": "Son", "email": "n.vanson@gmail.com", "password": "1234567aA"},
        {"id": 2, "username": "Hoan", "email": "n.vanhoan@gmail.com", "password": "1234567bB"},
        {"id": 3, "username": "Lam", "email": "tunglammeta@gmail.com", "password": "1234567cC"},
        {"id": 4, "username": "Hung", "email": "n.vanhung@gmail.com", "password": "1234567dD"},
        {"id": 5, "username": "Nam", "email": "n.huynam@gmail.com", "password": "1234567eE"},
        {"id": 6, "username": "Viet", "email": "n.vanviet@gmail.com", "password": "1234567fF"}
]


def test_get(app):
    response = app.test_client().get('/api/user')
    assert response.status_code == 200
    response_body = response.get_json()
    for i in range(6):
        assert response_body['users'][i]["username"] == test_users[i]["username"]
        assert response_body['users'][i]["email"] == test_users[i]["email"]


def test_get_id(app):
    for i in range(6):
        response = app.test_client().get('/api/user/{}'.format(i+1))
        assert response.status_code == 200
        response_body = response.get_json()
        cache_key = response_body['user']['id']
        data_in_cache = cache.get(str(cache_key))
        assert str(data_in_cache) == '<User %r>' % test_users[i]["username"]
        assert response_body['user']["username"] == test_users[i]["username"]
        assert response_body['user']["email"] == test_users[i]["email"]


def test_get_id_false(app):
    response = app.test_client().get('/api/user/9')
    assert response.status_code == 400
    response_body = response.get_json()
    assert response_body['code'] == 400
    assert response_body['description'] == "None exist user"
    assert response_body['name'] == "Bad Request"


def test_post(app):
    data_sended = {"name": "zafwfawfzzz", "email": "n.zzfawfawefz.2209@gmail.com", "password": "1234567gG"}
    response = app.test_client().post('/api/user',
                                      data=json.dumps(data_sended),
                                      content_type='application/json',)

    assert response.status_code == 200
    response_body = response.get_json()
    assert response_body['added_user']['username'] == data_sended['name']
    assert response_body['added_user']['email'] == data_sended['email']


data_sended = [
    "hello",
    {"gg": "zafwfawfzzz", "email": "n.zzfawfawefz.2209@gmail.com", "password": "1234567hH"},
    {"name": "zafwfawfzzz", "xx": "n.zzfawfawefz.2209@gmail.com", "password": "1234567jJ"},
    {"name": "zafwfawfzzz", "email": "n.zzfawfawefz.2209gmail.com", "password": "1234567jJ"},
    {"name": "zafwfawfzzz", "email": "n.zzfawfawefz.2209@gmail.com", "password": "1"},
    {"name": "Viet", "email": "n.vanviet@gmail.com", "password": "1234567fF"}
]

content_type = [
    "text/html",
    "application/json",
    "application/json",
    "application/json",
    "application/json",
    "application/json"
]

expected = [
    {
        "code": 400,
        "description": "Invalid: content type is not json!",
        "name": "Bad Request"
    },
    {
        "code": 400,
        "description": {
            "gg": [
                "unknown field"
            ],
            "name": [
                "required field"
            ]
        },
        "name": "Bad Request"
    },
    {
        "code": 400,
        "description": {
            "xx": [
                "unknown field"
            ],
            "email": [
                "required field"
            ]
        },
        "name": "Bad Request"
    },
    {
        "code": 400,
        "description": {
            "email": [
                "Invalid email"
            ]
        },
        "name": "Bad Request"
    },
    {
        "code": 400,
        "description": {
            "password": [
                "Password must contain at least 8 characters, one uppercase and one lowercase letter"
            ]
        },
        "name": "Bad Request"
    },
    {
        "code": 400,
        "description": "Invalid: the username or email already exist!",
        "name": "Bad Request"
    }
]


@pytest.mark.parametrize("data_sended, content_type, expected",
                         [
                             (data_sended[0], content_type[0], expected[0]),
                             (data_sended[1], content_type[1], expected[1]),
                             (data_sended[2], content_type[2], expected[2]),
                             (data_sended[3], content_type[3], expected[3]),
                             (data_sended[4], content_type[4], expected[4]),
                             (data_sended[5], content_type[5], expected[5])
                         ],
                         )
def test_post_fail(app, data_sended, content_type, expected):
    response = app.test_client().post('/api/user',
                                      data=json.dumps(data_sended),
                                      content_type=content_type,)
    assert response.status_code == 400
    response_body = response.get_json()
    assert response_body == expected


def test_patch(app):
    data_sended = {"name": "Hiep", "email": "n.vanhiep@gmail.com", "password": "axcdafwbA1"}
    response = app.test_client().patch('/api/user/5',
                                       data=json.dumps(data_sended),
                                       content_type='application/json',)

    assert response.status_code == 200
    response_body = response.get_json()
    assert response_body['updated_user']['username'] == data_sended['name']
    assert response_body['updated_user']['email'] == data_sended['email']
    cache_key = response_body['updated_user']['id']
    data_in_cache = cache.get(str(cache_key))
    assert str(data_in_cache) == '<User %r>' % data_sended['name']


@pytest.mark.parametrize("data_sended, content_type, expected",
                         [
                             (data_sended[0], content_type[0], expected[0]),
                             (data_sended[1], content_type[1], expected[1]),
                             (data_sended[2], content_type[2], expected[2]),
                             (data_sended[3], content_type[3], expected[3]),
                             (data_sended[4], content_type[4], expected[4]),
                             (data_sended[5], content_type[5], expected[5])
                         ],
                         )
def test_patch_fail1(app, data_sended, content_type, expected):
    response = app.test_client().patch('/api/user/1',
                                       data=json.dumps(data_sended),
                                       content_type=content_type,)
    assert response.status_code == 400
    response_body = response.get_json()
    assert response_body == expected


def test_patch_fail2(app):
    data_sended = {"name": "Hiep", "email": "n.vanhiep@gmail.com", "password": "axcdafwbA1"}
    response = app.test_client().patch('/api/user/9',
                                       data=json.dumps(data_sended),
                                       content_type='application/json',)
    assert response.status_code == 400
    response_body = response.get_json()
    assert response_body['code'] == 400
    assert response_body['description'] == "None exist user"
    assert response_body['name'] == "Bad Request"


def test_delete(app):
    response = app.test_client().delete('/api/user/2')

    assert response.status_code == 200
    response_body = response.get_json()
    cache_key = response_body['deleted_user']['id']
    data_in_cache = cache.get(str(cache_key))
    assert data_in_cache is None
    assert response_body['deleted_user']['username'] == "Hoan"
    assert response_body['deleted_user']['email'] == "n.vanhoan@gmail.com"


def test_delete_fail(app):
    response = app.test_client().delete('/api/user/12')

    assert response.status_code == 400
    response_body = response.get_json()
    assert response_body['code'] == 400
    assert response_body['description'] == "None exist user"
    assert response_body['name'] == "Bad Request"


def test_delete_all(app):
    response = app.test_client().delete('/api/user')

    assert response.status_code == 200
    response_body = response.get_json()
    assert response_body['deleted_users_id'] == [u['id'] for u in test_users]
