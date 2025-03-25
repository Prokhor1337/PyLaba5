import random

secret = random.randint(1, 50)

while True:
    guess = int(input("Вгадайте число від 1 до 50: "))
    diff = abs(secret - guess)

    if guess == secret:
        print("Вітаємо! Ви вгадали число.")
        break
    elif diff <= 3:
        print("Дуже близько!")
    elif diff <= 10:
        print("Близько.")
    else:
        print("Далеко.")
