import pickle

def most_common():
    f = open('shapecolour.p', 'rb')
    item = pickle.load(f)
    count = {}
    for d in item:
        key = d['shape'] + ' ' + d['colour']
        if (key) not in count:
            count[key] = 0
        count[key] += 1
    f.close()
    common = ''
    most = 0
    for pair in count:
        if count[pair] > most:
            most = count[pair]
            common = pair
    result = common.split(' ')
    return {'Colour': result[1], 'Shape': result[0], }

(most_common())
