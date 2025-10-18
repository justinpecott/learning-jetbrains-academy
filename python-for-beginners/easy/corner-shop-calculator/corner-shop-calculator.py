# print('Prices:')
# print('Bubblegum: $2')
# print('Toffee: $0.2')
# print('Ice cream: $5')
# print('Milk chocolate: $4')
# print('Doughnut: $2.5')
# print('Pancake: $3.2')

bg = 202
tf = 118
ic = 2250
mc = 1680
dn = 1075
pc = 80

print('Earned amount:')
print('Bubblegum: $' + str(bg))
print('Toffee: $' + str(tf))
print('Ice cream: $' + str(ic))    
print('Milk chocolate: $' + str(mc)) 
print('Doughnut: $' + str(dn)) 
print('Pancake: $' + str(pc))

incme = bg + tf + ic + mc + dn + pc
print()
print('Income: $' + str(incme))

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(*numbers, sep='')

staff_expenses = input('Staff expenses: ')
other_expenses = input('Other expenses: ')
net_income = incme - int(staff_expenses) - int(other_expenses)
print('Net income: $' + str(net_income))