import pytest
from main import predict, app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_index_route(client):
    """Test the index route."""
    response = client.get('/')
    assert response.status_code == 200


def test_predict_route(client):
    """Test the predict route."""
    response = client.get('/predict')
    assert response.status_code == 200



