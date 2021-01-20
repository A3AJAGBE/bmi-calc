"""
An application that calculates a user Body Mass Index (BMI) using their weight in kg and height in metres
"""
print("Weight input should be in 'kg' while Height should be in 'm'\n")

weight = float(input('Weight: '))
height = float(input('Height: '))

bmi = round(weight / height ** 2)

# Interpreting the bmi result

if bmi < 18.5:
    print(f"BMI Result: {bmi}, you are underweight.")
elif bmi < 25:
    print(f"BMI Result: {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"BMI Result: {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"BMI Result: {bmi}, you are obese.")
else:
    print(f"BMI Result: {bmi}, you are clinically obese.")

