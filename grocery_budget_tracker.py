def add_item(name, price, quantity):
    return {
        "name": name,
        "price": price,
        "quantity": quantity 
    }

def calculate_total(shopping_list):
    total = 0
    for item in shopping_list:
        total += item["price"] * item["quantity"]
    return total

shopping_list = []

shopping_list.append(add_item("bread", 30, 4))

for item in shopping_list:
    print(item["name"], "-", item["quantity"], "x", item["price"])

budget = float(input("What is your budget? "))
total = calculate_total(shopping_list)

print("Total cost: ", total)

if total > budget:
    print("You are over budget")
else:
    print("You are within budget")