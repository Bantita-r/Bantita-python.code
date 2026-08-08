"""Assignment 2.1: โปรแกรมเพื่อการตรวจสอบผลการสอบ (exam-score.py)

ให้รับคะแนนสอบของนักเรียนจำนวน 5 คนเก็บไว้ในตัวแปรชนิด list จากนั้นให้ตรวจสอบคะแนนของนักเรียนแต่ละคนว่าผ่านหรือไม่ผ่าน โดยกำหนดว่าคะแนน 50 คะแนนขึ้นไปถือว่าผ่าน

กระบวนการทำงาน
รับคะแนน 5 ค่า เก็บคะแนนทั้งหมดไว้ใน list (เก็บคะแนนทั้งหมดก่อนค่อยไปตรวจสอบ)
ใช้ loop ตรวจสอบคะแนนทีละค่า (ใช้ "for" loop วน เพื่อการตรวจสอบ)
ใช้ condition (if-else) แสดงผลว่า “ผ่าน” หรือ “ไม่ผ่าน”"""

scores = []
for i in range(1, 6):
    score = int(input(f"Enter score of student {i}: "))
    scores.append(score)

print()

for i in range(len(scores)):
    if scores[i] >= 50:
        result = "ผ่าน"
    else:
        result = "ไม่ผ่าน"
        
    print(f"Student {i + 1}: {scores[i]} -> {result}")