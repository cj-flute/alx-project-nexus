import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_user_registration():
    client = APIClient()
    data = {
        "username": "TestUser",
        "email": "test@test.com",
        "first_name": "Test",
        "last_name": "User",
        "password": "TestPass123!"
    }
    response = client.post("/api/auth/register/", data)
    assert response.status_code == 201
    assert User.objects.filter(email="test@test.com").exists()


@pytest.mark.django_db
def test_user_login():
    user = User.objects.create_user(
        email="test@test.com",
        username="TestUser",
        password="TestPass123!"
    )

    client = APIClient()
    data = {
        "email": "test@test.com",
        "password": "TestPass123!"
    }
    response = client.post("/api/auth/login/", data)
    assert response.status_code == 200
    assert "access" in response.json()
    assert "refresh" in response.json()
