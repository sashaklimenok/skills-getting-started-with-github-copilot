import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# Arrange-Act-Assert: GET /activities

def test_get_activities():
    # Arrange
    # ... TestClient уже создан ...
    
    # Act
    response = client.get("/activities")
    
    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Arrange-Act-Assert: POST /activities/{activity_name}/signup

def test_signup_for_activity_success():
    # Arrange
    activity_name = "Yoga"
    email = "testuser@example.com"
    
    # Act
    response = client.post(f"/activities/{activity_name}/signup", json={"email": email})
    
    # Assert
    assert response.status_code == 200 or response.status_code == 201
    assert "message" in response.json()

# Arrange-Act-Assert: POST /activities/{activity_name}/signup (activity not found)

def test_signup_for_activity_not_found():
    # Arrange
    activity_name = "NonExistent"
    email = "testuser@example.com"
    
    # Act
    response = client.post(f"/activities/{activity_name}/signup", json={"email": email})
    
    # Assert
    assert response.status_code == 404
    assert "detail" in response.json()

# Arrange-Act-Assert: GET /

def test_root_redirect():
    # Arrange
    # ... TestClient уже создан ...
    
    # Act
    response = client.get("/", allow_redirects=False)
    
    # Assert
    assert response.status_code in (301, 302)
    assert "Location" in response.headers
    assert response.headers["Location"].endswith("/static/index.html")
