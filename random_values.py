import random
from DiceRoll import Dice

print(random.random())  # Generates random values between 0 and 1
print(random.randint(10, 20))  # Generates random values between the specified limits

members = ["Rajeev", "Anjali", "Kriti", "Sarthak"]
leader = random.choice(members)  # Picks a list element randomly
print(f"The team leader is {leader}")

diceRoll = Dice()
print(diceRoll.roll())