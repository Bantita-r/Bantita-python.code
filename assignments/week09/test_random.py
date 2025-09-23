import random

#refactor != debug

def test_random():
    #สุ่มเลขระหว่าง1-10 เก็บไว้ในตัวเเปรชื่อrandom_number
    random_number = random.randint(1, 100)

    #รับค่าการทายเลขจากผู้ใช้ เก็บไว้ในตัวแปรชื่อ gurss_number
    guess_number = input("What is your guess number?: ")
    #guess_number = int(guess_number)จะเขียนแบบนี้ก็ได้

    if random_number == guess_number:
        print("Congratulation")

    elif random_number < guess_number:
        print("Too much")

    elif random_number > guess_number:
        print("Too low")

    print(random_number)
    
test_random()