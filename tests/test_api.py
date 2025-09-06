def test_get_users(api_client):
    response = api_client.get("/users")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_single_user(api_client):
    response = api_client.get("/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1

def test_create_post(api_client, test_data):
    response = api_client.post("/posts", json=test_data["new_post"])
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == test_data["new_post"]["title"]
    assert data["userId"] == test_data["new_post"]["userId"]

def test_delete_post(api_client):
    response = api_client.delete("/posts/1")
    assert response.status_code == 200

def test_get_invalid_user(api_client):
    response = api_client.get("/users/99999")
    assert response.status_code == 404
