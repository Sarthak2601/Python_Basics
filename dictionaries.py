customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True
}
# Keys should be unique
# Look at it as a dictionary with a word and its meaning

print(customer.get("birthdate"))   # Using the get method we will not be returned an error.

print(customer.get("Birthdata", "26-01-2001"))  # Prints the value given as it becomes the default value

customer["name"] = "Jack Smith"  # Updating

customer["birthdate"] = "26-01-2001"  # Addition

print(customer)  # Printing

# Exercise - Ask for number and print those numbers

number = (input("Enter your phone number"))
digits_mapping = {
    "0" : "Zero",
    "1" : "One",
    "2" : "Two",
    "3" : "Three",
    "4" : "Four",
    "5" : "Five",
    "6" : "Six",
    "7" : "Seven",
    "8" : "Eight",
    "9" : "Nine",
}
output = ""
for ch in number :
    output += digits_mapping.get(ch, "!") + " "  # ! is a default value
print(output)