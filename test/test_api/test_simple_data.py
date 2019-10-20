import json
from app import create_app


app = create_app()


def test_post():
    payload = {"name": "Viet", "email": "n.vanviet.2209@gmail.com"}
    response = app.test_client().post('/api/user',
                                      data=json.dumps(payload),
                                      content_type='application/json',)

    assert response.status_code == 200
    response_body = response.get_json()
    assert response_body['added_user']['email'] == payload['email']
