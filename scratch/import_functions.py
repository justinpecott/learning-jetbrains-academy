# import super_module
# super_module.super_function()  # calling a function defined in super_module
# print(super_module.super_variable)  # accessing a variable defined in super_module


# from super_module import super_function
# super_function()  # super_function is now available directly at the current module
# super_module.super_function()  # note, that in this case name super_module is not imported, 
                               # so this line leads to an error

import math
print(math.factorial(5))  # prints the value of 5!
print(math.log(10))  # prints the natural logarithm of 10
print(math.pi)  # math also contains several constants
print(math.e)


from string import digits
print(digits)  # prints all the digit symbols


import random
print(random.choice(['red', 'green', 'yellow']))  # print a random item from the list
random.seed(6)
random.randrange(-100, 100)

print(math.expm1(-57))