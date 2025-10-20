import random

dinner_bill = {}

def get_valid_float(prompt):
    """Keep asking until valid positive float is entered"""
    while True:
        value = input(prompt)
        try:
            float_value = float(value)
            if float_value <= 0:
                print("Bill value must be positive")
            else:
                return float_value
        except ValueError:
            print("Invalid bill value")

def get_yes_no_input(prompt):
    """Keep asking until Yes or No is entered"""
    while True:
        response = input(prompt)
        if response in ["Yes", "No"]:
            return response
        else:
            print("Please enter either Yes or No")

people = input("Enter the number of friends joining (including you):")
if people.isdigit() and int(people) > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(int(people)):
        name = input()
        dinner_bill[name] = 0

    print()
    total_bill = get_valid_float("Enter the total bill value:\n")
    bill_per_person = round(total_bill / len(dinner_bill), 2)
    for name, value in dinner_bill.items():
        dinner_bill[name] = bill_per_person

    lucky_feature = get_yes_no_input('Do you want to use the "Who is lucky?" feature? Write Yes/No:\n')
    if lucky_feature == "Yes":
        lucky_one = random.choice(list(dinner_bill.keys()))
        print(f"{lucky_one} is the lucky one!")

        bill_per_person = round(total_bill / (len(dinner_bill) - 1), 2)
        for name, value in dinner_bill.items():
            dinner_bill[name] = bill_per_person
        dinner_bill[lucky_one] = 0.00
    else:
        print("No one is going to be lucky")

    print(dinner_bill)
else:
    print("No one is joining for the party")