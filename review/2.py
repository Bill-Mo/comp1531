l = input('enter numbers').split()
positive = []
for num in l:
    if int(num) > 0:
        positive.append(int(num))
avg = sum(positive)/len(positive)
print(avg)