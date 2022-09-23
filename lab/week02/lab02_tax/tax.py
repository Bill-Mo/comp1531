income = int(input('Enter your income: '))
if 0 <= income <= 18200:
    tax = 0
if 18201 <= income <= 37000:
    tax = 0.19 * (income - 18200)
if 37001 <= income <= 87000:
    tax = 3572 + 0.325 * (income - 37000)
if 87001 <= income <= 180000:
    tax = 19822 + 0.37 * (income - 87000)
if 180001 <= income:
    tax = 54232 + 0.45 * (income - 180000)

tax = '{:,.2f}'.format(tax)
print('The estimated tax on your income is ' + '$' + tax)
#print('The estimated tax on your income is ' + '%.2f'%tax)
