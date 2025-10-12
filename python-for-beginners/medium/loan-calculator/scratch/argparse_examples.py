import argparse

parser = argparse.ArgumentParser(description="This program prints recipes \
consisting of the ingredients you provide.")

parser.add_argument("-i1", "--ingredient_1")  # optional argument
                                              # or
parser.add_argument("ingredient_1")           # positional argument

parser.add_argument("--salt", action="store_true")

parser.add_argument("--pepper", default=False)

parser.add_argument("-i2", "--ingredient_2",
                    choices=["pasta", "rice", "potato", "onion",
                             "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                    help="You need to choose only one ingredient from the list.")

args = parser.parse_args()

print(args.ingredient_2)  # onion 
# (the value was chosen by a user from the given options)

print(args.ingredient_3)  # None
# (the value wasn't provided by a user)

import argparse


parser = argparse.ArgumentParser(description="This program prints recipes \
consisting of the ingredients you provide.")

parser.add_argument("-i1", "--ingredient_1", choices=["pasta", "rice", "potato",
                    "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                    help="You need to choose only one ingredient from the list.")
parser.add_argument("-i2", "--ingredient_2", choices=["pasta", "rice", "potato",
                    "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                    help="You need to choose only one ingredient from the list.")
parser.add_argument("-i3", "--ingredient_3", choices=["pasta", "rice", "potato",
                    "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                    help="You need to choose only one ingredient from the list.")
parser.add_argument("-i4", "--ingredient_4", choices=["pasta", "rice", "potato",
                    "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                    help="You need to choose only one ingredient from the list.")
parser.add_argument("-i5", "--ingredient_5", choices=["pasta", "rice", "potato",
                    "onion", "garlic", "carrot", "soy_sauce", "tomato_sauce"],
                    help="You need to choose only one ingredient from the list.")

parser.add_argument("--salt", action="store_true",
                    help="Specify if you'd like to use salt in your recipe.")
parser.add_argument("--pepper", default="False",
                    help="Change to 'True' if you'd like to use pepper in your recipe.")

args = parser.parse_args()

ingredients = [args.ingredient_1, args.ingredient_2, args.ingredient_3,
               args.ingredient_4, args.ingredient_5]
if args.salt:
    ingredients.append("salt")
if args.pepper == "True":
    ingredients.append("pepper")

print(f"The ingredients you provided are: {ingredients}")


def find_a_recipe(ingredients):
    ...
    # processes the input and returns a recipe depending on the provided ingredients

python recipe_book.py -i1 rice -i2 onion -i3 garlic -i4 carrot -i5 tomato_sauce --salt
# The ingredients you provided are: ['rice', 'onion', 'garlic', 'carrot', 'tomato_sauce', 'salt']
# <The description of the available recipe>

python recipe_book.py -i1=pasta -i2=garlic -i3=tomato_sauce --salt --pepper="True"
# The ingredients you provided are: ['pasta', 'garlic', 'tomato_sauce', None, None, 'salt', 'pepper']
# <The description of the available recipe>

python recipe_book.py -i1 bread -i2 onion -i3 garlic -i4 carrot -i5 tomato_sauce --salt
# usage: recipe_book.py [-h]
#                       [-i1 {pasta,rice,potato,onion,garlic,carrot,soy_sauce,tomato_sauce}]
#                       [-i2 {pasta,rice,potato,onion,garlic,carrot,soy_sauce,tomato_sauce}]
#                       [-i3 {pasta,rice,potato,onion,garlic,carrot,soy_sauce,tomato_sauce}]
#                       [-i4 {pasta,rice,potato,onion,garlic,carrot,soy_sauce,tomato_sauce}]
#                       [-i5 {pasta,rice,potato,onion,garlic,carrot,soy_sauce,tomato_sauce}]
#                       [--salt] [--pepper PEPPER]
# recipe_book.py: error: argument -i1/--ingredient_1: invalid choice: 'bread'
# (choose from 'pasta', 'rice', 'potato', 'onion', 'garlic', 'carrot', 'soy_sauce', 'tomato_sauce')