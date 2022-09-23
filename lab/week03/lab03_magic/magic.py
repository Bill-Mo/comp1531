def magic(square):
    for rows in square:
        for compared in square:
            if len(rows) != len(compared):
                return 'Invalid data: missing or repeated number'
    if len(square) != len(square[0]):
        return 'Invalid data: missing or repeated number'
        
    for rows in square:
        for nums in rows:
            myself = 0
            for compared in square:
                for cnums in compared:
                    if nums == cnums:
                        myself += 1
            if myself > 1:
                return 'Invalid data: missing or repeated number'
                
    magic_number = sum(square[0])
    for rows in square:
        if sum(rows) != magic_number:
            return 'Not a magic square'
    for cols in range(len(square)):
        test_number = 0
        for rows in square:
            test_number += rows[cols]
        if test_number != magic_number:
            return 'Not a magic square'
    test_number = 0
    for rows in range(len(square)):
        test_number += square[rows][rows]
    if test_number != magic_number:
        return 'Not a magic square'
    test_number = 0
    for rows in range(len(square)):
        test_number += square[rows - len(square)][rows]
    if test_number != magic_number:
        return 'Not a magic square'
        
    return 'Magic square'
    
