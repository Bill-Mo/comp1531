weight = float(input('What is your weight in kg? '))
height = float(input('What is your height in m? '))
BMI = round(weight / (height ** 2), 1)
print('Your BMI is ' + str(BMI))
