import random

secret = random.randint(1, 20)
attempts = 3

while attempts > 0:
    guess = int(input(f"Вгадайте число від 1 до 20. Залишилось спроб: {attempts}: "))

    if guess == secret:
        print("Вітаємо! Ви вгадали число.")
        break

    attempts -= 1

if attempts == 0:
    print(f"Ви програли! Загадане число було {secret}.")
