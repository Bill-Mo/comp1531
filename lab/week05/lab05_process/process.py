import json
import operator
import pickle

def process():
    f = open('shapecolour.p', 'rb')
    item = pickle.load(f)
    f.close()
    result = {
        'mostCommon': most_common(), 
        'rawData': item
    }
    fwrite = open('processed.json', 'w')
    fwrite.write(json.dumps(result))
    
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
    return {'colour': result[1], 'shape': result[0], }
