import json


test_users = [
        {"id": 1, "username": "Son", "email": "n.vanson@gmail.com"},
        {"id": 2, "username": "Hoan", "email": "n.vanhoan@gmail.com"},
        {"id": 3, "username": "Lam", "email": "n.tunglam@gmail.com"},
        {"id": 4, "username": "Hung", "email": "n.vanhung@gmail.com"},
        {"id": 5, "username": "Nam", "email": "n.huynam@gmail.com"},
        {"id": 6, "username": "Viet", "email": "n.vanviet@gmail.com"},
        {"id": 7, "username": "zzzz", "email": "n.zzz.2209@gmail.com"}
]


def test_get(app):
    response = app.test_client().get('/api/user')
    assert response.status_code == 200
    response_body = response.get_json()
    assert response_body['users'] == test_users


# def test_post(app):
#     data_sended = {"name": "zzzz", "email": "n.zzz.2209@gmail.com"}
#     response = app.test_client().post('/api/user',
#                                       data=json.dumps(data_sended),
#                                       content_type='application/json',)

#     assert response.status_code == 200
#     response_body = response.get_json()
#     assert response_body['added_user']['username'] == data_sended['name']
#     assert response_body['added_user']['email'] == data_sended['email']

