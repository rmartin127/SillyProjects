# Write your code here :-)
import math

num = input("Factorize a number:")
try:
    num = int(num)
    half = math.ceil(num / 2)
    count = 2
    factors = [num, 1]
    factor_pair = [[1, num]]
    pair_count = 1
    new_pair = [[1,2]]
    for i in range(2, half + 1):
        if num % i == 0:
            count += 1
            factors.append(i)
            if i not in factor_pair:
                factor_pair.append([i, (num // i)])
    factor_half = math.ceil(len(factor_pair) / 2)
    for i in range(0, factor_half):
        new_pair.append(factor_pair[i])
    if count == 2:
        print(f"{num} is prime")
    else:
        print(
            f"There are {count} factors of {num}, they are: \n{sorted(factors)} \n{new_pair}"
        )
except:
    print("Not a number")
