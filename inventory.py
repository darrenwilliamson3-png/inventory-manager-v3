def find_product(products: list[dict], product_id: int) -> dict | None:
    for product in products:
        if product["id"] == product_id:
            return product
    return None

def add_product(
        products: list[dict],
        product_id: int,
        name: str,
        price: float,
        stock: int,
) -> bool:
    if price < 0 or stock < 0:
        return False

    if find_product(products, product_id) is not None:
        return False

    products.append({
        "id": product_id,
        "name": name,
        "price": price,
        "stock": stock
    })
    return True

def set_stock(products: list[dict], product_id: int, new_stock: int) -> bool:
    if new_stock < 0:
        return False

    product = find_product(products, product_id)
    if product is None:
        return False

    product["stock"] = new_stock
    return True

def delete_product(products: list[dict], product_id: int) -> bool:
    product = find_product(products, product_id)
    if product is None:
        return False

    products.remove(product)
    return True