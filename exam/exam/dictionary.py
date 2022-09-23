def construct_dict(keys, values):
    if len(keys) != len(values):
        raise ValueError()
    d = {}
    i = 0
    for i in range(len(keys)):
        d[keys[i]] = values[i]
    return d
