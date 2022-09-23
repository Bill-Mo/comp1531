num = input("Enter a number: ")
is_num = False
while not is_num:
    try:
        print(int(num) * int(num))
        is_num = True
    except ValueError:
        print('error')
        num = input("Enter a number: ")