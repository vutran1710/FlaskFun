import json


def test_login(app):
    data_sended = {"name": "Lam", "password": "1234567cC"}
    response = app.test_client().post('/api/login',
                                      data=json.dumps(data_sended),
                                      content_type='application/json',)
    assert response.status_code == 200
    response_body = response.get_json()
    assert response_body['message'] == "Login success."
    assert response_body['user']['username'] == data_sended['name']
    assert response_body['token']


def test_logout(app):
    data_sended = {"name": "Lam", "password": "1234567cC"}
    resp_login = app.test_client().post('/api/login',
                                        data=json.dumps(data_sended),
                                        content_type='application/json',)
    headers = {
        'Authorization': 'Bearer {}'.format(resp_login.get_json()['token'])
    }
    response = app.test_client().put('/api/logout', headers=headers)
    assert response.status_code == 200
    response_body = response.get_json()
    assert response_body['message'] == "Successfully logged out."
