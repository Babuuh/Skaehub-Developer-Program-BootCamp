import random 

number = random.randrange(1, 100)
guess = 'wrong'
print(number)
while guess:
    answer = int(input('Enter a number between 0 and 100: '))

    try:
        value = int(answer)
    except ValueError:
        print('Invalid integer. Try agin: ')
        continue
    value = int(answer)

    if value < number:
         print('try a higher value')

    elif value > number:
        print('try a lower value')

    else:
        print(str(number)+ ' is the correct number')

        guess = 'correct'