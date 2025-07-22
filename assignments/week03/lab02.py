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
           print("Your balance is:", balance)

       if choice == "2":
           amount = float(input("Enter amount to withdraw: "))
           if amount < 0:
               print("Can not withdraw less than 0")
               balance =  balance - amount
               print("Withdraw successful. New balance:", balance)
           
       if choice == "3":
           amount = float(input("Enter amount to deposit: "))
           if amount < 0:
               print("Can not withdraw less than 0")
           balance = balance + amount
           print("Deposit successful. New balance:", balance)

       if choice == "4":
           break
       else:
           print("Please select 1-4 only!!")
           continue
else:
   print("Incorrect PIN.")