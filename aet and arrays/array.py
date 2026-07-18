import array as arr

my_array = arr.array('i', [1,2,3,4,5,5])

print(my_array)

print(my_array.count(5))

my_array.reverse()

print(my_array)

# PART 4: Create an array of fruit counts using the array module

import array as arr

fruit_counts = arr.array('i', [3, 5, 2, 4])

print("Fruit counts array:", fruit_counts)

# PART 5: Add new fruit counts to the array

fruit_counts.insert(0, 1)

fruit_counts.append(6)

print("Fruit counts after adding items:", fruit_counts)

# PART 6: Count how many times the number 4 appears in the array

count_of_4 = fruit_counts.count(4)

print("Number of times 4 appears:", count_of_4)

# PART 7: Reverse the order of the fruit counts array

fruit_counts.reverse()

print("Reversed fruit counts array:", fruit_counts)