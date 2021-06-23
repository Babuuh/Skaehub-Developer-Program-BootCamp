from math import sqrt

number = int(input('Enter a number: '))

def is_perfect_square(number):
    root = sqrt(number)

    if ((root + 0.5) ** 2 == number):
        return str(number) + ' is a perfect square'

    else:
        return str(number) + ' is not a perfect square'

print(is_perfect_square(number))