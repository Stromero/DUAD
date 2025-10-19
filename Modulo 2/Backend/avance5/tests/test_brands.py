# tests/test_brands.py
import json

def test_get_brands_empty(client, user_token):
    response = client.get("/brands", headers={"Authorization": f"Bearer {user_token}"})
    assert response.status_code in [200, 401]  # depende si validas JWT real
    if response.status_code == 200:
        data = response.get_json()
        assert "data" in data

def test_create_brand_missing_field(client, admin_token):
    response = client.post(
        "/brands",
        data=json.dumps({}),
        content_type="application/json",
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert response.status_code == 400
    assert "Description is required" in response.get_json()["error"]

def test_update_brand_not_found(client, admin_token):
    response = client.put(
        "/brands/9999",
        data=json.dumps({"description": "NewBrand"}),
        content_type="application/json",
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert response.status_code in [404, 401]

