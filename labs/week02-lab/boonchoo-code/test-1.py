print("Now try these exercises:")
print()
print("1. Circle Calculator:")
print("   - Ask user for radius")
print("   - Calculate area (π * r²)")
print("   - Calculate circumference (2 * π * r)") #เส้นรอบรูป
print("   - Use 3.14159 for π")
print()

print("Circle Calculator")

pi = 3.14159

radius = float(input("Enter radius: "))

area = pi * radius * radius
circumference = 2 * pi * radius

print("Area =", area)
print("Circumference =", circumference)


