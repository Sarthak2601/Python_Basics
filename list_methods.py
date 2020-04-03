numbers = [5, 1, 4, 7, 8, 5]
numbers.append(12)  # Insert a member at the last
print(numbers)

numbers.insert(2, 6)  # Insert a member at a certain index
print(numbers)

numbers.pop()  # Removes the last element
print(numbers)

numbers.pop(1)  # Removes element from a certain index
print(numbers)

print(numbers.index(4))  # Returns the index of this value
# numbers.clear()  # Empties the list

print(numbers.count(5))  # Counts the number of 5's

numbers.sort()  # Ascending order
print(numbers)
numbers.reverse()  # Add this for descending order
print(numbers)

numbers2 = numbers.copy()  # makes a copy of list

# Challenge -- Remove the duplicates in a list

# Approach 1
list = [4, 5, 2, 4, 5, 2]
for i in list:
    if list.count(i) > 1:
        index = list.index(i)
        list.pop(index)
print(list)

# Approach 2

listing = [4, 5, 2, 4, 5, 2]
unique = []
for i in listing :
    if i not in unique:
        unique.append(i)
print(unique)
