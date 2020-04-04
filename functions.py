def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


def square(number):
    return number * number


user_first_name = input("Please enter your first name : ")
user_last_name = input("Please enter your last name : ")
print("Start")
greet_user(last_name=user_last_name, first_name=user_first_name)  # This way, they are keyword arguments
print("Finish")

# Keyword arguments increase the readability of your code
# They should always be used after positional arguments.

print(square(7))
