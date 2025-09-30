"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""

print("=== PERSONAL INFORMATION VALIDATOR ===")
name = input("Enter your name: ")
age = input("Enter your age: ")
phone = input("Enter your phone number: ")

#name validation 
nameFlag = True
for char in name :
    print(char, char.isalpha())
    if char.isalpha()  or char == "":
        nameFlag == True
    else:
        nameFlag == False

# age  validate
age_Flag = True
if 18 <= age and age <= 65:
    age_Flagr = True
else:
   age_Flag = False

    # phone number validate
    # 10 digits
phoneFlag = True
if  len(phone) != 10:
    pphoneFlag = False
else:
    for char in phone:
        if char.isdigit() == False:
            phoneFlag = False
            break

print("validator Results:")
if nameFlag:
    print("Name : Valid (conrains only letters and spaces)")
else:  
    print("Name: Invalid (not conrains only letter and spaces)")

if ageFlag:
    print(f"Age: Valid ({age}years old)")
else:
    print("Age: Invalid(less than 18 or more than 65)")

if phoneFlag:
    print("Phone: Valid (10-digit number)")
else:
    print("Phone: Invalid (not 10-digit number)")

print("Formatted Information: ")
print("Name:",name.upper())

if int(age) >= 18  and int(age) <=30:
    print(" Age group: Youmg Adult (18-30)")
else:
    print("Age Group : not Young Adult")
print("Phone :",phone_Flag)
 