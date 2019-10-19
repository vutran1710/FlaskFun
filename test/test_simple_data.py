from app import create_app


app = create_app()


def test_get():
    response = app.test_client().get('/api/simple_data/?key=editor')

    assert response.status_code == 200
    assert response.data == b'value: vscode'
#  assert response.data == b'java' #fail


def test_put():
    response = app.test_client().put('/api/simple_data/?key=java')
    assert response.status_code == 200
    assert response.data == b'New keys added: java'


def test_delete():
    response = app.test_client().delete('/api/simple_data/?key=language')
    assert response.status_code == 200
    assert response.data == b'key: language has been deleted!'
