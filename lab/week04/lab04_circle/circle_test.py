from circle import Circle

def test_small():
    c = Circle(3)
    assert(round(c.circumference(), 1) == 18.8)
    assert(round(c.area(), 1) == 28.3)
    
def test_big():
    c = Circle(5000)
    assert(round(c.circumference(), 3) == 31415.927)
    assert(round(c.area(), 3) == 78539816.34)
