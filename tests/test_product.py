def test_product_crud(auth_token):
    from tests.conftest import client

    headers = {"Authorization": f"Bearer {auth_token}"}


    cat = client.post(
        "/api/categories/",
        json={"name": "TestCat"},
        headers=headers
    ).json()


    sup = client.post(
        "/api/suppliers/",
        json={"name": "TestSupplier"},
        headers=headers
    ).json()


    res = client.post(
        "/api/products/",
        json={
            "name": "Test Product",
            "sku": "SKU001",
            "price": 100,
            "quantity": 5,
            "category_id": cat["id"],
            "supplier_id": sup["id"]
        },
        headers=headers
    )

    assert res.status_code == 200
