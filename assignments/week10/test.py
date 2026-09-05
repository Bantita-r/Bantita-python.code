# 1. รับค่า text จากผู้ใช้
# 2. รับค่าอักขระที่ต้องการค้นหาจากผู้ใช้
# 3. แสดงผลจำนวนของอักขระในข้อความ text

# ตัวอย่างหน้าจอ
# Insert your text: Bantita Rattanajutamanee
# Character to find: a
# 6 letters 'a' found in 'Bantita Rattanajutamanee'

text = input("Insert your text: ")
char_to_find = input("Character to find: ")

count = 0
for char in text:
    if char == char_to_find:
        count += 1

print(f"{count} letters '{char_to_find}' found in '{text}'")