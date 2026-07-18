# PART 1: Create two fruit baskets as sets

basket1 = {"apple", "banana", "mango", "apple", "grape"}

basket2 = {"mango", "kiwi", "banana", "kiwi"}

print("Basket 1:", basket1)

print("Basket 2:", basket2)

# PART 2: Add a new fruit to basket1

basket1.add("orange")

print("Basket 1 after adding orange:", basket1)

# PART 3: Find fruits common to both baskets

common_fruits = basket1.intersection(basket2)

print("Fruits in both baskets:", common_fruits)