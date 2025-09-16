import json

def test_create_invoice_missing_fields(client, admin_token):
    response = client.post(
        "/invoices",
        data=json.dumps({"code": "INV001"}),  # faltan campos
        content_type="application/json",
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert response.status_code == 400
    assert "Missing required fields" in response.get_json()["error"]

def test_delete_invoice_not_found(client, admin_token):
    response = client.delete(
        "/invoices/9999",
        headers={"Authorization": f"Bearer {admin_token}"}
    )
    assert response.status_code in [404, 401]
