import json

import json

def test_create_product_success(client, admin_token):
    """Crear un producto con todos los campos requeridos"""
    payload = {
        "code": "PRD100",
        "price": 250,
        "id_brand": 1,
        "id_type": 1
    }

    response = client.post(
        "/products",
        data=json.dumps(payload),
        content_type="application/json",
        headers={"Authorization": f"Bearer {admin_token}"}
    )

    assert response.status_code == 201
    data = response.get_json()
    assert "message" in data
    assert data["message"] == "Product created"
    assert "id" in data
    assert isinstance(data["id"], int)

def test_delete_product_not_found(client, admin_token):
    """Intentar eliminar un producto que no existe"""
    response = client.delete("/products/9999", headers={"Authorization": f"Bearer {admin_token}"})
    assert response.status_code == 404
    assert "Producto no encontrado" in response.get_json()["error"]
