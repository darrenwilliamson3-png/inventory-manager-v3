from inputs import input_int, input_float, input_str
from inventory import add_product, set_stock, delete_product
from storage import load_products, save_products

DATA_FILE = "products.csv"

def show_products(products: list[dict]) -> None:
    if not products:
        print("No products found")
        return

    print("\nID | Name | Price | Stock")
    print("-" * 30)
    for p in sorted(products, key=lambda p: p["id"]):
        print(f"{p['id']} | {p['name']} | {p['price']} | {p['stock']}|")

def show_menu() -> None:
    print("\nInventory Manager (IMV3)")
    print("1. Show all products")
    print("2. Add a product")
    print("3. Edit Stock")
    print("4. Save products")
    print("5. Delete products")
    print("6. Show products by name")
    print("0. Exit")

def main() -> None:
    products = load_products(DATA_FILE)
    dirty = False

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_products(products)

        elif choice == "2":
            product_id = input_int("Product ID: ")
            if product_id is None:
                continue

            name = input_str("Name: ")
            if name is None:
                continue

            price = input_float("Price: ")
            if price is None:
                continue

            stock = input_int("Stock: ")
            if stock is None:
                continue

            if add_product(products, product_id, name, price, stock):
                print("Product added!")
                dirty = True
            else:
                print("Product not added!")

        elif choice == "3":
            product_id = input_int("Product ID: ")
            if product_id is None:
                continue

            new_stock = input_int("New Stock Value")
            if new_stock is None:
                continue

            if set_stock(products, product_id, new_stock):
                print("Stock updated.")
                dirty = True
            else:
                print("Stock not updated.")

        elif choice == "4":
            save_products(DATA_FILE, products)
            dirty = False
            print("Products saved.")

        elif choice == "5":
            product_id = input_int("Product ID to delete: ")
            if product_id is None:
                continue

            if delete_product(products, product_id):
                print("Product deleted.")
                dirty = True
            else:
                print("Product not found")

        elif choice == "6":
            term = input_str("Search term: ")
            if term is None:
                continue

            matches = [
                p for p in products
                if term.lower() in p["name"].lower()
            ]

            if not matches:
                print("No matching products found!")
            else:
                show_products(matches)

        elif choice == "0":
            if dirty:
                answer = input("You have unsaved changes. Save before you exit (y/n)").strip()
                if answer == "y":
                    save_products(DATA_FILE, products)
                    print("Product saved.")
                print("GoodBye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()