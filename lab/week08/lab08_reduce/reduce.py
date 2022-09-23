def reduce(f, xs):
    if len(xs) == 0:
        return None
    if len(xs) == 1:
        return xs[0]
    a, b = xs[0], xs[1]
    xs.pop(0)
    return doRecude(f, a, b, xs)

def doRecude(f, a, b, xs):
    print(a, b, xs)
    if len(xs) == 0 or len(xs) == 1:
        return f(a, b)
    xs.pop(0)
    return doRecude(f, f(a, b), xs[0], xs)
