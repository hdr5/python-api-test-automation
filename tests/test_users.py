import requests

BASE_URL = "http://127.0.0.1:8000"

def test_create_get_and_delete_user():
    payload = {
        "name": "Test User",
        "email": "test@example.com"
    }

    # Create user
    create_response = requests.post(
        BASE_URL + "/users",
        json=payload
    )

    assert create_response.status_code == 201

    created_user = create_response.json()

    assert created_user["name"] == "Test User"
    assert created_user["email"] == "test@example.com"

    user_id = created_user["id"]

    # Verify user exists
    get_response = requests.get(BASE_URL + "/users")

    assert get_response.status_code == 200

    users = get_response.json()

    user_exists = any(user["id"] == user_id for user in users)

    assert user_exists

    # Delete user
    delete_response = requests.delete(
        BASE_URL + f"/users/{user_id}"
    )

    assert delete_response.status_code == 200

    # Verify user was deleted
    get_response = requests.get(BASE_URL + "/users")

    users = get_response.json()

    user_exists = any(user["id"] == user_id for user in users)

    assert not user_exists

def test_get_users():
    response = requests.get(BASE_URL + "/users")

    assert response.status_code == 200

    users = response.json()

    assert isinstance(users, list)
    assert users[0]["name"] == "David"
    assert users[1]["email"] == "sarah@example.com"
