# Write your code here :-)
isEven = True
import sys
def numberType(int):
    global isEven
    if int % 2 == 0:
        isEven = True
        return isEven
    elif int % 2 == 1:
        isEven = False
        return isEven

def evenMath(int):
    global number
    number = int // 2
    print(number)
    return number

def oddMath(int):
    global number
    number = 3 * int + 1
    print(number)
    return number



while True:
    hops = 0
    print('Welcome to the Collatz Conjecture, where we get to 1 by mathematical means every time, press (q) to exit')
    number = input()
    if number == 'q':
        print('Thank you for playing')
        sys.exit()
    else:
        try:
            number = int(number)
        except ValueError:
            print('Please input a Positive Integer')
            continue
        if number <= 0:
            sys.exit()
        while number != 1:
            numberType(number)
            hops += 1
            if isEven == True:
                evenMath(number)
            else:
                oddMath(number)
        print('It took ' + str(hops) + ' operations to get to 1!')
