import random

colors = {
    "червоний": "теплий",
    "синій": "холодний",
    "зелений": "холодний",
    "жовтий": "теплий",
    "фіолетовий": "холодний"
}

secret = random.choice(list(colors.keys()))
attempts = 3

while attempts > 0:
    guess = input("Вгадайте колір (червоний, синій, зелений, жовтий, фіолетовий): ").strip().lower()

    if guess == secret:
        print("Вітаємо! Ви вгадали колір.")
        break

    print(f"Невірно. Колір належить до {colors[secret]} кольорів. Залишилось спроб: {attempts - 1}")

    attempts -= 1

if attempts == 0:
    print(f"Ви програли! Загаданий колір був {secret}.")
