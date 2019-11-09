import json
import pytest
from app import bcrypt
from app.test.test_api.test_user import data_sended, content_type, expected


def test_register(app):
    data_sended = {"name": "zafwfawfzzz", "email": "n.zzfawfawefz.2209@gmail.com", "password": "1234567gG"}
    response = app.test_client().post('/api/register',
                                      data=json.dumps(data_sended),
                                      content_type='application/json',)
    assert response.status_code == 200
    response_body = response.get_json()
    assert response_body['message'] == "Thanks for registering! Please check your email to confirm your email address."
    assert response_body['added_user']['username'] == data_sended['name']
    assert response_body['added_user']['email'] == data_sended['email']
    assert bcrypt.check_password_hash(response_body['added_user']["password"], data_sended["password"])


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
def test_register_fail(app, data_sended, content_type, expected):
    response = app.test_client().post('/api/register',
                                      data=json.dumps(data_sended),
                                      content_type=content_type,)
    assert response.status_code == 400
    response_body = response.get_json()
    assert response_body == expected


def test_confirm_email(app):
    data_sended = {"name": "sonnguyen", "email": "khraxo95@gmail.com", "password": "1xxxxxxxAA"}
    response_register = app.test_client().post('/api/register',
                                               data=json.dumps(data_sended),
                                               content_type='application/json',)

    confirmation_token = response_register.get_json()['confirmation_token']

    response_comfirm = app.test_client().get('/api/register/confirm/' + confirmation_token)

    assert response_comfirm.status_code == 200
    assert response_comfirm.get_json()['message'] == 'Thank you for confirming your email address.'
    assert response_comfirm.get_json()['your_email'] == data_sended["email"]

    response_comfirm = app.test_client().get('/api/register/confirm/' + confirmation_token)

    assert response_comfirm.get_json()['message'] == "Account already confirmed. Please login."
    
