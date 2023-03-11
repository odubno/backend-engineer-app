import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_names(client):
    response = client.get('/employees')
    employees = response.json

    assert response.status_code == 200
    assert len(employees) == 6
    assert employees == [{'gender': 'male', 'id': 1}, {'gender': 'male', 'id': 2}, {'gender': 'male', 'id': 3}, {'gender': 'female', 'id': 4}, {'gender': 'female', 'id': 5}, {'gender': 'female', 'id': 6}]
