def generate_number(i):
    return (i * (3 + i)) * (1 if i % 2 == 0 else -1)

def calc(num):
    ret_str = ""

    nums = []
    for i in range(num):
        nums.append(generate_number(i))

    middle_index = int(num/2 - 0.5)
    middle = nums[middle_index]

    min_num, max_num = 0, 0

    for i in nums:
        if i < min_num:
            min_num = i
        if i > max_num:
            max_num = i

    string = 0
    for i in nums:
        string += i

    ret_str += "Middle item: " + str(middle) + "\n" + "Min item: " + str(min_num) + "\n" + "Max item: " + str(max_num) + "\n" + "Sum: " + str(string) + "\n"
    
    return ret_str

if   __name__ == '__main__':
    number = int(input())
    res = calc(number)
    print(res)
