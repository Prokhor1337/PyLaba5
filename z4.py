import random

secret = str(random.randint(1000, 9999))
attempts = 5

while attempts > 0:
    guess = input("Введіть 4-значний PIN-код: ")

    if guess == secret:
        print("Вітаємо! Ви вгадали PIN-код.")
        break

    correct_digits = sum(1 for a, b in zip(secret, guess) if a == b)
    print(f"Невірно. Правильних цифр на місці: {correct_digits}. Залишилось спроб: {attempts - 1}")

    attempts -= 1

if attempts == 0:
    print(f"Ви програли! PIN-код був {secret}.")
