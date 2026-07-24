# Complete this program to classify people by age
age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:
age = int(input("Enter age: "))

if age < 0:
    print("Invalid age")
elif age <= 12:
    print("Child")
elif age <= 19:
    print("Teenager")
elif age <= 59:
    print("Adult")
else:
    print("Senior")


# Complete this ATM simulation
balance = 1000
pin = "1234"

entered_pin = input("Enter PIN: ")
if entered_pin == pin:
    print("PIN accepted")
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit") 
        print("4. Exit")
        
        choice = input("Choose option: ")
        
        if choice == "1":
            print(f"Your balance is: {balance}")
            
        elif choice == "2":
            amount = int(input("Enter amount to withdraw: "))
            if amount > balance:
                print("Insufficient funds!")
            else:
                balance -= amount
                print(f"Withdraw successful. New balance: {balance}")
                
        elif choice == "3":
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print(f"Deposit successful. New balance: {balance}")
            
        elif choice == "4":
            print("Goodbye!")
            break 
            
        else:
            print("Invalid option, please try again.")
        
        
else:
    print("Invalid PIN")
