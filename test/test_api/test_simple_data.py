import sys
sys.path.append('../')
from app import create_app


app = create_app()


def test_get():
    response = app.test_client().get('/api/user?key=editor')

    assert response.status_code == 200
    assert response.data == b'value: vscode '


def test_put():
    response = app.test_client().put('/api/simple_data?key=java')
    assert response.status_code == 200
    assert response.data == b"New keys with empty string values added: java"


def test_delete():
    response = app.test_client().delete('/api/simple_data?key=language')
    assert response.status_code == 200
    assert response.data == b'key: language has been deleted!'

# def test_post():
#     response = app.test_client().delete('/api/simple_data?key=language')
#     assert response.status_code == 200
#     assert response.data == b'New keys added: '