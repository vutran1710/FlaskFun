import json
import pytest


test_users = [
        {"id": 1, "username": "Son", "email": "n.vanson@gmail.com"},
        {"id": 2, "username": "Hoan", "email": "n.vanhoan@gmail.com"},
        {"id": 3, "username": "Lam", "email": "n.tunglam@gmail.com"},
        {"id": 4, "username": "Hung", "email": "n.vanhung@gmail.com"},
        {"id": 5, "username": "Nam", "email": "n.huynam@gmail.com"},
        {"id": 6, "username": "Viet", "email": "n.vanviet@gmail.com"}
]


def test_get(app):
    response = app.test_client().get('/api/user')
    assert response.status_code == 200
    response_body = response.get_json()
    assert response_body['users'] == test_users


def test_get_id(app):
    for i in range(6):
        response = app.test_client().get('/api/user/{}'.format(i+1))
        assert response.status_code == 200
        response_body = response.get_json()
        assert response_body['user'] == test_users[i]


def test_get_id_false(app):
    response = app.test_client().get('/api/user/9')
    assert response.status_code == 400
    response_body = response.get_json()
    assert response_body['code'] == 400
    assert response_body['description'] == "None exist user"
    assert response_body['name'] == "Bad Request"


def test_post(app):
    data_sended = {"name": "zafwfawfzzz", "email": "n.zzfawfawefz.2209@gmail.com"}
    response = app.test_client().post('/api/user',
                                      data=json.dumps(data_sended),
                                      content_type='application/json',)

    assert response.status_code == 200
    response_body = response.get_json()
    assert response_body['added_user']['username'] == data_sended['name']
    assert response_body['added_user']['email'] == data_sended['email']


data_sended = [
    "hello",
    {"gg": "zafwfawfzzz", "email": "n.zzfawfawefz.2209@gmail.com"},
    {"name": "zafwfawfzzz", "xx": "n.zzfawfawefz.2209@gmail.com"}
]

content_type = [
    "text/html",
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
        "result": False,
        "errors": {
            "gg": [
                "unknown field"
            ],
            "name": [
                "required field"
            ]
        }
    },
    {
        "result": False,
        "errors": {
            "email": [
                "required field"
            ],
            "xx": [
                "unknown field"
            ]
        }
    }
]


@pytest.mark.parametrize("data_sended, content_type, expected",
                         [
                             (data_sended[0], content_type[0], expected[0]),
                             (data_sended[1], content_type[1], expected[1]),
                             (data_sended[2], content_type[2], expected[2])
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
    data_sended = {"name": "Hiep", "email": "n.vanhiep@gmail.com"}
    response = app.test_client().patch('/api/user/5',
                                       data=json.dumps(data_sended),
                                       content_type='application/json',)

    assert response.status_code == 200
    response_body = response.get_json()
    assert response_body['updated_user']['username'] == data_sended['name']
    assert response_body['updated_user']['email'] == data_sended['email']


@pytest.mark.parametrize("data_sended, content_type, expected",
                         [
                             (data_sended[0], content_type[0], expected[0]),
                             (data_sended[1], content_type[1], expected[1]),
                             (data_sended[2], content_type[2], expected[2])
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
    data_sended = {"name": "Hiep", "email": "n.vanhiep@gmail.com"}
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
    assert response_body['deleted_users'] == test_users
