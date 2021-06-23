number = int(input('Enter a posive integer: '))

def is_power_of_four(number):

    if (number < 0):
        print('No negative numbers')

    else:
        if ( number == 0):
            return False
        
        while( number != 1):
            if ( number % 4 != 0):
                return False
            number = number // 4
            
        return True



print(is_power_of_four(number))