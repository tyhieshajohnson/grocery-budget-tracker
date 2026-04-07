name = input("What is your name? ")
print("Hello", name)

price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
print("What is the price? ", price)
print("What is the quantity? ", quantity)

total = price * quantity
print("The total is: ", total)

# Operators allow us to perform calculations:
# + addition
# - substraction
# * multiplatication
# / division
budget = 20

if total < budget:
    print("You are under budget")
elif total == budget:
    print("You used your full budget babe")
else: 
    print("You are over budget")

item = input("What item would you like to buy? ")
print("Please don't forget to buy, ", item)

items = ["bread", "milk", "cheese"]
print(items[1])

for item in items:
    print(item)

item = {
    "name": "bread",
    "price": 18.50,
    "quantity": 2
}
print(item)

def calculate_total(prices):
    total = 0
    for price in prices:
        # this is short hand for: total = total + price
        total += price
    return total

print(calculate_total([10,20,30]))