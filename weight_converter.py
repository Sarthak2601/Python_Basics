weight = int(input('Enter your weight in kg or gm'))
original_input = input('is it in (K)g or (G)m ?')
formatted_input = original_input.upper()
if formatted_input == 'K':
    print(f"Your weight in grams is {weight * 1000}")
elif formatted_input == 'G':
    print(f"Your weight in kilograms is {weight / 1000}")
else:
    print("Please enter a valid character")
