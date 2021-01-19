"""
An application that calculates a user Body Mass Index (BMI) using their weight in kg and height in metres
"""
print("Weight input should be in 'kg' while Height should be in 'm'")

weight = float(input('Weight: '))
height = float(input('Height: '))

bmi = round(weight / height ** 2)

print(f'BMI Result: {bmi}')
