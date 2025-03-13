print("1")
text_pass = "password wordpass 1111 2222 3333"
password = input("Input password: ")
if password in text_pass:
    print("Welcome!")
else:
    print("Wrong password!")
print("3")
score = int(input("Введіть вашу оцінку: "))

if 90 <= score <= 100:
    print("Ваша оцінка: A")
elif 82 <= score <= 89:
    print("Ваша оцінка: B")
elif 74 <= score <= 81:
    print("Ваша оцінка: C")
elif 64 <= score <= 73:
    print("Ваша оцінка: D")
elif 60 <= score <= 63:
    print("Ваша оцінка: E")
elif 35 <= score <= 59:
    print("Ваша оцінка: FX")
elif 0 <= score <= 34:
    print("Ваша оцінка: F")
else:
    print("Некоректна оцінка! Введіть число від 0 до 100.")

print("Завдання 3 знаходження найменшого з двох чисел")

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
print(f"Найменше число: {min(a, b)}")

print("Завдання 4 Знаходження найбільшого з трьох чисел")

a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))
print(f"Найбільше число: {max(a, b, c)}")

print("Завдання 5 Перевірка числа на позитивність, негативність або нуль")
x = int(input("Введіть число: "))
if x > 0:
    print("Число додатнє")
elif x < 0:
    print("Число від'ємне")
else:
    print("Число дорівнює нулю")

print(" Завдання 6 Визначення парності числа")

x = int(input("Введіть число: "))
if x % 2 == 0:
    print("Число парне")
else:
    print("Число непарне")

print(" Завдання 7 Визначення дня тижня за числом")
days = {
    1: "Понеділок",
    2: "Вівторок",
    3: "Середа",
    4: "Четвер",
    5: "П'ятниця",
    6: "Субота",
    7: "Неділя"
}
day = int(input("Введіть число від 1 до 7: "))
print(days.get(day, "Невірне число"))

print(" Завдання 8* Обмінний пункт валюти")
usd = 42
euro = 44
try:
    money = float(input("Введіть суму, яку ви бажаєте обміняти: "))
    currency = int(input("Вкажіть код валюти (долар - 400, євро - 401): "))
    if currency == 400:
        print(f"Ви отримаєте {money / usd:.2f} доларів")
    elif currency == 401:
        print(f"Ви отримаєте {money / euro:.2f} євро")
    else:
        print("Невірний код валюти")
except ValueError:
    print("Помилка! Введіть числове значення.")

