import random


def print_params(banan, apple):
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    number1 = random.choice(list)
    list.remove(number1)
    number2 = random.choice(list)
    print(banan, apple)
    return number1, number2


number1, number2 = print_params('banan', 'apple')
print(number1, number2)
