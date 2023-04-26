#BMI Calculator
height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
new_Height = float(height)
new_Weight = int(weight)

bmi = new_Weight / new_Height ** 2
new_Bmi = int(bmi)
print(new_Bmi)
 
