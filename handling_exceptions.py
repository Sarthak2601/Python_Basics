# In python we handle exceptions using try and except

try:
    age = int(input("Enter your age : "))
    income = 2000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("Age can't be 0.")
except ValueError:
    print("Invalid age, enter numeric.")

