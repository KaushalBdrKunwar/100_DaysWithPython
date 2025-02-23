# BMI Calculator Project
weight = float(input("Enter your weight in kgs: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are Underweight.")
elif 18.5 <= bmi < 24.9:
    print("You are Healthy.")
elif 25.0 <= bmi < 29.9:
    print("You are Overweight.")
elif 30.0 <= bmi < 34.9:
    print("You have Class 1 Obesity.")
elif 35.0 <= bmi < 39.9:
    print("You have Class 2 Obesity.")
else:  # Covers bmi >= 40.0
    print("You have Class 3 Obesity.")
