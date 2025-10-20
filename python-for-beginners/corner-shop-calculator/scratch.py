from dataclasses import dataclass

@dataclass
class Cat:
    name: str
    age: int
    breed: str
    tail_length: float

@dataclass
class Dog:
    name: str
    age: int
    breed: str
    barking_volume: float
    is_hunting_breed: bool

def match_animal(animal):
    # Declare a match statement for the passed animal
    match animal:
        case Cat(name=name, age=age, breed=breed, tail_length=20.0):
            print('Any cat with the tail length of 20.0 matches this case! '
                    f'Name is {name}, age is {age}, breed is {breed}')
        case Cat(name="Kitty", age=5, breed=breed, tail_length=tail_length):
            print('Any cat named Kitty of age 5 matches this case! '
                    f'Breed is {breed}, tail length is {tail_length}')
        case Dog(name="Fluffy"):
            print('Any dog named Fluffy matches this case! No need for statistics :)')
        case Dog():
            print('Any dog matches this case!')
        case _:
            print('Every left animal matches this case')