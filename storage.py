import csv

def load_products(filename: str) -> list[dict]:
    products = []

    try:
        with open(filename, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                try:
                    products.append({
                        "id": int(row["id"]),
                        "name": row["name"],
                        "price": float(row["price"]),
                        "stock": int(row["stock"]),
                    })
                except (ValueError, KeyError):
                    # Skip malformed rows
                    continue
    except FileNotFoundError:
        pass
    return products

def save_products(filename: str, products: list[dict]) -> None:
    with open(filename, "w", newline="", encoding="utf-8") as f:
        fieldnames = ["id", "name", "price", "stock"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        for product in products:
            writer.writerow(product)