def generate(n):
    if not isinstance(n, int) or n == 0:
        return []
    
    if n == 1:
        return [0]

    f = [0, 1]
    if n == 2:
        return f
    
    n -= 2
    while (n != 0):
        a = f[-2]
        b = f[-1]
        f.append(a + b)
        n -= 1

    return f
