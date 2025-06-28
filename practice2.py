clients = [
    {"name": "Alice", "age": 30, "country": "USA", "purchases": ["apple", "banana"]},
    {"name": "Bob", "age": 25, "country": "Spain", "purchases": ["apple", "orange"]},
    {"name": "Charlie", "age": 35, "country": "France", "purchases": ["grape", "banana", "apple"]},
    {"name": "Diana", "age": 28, "country": "USA", "purchases": ["banana", "mango"]}
]

def unique (clients):
    g = set()
    for clients in clients:
        g.update(clients["purchases"])
    return g
print(unique(clients))

def count_products(clients):
    product_count = {}
    for client in clients:
        for item in client["purchases"]:
            if item in product_count:
                product_count[item] += 1
            else:
                product_count[item] = 1
    return product_count
print(count_products(clients))

def vip(clients):
    for client in clients:
        if len(client["purchases"]) > 2:
            client["vip"] = True
        else:
            client["vip"] = False
    return clients
print(vip(clients))

def filter(clients):
    filtered = []
    for client in clients:
        if client["country"] == "USA":
            filtered.append(client)
    return filtered
print(filter(clients))

def sorting(clients):
    return sorted(clients, key=lambda client: client["age"])
print(sorting(clients))
