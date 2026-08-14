"""
โจทย์: เขียน Function แปลงหน่วยสกุลเงินจาก THB ไปเป็นสกุลเงินต่างประเทศ
โดยกำหนดอัตราแลกเปลี่ยนคร่าวๆ ดังนี้:
- 1 USD = 30 THB
- 1 JPY = 0.30 THB

โดยใช้ชื่อฟังก์ชันและการเรียกใช้งานรูปแบบนี้:
convert_currency(100, "USD")

แสดงผลลัพธ์ออกทางหน้าจอ เช่น:
100 THB = 3.33 USD

พร้อมทั้งเขียนโค้ดทดสอบการใช้งานฟังก์ชันที่เขียนขึ้นด้วย
"""

def convert_currency(amount, currency):
    # กำหนดอัตราแลกเปลี่ยนเทียบกับบาท (THB)
    if currency.upper() == "USD":
        rate = 30.0
        converted_amount = amount / rate
        print(f"{amount} THB = {converted_amount:.2f} USD")
        
    elif currency.upper() == "JPY":
        rate = 0.30
        converted_amount = amount / rate
        print(f"{amount} THB = {converted_amount:.2f} JPY")
        
    else:
        print(f"ขออภัย ไม่รองรับสกุลเงิน {currency}")


convert_currency(100, "USD")
convert_currency(100, "JPY")
convert_currency(500, "EUR") 