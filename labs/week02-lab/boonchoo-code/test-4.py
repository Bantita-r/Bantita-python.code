print("4. BMI Calculator:")
print("   - Ask for weight (kg) and height (m)")
print("   - Calculate: BMI = weight / (height ** 2)")
print()

#input
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

#processs
bmi = weight / (height ** 2)
#output
print("BMI = ", bmi)