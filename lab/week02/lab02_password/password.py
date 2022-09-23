def check_password(password):
    '''
    Takes in a password, and returns a string based on the strength of that password.

    The returned value should be:
    * "Strong password", if at least 12 characters, contains at least one number, at least one uppercase letter, at least one lowercase letter.
    * "Moderate password", if at least 8 characters, contains at least one number.
    * "Poor password", for anything else
    * "Horrible password", if the user enters "password", "iloveyou", or "123456"
    '''
    characters = 0
    lowercase = 0
    uppercase = 0
    number = 0
    for letter in password:
        number += 1
        if letter.islower():
            lowercase += 1
        elif letter.isupper():
            uppercase += 1
        elif letter.isdigit():
            number += 1
        else:
            characters += 1
    
    characters = characters + lowercase + uppercase + number
    if password == 'password' or password == 'iloveyou' or password == '123456':
        return 'Horrible password'
    elif characters >= 12 and number >= 1 and uppercase >= 1 and lowercase >= 1:
        return 'Strong password'
    elif characters >= 8 and number >= 1:
        return 'Moderate password'
    else:
        return 'Poor password'

if __name__ == '__main__':
    print(check_password("ihearttrimesters"))
    # What does this do?
