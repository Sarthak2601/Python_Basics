for i in 'Python':
    print(i)

for i in ['Sarthak', 'Agarwal', 'Coder']:
    print(i)

for i in range(10):  # Range function creates a list of elements -- in here 0 to 9
    print(i)

for i in range(2, 10):  # Range from 2-9
    print(i)

for i in range(2, 10, 2):   # last parameter is the step parameter -- O/P - 2,4,6,8
    print(i)

#EXERCISE

prices = [10,20,30]
total = 0
for cost in prices:
    total += cost
print(f"Total : {total}")