# BMI = weight(kg)/height(m) ** 2 
print()
weight = input("Please enter your weight in pounds: ")
height = input("Please enter your height in feet: ")
weight = round(float(weight) / 2.2, 2) # rounds to 2 decimal places
height = round(float(height) / 3.281, 2)

bmi=round(weight/height ** 2)
print(f"Your BMI is {bmi}")
if bmi < 18:
    print("You are underweight")
elif bmi < 25:
    print("You are in the normal weight category")
elif bmi < 30:
    print("You are overweight")
elif bmi < 35:
    print("You are obese")
else:
    print("You are severely obese and possibly dead")



