import random

# Завдання 1
print(" ".join(str(2**i) for i in range(10)))

# Завдання 2
num = int(input("Введіть чотиризначне число: "))
print("Сума цифр:", sum(int(digit) for digit in str(num)))

# Завдання 3
sum_numbers = 0
while True:
    num = int(input("Введіть число: "))
    if num < 0:
        break
    sum_numbers += num
print("Сума додатних чисел:", sum_numbers)

# Завдання 4
numbers = []
while True:
    num = int(input("Введіть число: "))
    if num == 0:
        break
    numbers.append(num)
print("Середнє значення:", sum(numbers)/len(numbers) if numbers else 0)

# Завдання 5
word = input("Введіть текст: ")
vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ"
print("Результат:", "".join([ch for ch in word if ch not in vowels]))

# Завдання 6
number = 0
while True:
    age = input("Введіть ваш вік або 'exit' для виходу: ")
    if age.lower() == 'exit':
        break
    age = int(age)
    number += 1
    if age < 3:
        print("Квиток безкоштовний")
    elif age <= 12:
        print("Квиток коштує 50 грн")
    else:
        print("Квиток коштує 80 грн")

# Завдання 7*
secret_number = random.randint(1, 100)
while True:
    answer = input("Вгадайте число або введіть 'exit' для виходу: ")
    if answer.lower() == 'exit':
        print("Гра завершена")
        break
    if not answer.isdigit():
        print("Будь ласка, введіть число")
        continue
    answer = int(answer)
    if answer < secret_number:
        print("Число більше")
    elif answer > secret_number:
        print("Число менше")
    else:
        print("Ви вгадали!")
        break
