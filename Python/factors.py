# Write your code here :-)
import math
num = input("Factorize a number:")
try:
    num = int(num)
    half = math.ceil(num/2)
    count = 2
    factors = [num,1]
    for i in range(2,half+1):
        if num % i == 0:
            count += 1
            factors.append(i)
    if count == 2:
        print(f'{num} is prime')

    else:
        print(f'There are {count} factors of {num}, they are: \n{sorted(factors)}')
except:
    print("Not a number")
#try:

#except:
#    print(f"unexpted {type(num)} in bagging area")
