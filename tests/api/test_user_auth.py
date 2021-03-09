from fastapi import status

from .fixtures import test_client, fake_db


def test_user_correct_registration(test_client, fake_db):
    user_data = {
        'email': 'example911@example.com',
        'password': 'Qwerty123@'
    }
    response = test_client.post('/api/v1/auth/register', data=user_data)
    assert response.status_code == status.HTTP_201_CREATED
    assert 'user_uuid' in response.json()
