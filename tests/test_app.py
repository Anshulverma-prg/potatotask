import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_query_tweets(client):
    response = client.get('/query?term=music')
    assert response.status_code == 200
    assert 'hits' in response.get_json()

  
