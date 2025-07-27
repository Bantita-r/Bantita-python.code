"""
Personal Finance Calculator
Student: Bantita Rattanajutamanee
Date: 26/07/2025
Purpose: Calculate monthly budget and savings
"""
#ข้อมูลรายได้และค่าใช้จ่ายจากผู้ใช้
monthly_income = float(input("Enter your monthly income (THB): "))
rent_cost = float(input("Enter your monthly rent/housing cost (THB): "))
food_budget = int(input("Enter your monthly food budget (THB): "))
transportation_cost = float(input("Enter your monthly transportation cost (THB): "))
entertainment_budget = int(input("Enter your monthly entertainment budget (THB): "))
emergency_fund_percent = float(input("Enter emergency fund percentage (e.g., 10.5): "))
investment_percent = float(input("Enter investment percentage (e.g., 15.0): "))

# คำนวณค่าใช้จ่ายคงที่ 
fixed_expenses = rent_cost + transportation_cost

# คำนวณค่าใช้จ่ายไม่คงที่
variable_expenses = food_budget + entertainment_budget

# ค่าใช้จ่ายรวมทั้งหมด
total_expenses = fixed_expenses + variable_expenses

# รายได้ที่เหลือหลังจากที่หักค่าใช้จ่ายแล้ว
remaining_income = monthly_income - total_expenses

# เงินไว้ใช้เผื่อฉุกเฉิน
emergency_fund_amount = monthly_income * (emergency_fund_percent / 100)

# เงินไว้ใช้ลงทุน
investment_amount = monthly_income * (investment_percent / 100)

# เงินที่เหลือไว้เก็บออม
available_for_savings = remaining_income - emergency_fund_amount - investment_amount

# คำนวณหาสัดส่วนค่าใช้จ่ายต่อรายได้
expense_ratio = (total_expenses / monthly_income) * 100

# แสดงผลลัพธ์ออกมา
print("\n=== MONTHLY BUDGET REPORT ===")
print(f"Income: {monthly_income:.2f} THB")
print(f"Fixed Expenses: {fixed_expenses:.2f} THB")
print(f"Variable Expenses: {variable_expenses:.2f} THB")
print(f"Total Expenses: {total_expenses:.2f} THB")
print(f"Remaining: {remaining_income:.2f} THB")

print("\n=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund ({emergency_fund_percent}%): {emergency_fund_amount:.2f} THB")
print(f"Investment ({investment_percent}%): {investment_amount:.2f} THB")
print(f"Available for Savings: {available_for_savings:.2f} THB")

print("\n=== ANALYSIS ===")
print(f"Expense Ratio: {expense_ratio:.2f}%")