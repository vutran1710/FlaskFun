import json
import pytest
from app import bcrypt
from app.test.test_api.test_user import data_sended, content_type, expected
from unittest import mock
from app.api.register import generate_confirmation_token


@mock.patch('app.api.register.generate_confirmation_token')
@mock.patch('app.api.register.send_confirmation_email')
def test_send_email_func(mock_send_confirmation_email, mock_generate_confirmation_token, app):
    data_sended = {"name": "sonnguyen", "email": "khraxo95@gmail.com", "password": "1xxxxxxxAA"}

    response = app.test_client().post('/api/register',
                                      data=json.dumps(data_sended),
                                      content_type='application/json',)
    data = response.get_json()['added_user']
    id, email = data['id'], data['email']
    mock_generate_confirmation_token.assert_called_with(id, email)
    mock_send_confirmation_email.assert_called_with(email, mock_generate_confirmation_token())


def test_register(app):
    data_sended = {"name": "sonnguyen", "email": "khraxo95@gmail.com", "password": "1xxxxxxxAA"}
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


@mock.patch('app.api.register.generate_confirmation_token')
def test_confirm_email(mock_generate_confirmation_token, app):
    data_sended = {"name": "sonnguyen", "email": "khraxo95@gmail.com", "password": "1xxxxxxxAA"}
    confirm_token = generate_confirmation_token("7", "khraxo95@gmail.com")
    mock_generate_confirmation_token.return_value = confirm_token
    app.test_client().post('/api/register',
                           data=json.dumps(data_sended),
                           content_type='application/json',)

    reponse = app.test_client().get('/api/register/confirm/' + confirm_token.decode('utf-8'))
    assert reponse.status_code == 200
    response_body = reponse.get_json()
    assert response_body['message'] == 'Thank you for confirming your email address.'
    assert response_body['your_email'] == data_sended["email"]

    # When user re-confirms with the same token
    reponse = app.test_client().get('/api/register/confirm/' + confirm_token.decode('utf-8'))
    response_body = reponse.get_json()
    assert response_body['description'] == "Invalid token."


@pytest.mark.skip(reason="Need to wait 30s")
@mock.patch('app.api.register.generate_confirmation_token')
def test_confirm_email_fail(mock_generate_confirmation_token, app):
    data_sended = {"name": "sonnguyen", "email": "khraxo95@gmail.com", "password": "1xxxxxxxAA"}
    confirm_token = generate_confirmation_token("7", "khraxo95@gmail.com")
    mock_generate_confirmation_token.return_value = confirm_token
    app.test_client().post('/api/register',
                           data=json.dumps(data_sended),
                           content_type='application/json',)

    import time
    time.sleep(31)
    reponse = app.test_client().get('/api/register/confirm/' + confirm_token.decode('utf-8'))
    response_body = reponse.get_json()
    assert response_body['description'] == "The confirmation link is invalid or has expired."
