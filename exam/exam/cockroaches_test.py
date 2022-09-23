from cockroaches import decontaminate

def generate_files(cockroaches):
    '''
    Input Parameters:

    - cockroaches        a dictionary of the form

    {
        'monday.txt': ['kitchen', 'attic', 'bathroom']
        'tuesday.txt': ['kitchen', 'bedroom', 'backyaard'], etc
    }
    '''
    for filename in cockroaches:
        with open(filename, 'w') as FILE:
            for room in cockroaches[filename]:
                FILE.write(room + '\n')

def test_sample():
    d = {
        'monday.txt': ['kitchen', 'attic', 'bathroom'], 
        'tuesday.txt': ['kitchen', 'bedroom', 'backyard', 'attic'], 
        'wednesday.txt': ['attic', 'bathroom'], 
        }
    generate_files(d)

    assert(decontaminate(['monday.txt', 'tuesday.txt', 'wednesday.txt']) == { 'kitchen': 2, 'attic': 3, 'bathroom': 2, 'bedroom': 1, 'backyard': 1 })
