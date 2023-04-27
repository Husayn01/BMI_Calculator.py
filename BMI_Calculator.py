#BMI Calculator
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
new_Height = float(height)
new_Weight = int(weight)

bmi = new_Weight / new_Height ** 2
new_Bmi = round(bmi)
if new_Bmi <= 18.5:
    result = "are underweight"
    print(f"Your BMI is {new_Bmi} and you {result}")
elif new_Bmi < 25:
    result = "have anormal weight"
    print(f"Your BMI is {new_Bmi} and you {result}")
elif new_Bmi < 30:
    result = "are overweight"
    print(f"Your BMI is {new_Bmi} and you {result}")
elif new_Bmi < 35:
    result = "are obese"
    print(f"Your BMI is {new_Bmi} and you {result}")
else:
    result = "are clinically obese"
    print(f"Your BMI is {new_Bmi} and you {result}")
