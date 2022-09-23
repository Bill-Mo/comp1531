

if __name__ =='__main__':
    key = input('Key: ')
    message = input('Message: ')
    a = 0
    second = ''
    itself = 0
    decoded_key = {}
    for letter in key:
        is_second = 'second ' + letter
        if second != is_second: 
            decoded_key[letter] = 0
        for compared in key:
            if compared != key[itself]:
                if letter == compared:
                    second = 'second ' + letter
                    decoded_key[second] = 0
                    
                if letter > compared:
                    if is_second ==
                    decoded_key[letter] += 1
        itself += 1
                    
    print(decoded_key)
