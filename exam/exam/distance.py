def longest_distance(elements):
    l = []
    distance = 0
    longest = 0
    for idx, num in enumerate(elements):
        if num not in l:
            l.append(num)
        else:
            start = 0
            is_found = False
            while start < len(elements) and not is_found:
                if elements[start] == num:
                    distance = idx - start
                    longest = max(distance, longest)
                    is_found = True
                start += 1
    return longest
