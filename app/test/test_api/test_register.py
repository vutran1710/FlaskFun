import json
import pytest
from app.test.test_api.test_user import data_sended, content_type, expected
from unittest import mock
from app.api.register import generate_confirmation_token, generate_reset_token


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
    confirm_token = generate_confirmation_token(7, "khraxo95@gmail.com")
    mock_generate_confirmation_token.return_value = confirm_token
    app.test_client().post('/api/register',
                           data=json.dumps(data_sended),
                           content_type='application/json',)

    response = app.test_client().get('/api/register/confirm/' + confirm_token.decode('utf-8'))
    assert response.status_code == 200
    response_body = response.get_json()
    assert response_body['message'] == 'Thank you for confirming your email address.'
    assert response_body['your_email'] == data_sended["email"]

    # When user re-confirms with the same token
    response = app.test_client().get('/api/register/confirm/' + confirm_token.decode('utf-8'))
    assert response.status_code == 400
    response_body = response.get_json()
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
    response = app.test_client().get('/api/register/confirm/' + confirm_token.decode('utf-8'))
    assert response.status_code == 400
    response_body = response.get_json()
    assert response_body['description'] == "The confirmation link is invalid or has expired."


@mock.patch('app.api.register.generate_reset_token')
@mock.patch('app.api.register.send_password_reset_email')
def test_send_reset_func(mock_send_password_reset_email, mock_generate_reset_token, app):
    data_email = {"email": "tunglammeta@gmail.com"}

    app.test_client().post('/api/reset',
                           data=json.dumps(data_email),
                           content_type='application/json',)

    id, email = 3, data_email['email']
    mock_generate_reset_token.assert_called_with(id, email)
    mock_send_password_reset_email.assert_called_with(email, mock_generate_reset_token())


@mock.patch('app.api.register.generate_reset_token')
def test_reset_with_token(mock_generate_reset_token, app):
    data_email = {"email": "tunglammeta@gmail.com"}
    reset_token = generate_reset_token(3, "tunglammeta@gmail.com")
    mock_generate_reset_token.return_value = reset_token
    app.test_client().post('/api/reset',
                           data=json.dumps(data_email),
                           content_type='application/json',)

    data_password = {"new_password": "1234567cCc"}
    response = app.test_client().post('/api/reset/' + reset_token.decode('utf-8'),
                                      data=json.dumps(data_password),
                                      content_type='application/json',)

    assert response.status_code == 200
    response_body = response.get_json()
    assert response_body['message'] == 'Your password has been updated!'

    # When user re-confirms with the same token
    data_password = {"new_password": "1234567cCc"}
    response = app.test_client().post('/api/reset/' + reset_token.decode('utf-8'),
                                      data=json.dumps(data_password),
                                      content_type='application/json',)
    assert response.status_code == 400
    response_body = response.get_json()
    assert response_body['description'] == "Invalid token."
