print('%.3f' % (11/3))  # 3.667
print('Mix {}, {} and a {} to make an ideal omelet.'.format('2 eggs', '30 g of milk', 'pinch of salt'))
print('{0} in the {1} by Frank Sinatra'.format('Strangers', 'Night'))
print('The {film} at {theatre} was {adjective}!'.format(film='Lord of the Rings',
                                                        adjective='incredible',
                                                        theatre='BFI IMAX'))
print('The {0} was {adjective}!'.format('Lord of the Rings', adjective='incredible'))
# The Lord of the Rings was incredible!

name = 'Elizabeth II'
title = 'Queen of the United Kingdom and the other Commonwealth realms'
reign = 'the longest-lived and longest-reigning British monarch'
f'{name}, the {title}, is {reign}.'

hundred_percent_number = 1823
needed_percent = 16
needed_percent_number = hundred_percent_number * needed_percent / 100

print(f'{needed_percent}% from {hundred_percent_number} is {needed_percent_number}')
# 16% from 1823 is 291.68

print(f'Rounding {needed_percent_number} to 1 decimal place is {needed_percent_number:.1f}')
# Rounding 291.68 to 1 decimal place is 291.7

# word = input()
# print('{} has {} letters'.format(word, len(word)))

# a = float(input())
# b = int(input())
# print(f'{a:.{b}f}')

print("%.4f".format(3.14159265358979))
print("{1} {1} {1}".format(1, 2, 3))
#print("{1} is a {kind}".format(kind="fruit", "grapefruit"))
print("{city} is the capital of {country}".format(country="Portugal",
                                            city="Lisbon"))

