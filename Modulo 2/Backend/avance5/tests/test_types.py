import json

def test_get_types_empty(client, user_token):
    response = client.get("/types", headers={"Authorization": f"Bearer {user_token}"})
    assert response.status_code in [200, 401]
    if response.status_code == 200:
        data = response.get_json()
        assert "data" in data

def test_create_type_missing_field(client, admin_token):
    response = client.post(
        "/types",
        data=json.dumps({}),
        content_type="application/json",
        headers={"Authorization":  f"Bearer {admin_token}"}
    )
    assert response.status_code == 400
    assert "Description is required" in response.get_json()["error"]

def test_update_type_not_found(client, admin_token):
    response = client.put(
        "/types/9999",
        data=json.dumps({"description": "NewType"}),
        content_type="application/json",
        headers={"Authorization":  f"Bearer {admin_token}"}
    )
    assert response.status_code in [404, 401]
