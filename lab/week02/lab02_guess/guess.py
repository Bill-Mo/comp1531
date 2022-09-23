def guess_number(bound):
    return int((bound[0] + bound[1]) / 2)
    
def start_guess(number):
    print('My guess is: ' + str(number))
    guess = input('Is my guess too low (L), too high (H), or correct (C)?\n')
    return guess
    
def determine_guess(guess, bound, number):
    if guess == 'L':
        bound[0] = number
    elif guess =='H':
        bound[1] = number
    else:
        print('Got it!')


if __name__ =='__main__':
    print('Pick a number between 1 and 100 (inclusive)')
    low = 1
    high = 100
    guess = 'DEFAULT'
    bound = [low, high]
    while guess != 'C':
        number = guess_number(bound)
        guess = start_guess(number)
        determine_guess(guess, bound, number)
