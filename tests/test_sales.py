def test_sale_creation(auth_token):
    from tests.conftest import client

    headers = {"Authorization": f"Bearer {auth_token}"}


    cat = client.post(
        "/api/categories/",
        json={"name": "Stationery"},
        headers=headers
    ).json()


    sup = client.post(
        "/api/suppliers/",
        json={"name": "Local"},
        headers=headers
    ).json()


    product = client.post(
        "/api/products/",
        json={
            "name": "Pen",
            "sku": "PEN-01",
            "price": 10,
            "quantity": 100,
            "category_id": cat["id"],
            "supplier_id": sup["id"]
        },
        headers=headers
    ).json()

    # Create sale
    sale = client.post(
        "/api/sales/",
        json={
            "product_id": product["id"],
            "quantity_sold": 5
        },
        headers=headers
    )

    assert sale.status_code == 200
