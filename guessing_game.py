secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    input_number = int(input("Guess?"))
    guess_count +=1
    if input_number == secret_number :
        print("Congratulations, you won!")
        break  # Exits the loop
else:
    print("Sorry, you failed")

