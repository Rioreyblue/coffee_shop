available_coffee = [
    {"id": 1, "name": "black coffee", "price": 100, "quantity": 2},
    {"id": 1, "name": "choco latte coffee", "price": 150, "quantity": 2},
    {"id": 1, "name": "mocha coffee", "price": 200, "quantity": 2},
    {"id": 1, "name": "caramel coffee", "price": 250, "quantity": 2},
]

def coffees():
    for coffee in available_coffee:
        print(f"[{coffee['id']}]. [{coffee['name']}] = [{coffee['price']}] - [{coffee['quantity']}]")