'''
To find my_min, I used min function. To simplify ways to get products, I imported reduce function and did it in one line. To avoid redundant input step, I did inputting in one line by a for loop.
'''
from functools import reduce

def drykiss(my_list):
    my_min = min(my_list)

    result = (my_min, reduce(mul, [my_list[i] for i in range(0, 4)]), reduce(mul, [my_list[i] for i in range(1, 5)]))
    return result

def mul(x, y):
    return x * y

if __name__ == '__main__':
    my_list = []
    for char in 'abcde':
        my_list.append(int(input(f"Enter {char}: ")))
    result = drykiss(my_list)
    print("Minimum: " + str(result[0]))
    print("Product of first 4 numbers: ")
    print(f"  {result[1]}")
    print("Product of last 4 numbers")
    print(f"  {result[2]}")
