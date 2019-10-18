from app import app

"""install: pip install -U pytest
  Check version: pytest --version
"""
def test_get():
    response = app.test_client().get('/?key=editor')

    assert response.status_code == 200
    assert response.data == b'value: vscode' #pass
  #  assert response.data == b'java' #fail

def test_put():
    response = app.test_client().put('/data?key=java')
    assert response.status_code == 200
    assert response.data == b'New keys added: java' #pass

def test_delete():
    response = app.test_client().delete('/data?key=language')
    assert response.status_code == 200
    assert response.data == b'key: language has been deleted!' #pass

