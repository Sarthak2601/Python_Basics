for x in range(2):
    for y in range(2):
        print(f"({x},{y})")

# Challenge - Draw a F

numbers = [5, 2, 5, 2, 2]
string = 'x'
final_string = ''
for x in numbers:
    final_string = ''
    for y in range(x):
        final_string += string
    print(final_string)

# For making a L ==> numbers = [2,2,2,2,5]

