from fastapi.testclient import TestClient # type: ignore
from http import HTTPStatus


from fastapi_zero.app import app

def test_root_deve_retornar_ola_mundo():
    #Arrange
    client = TestClient(app) 
    #Act
    response = client.get('/')
    #Assert
    assert response.json() == {'message': 'Olá mundo!'}
    assert response.status_code == HTTPStatus.OK
