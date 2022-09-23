import random

first = random.randint(2,12)
second = random.randint(2,12)
answer = first * second

boolean = 1

while boolean == 1:
    guess = int(input(f"What is {first} x {second}? "))
    if guess == answer:
        print("Correct!")
        boolean = 0
    else:
        print("Incorrect - try again.")
