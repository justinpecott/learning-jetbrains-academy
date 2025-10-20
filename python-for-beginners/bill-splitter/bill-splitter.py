dinner_bill = {}

people = input("Enter the number of friends joining (including you):")
if people.isdigit() and int(people) > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(int(people)):
        name = input()
        dinner_bill[name] = 0

    print()
    print(dinner_bill)
else:
    print("No one is joining for the party")