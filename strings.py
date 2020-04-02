course = "Python's course"

# Usage of "" and ''

#Triple quotes - multiple lines
print(
'''
Hi, 
Hello, 
Bye  
''')

# positive and negative indices

print(course[-2])

# Returning a number of variables at specific indices

print(course[0:3])  # the element at 3rd index won't be included.
print(course[3:])   # second index = total length
print((course[:5]))  # first index = 0

# Formatted String

first = 'Sarthak'
last = 'Agarwal'
message = f"{first} [{last}] is a coder"    # Dynamic insertion of values
print(message)

