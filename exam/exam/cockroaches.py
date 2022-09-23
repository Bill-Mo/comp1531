def decontaminate(filenames):
    d = {}
    for f in filenames:
        with open(f, 'r') as FILE:
            line = FILE.readline()[:-1]
            while line != '':
                print(line)
                if line not in d:
                    d[line] = 1
                else:
                    d[line] += 1
                line = FILE.readline()[:-1]
    return d
