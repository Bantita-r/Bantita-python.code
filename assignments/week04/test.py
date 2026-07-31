# รับชื่อจริง (หรือข้อความ)จากผู้ใช้
# นับจำนวนสระทั้งหมดในข้อความนั้นว่ามีกี่ตัว(a,e,i,o,u)
 
# ตัวอย่างหน้าจอ
# What is your name? : Bantita
# Your text have 3 vowels

# รับชื่อจริง (หรือข้อความ)จากผู้ใช้
# นับจำนวนสระทั้งหมดในข้อความนั้นว่ามีกี่ตัว(a,e,i,o,u)

# ตัวอย่างหน้าจอ
# What is your name? : Bantita
# Your text have 3 vowels

name = input("What is your name? : ")
letters = list(name)

a = letters.count('a')
e = letters.count('e')
i = letters.count('i')
o = letters.count('o')
u = letters.count('u')

A = letters.count('A')
E = letters.count('E')
I = letters.count('I')
O = letters.count('O')
U = letters.count('U')

# Bantita

count = 0
for letters in name:
    if letters == 'a' or letters == 'A':
        count = count + 1
    elif letters == 'e' or letters == 'E':
        count = count + 1
    elif letters == 'i' or letters == 'I':
        count = count + 1
    elif letters == 'o' or letters == 'O':
        count = count + 1
    elif letters == 'u' or letters == 'U':
        count = count + 1

print(f"Your text have {count} vowels")