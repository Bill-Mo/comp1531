def reverse_words(string_list):
    '''
    Given a list of strings, return a new list where the order of the words is
    reversed
    '''
    newList = []
    for string in string_list:
        words = string.split()
        words.reverse()
        words = ' '.join(words)
        newList.append(words)
    return newList

if __name__ == "__main__":
    print(reverse_words(["Hello World", "I am here"]))
    # it should print ['World Hello', 'here am I']
