from weather import weather

def test_example():
    assert weather('08-08-2010', 'Albury') == (10.8, -10.0)
    
def test_invalid():
    assert weather('04-16-2009', 'Albury') == (None, None)
    assert weather('11-09-2009', 'Albury') == (None, None)
    assert weather('06-11-2013', 'random') == (None, None)
