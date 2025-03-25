import random

secret = random.randint(1, 10)

while True:
    guess = int(input("Вгадайте число від 1 до 10: "))
    if guess < secret:
        print("Більше!")
    elif guess > secret:
        print("Менше!")
    else:
        print("Вітаємо! Ви вгадали число.")
        break
