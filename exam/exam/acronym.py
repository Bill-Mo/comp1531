def acronym_make(inputs):
    if len(inputs) == 0:
        raise ValueError()
    l = []
    for strings in inputs:
        capital = ''
        for word in strings.split():
            word = word.capitalize()
            if word[0] not in 'AEIOU':
                capital += word[0]
        if len(capital) >= 10:
            l.append('N/A')
        elif capital != '':
            l.append(capital)
    return l
