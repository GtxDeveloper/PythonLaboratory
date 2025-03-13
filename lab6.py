for i in range(1, 21):
    print(i)


A = int(input("Введите A: "))
B = int(input("Введите B: "))

if A < B:
    for i in range(A, B + 1):
        print(i)
else:
    for i in range(A, B - 1, -1):
        print(i)


result = 1
for _ in range(10):
    num = int(input("Введите число: "))
    result *= num

print("Произведение чисел:", result)


numbers = [int(input("Введите число: ")) for _ in range(10)]
even_numbers = [num for num in numbers if num % 2 == 0]

print("Четные числа:", even_numbers)


numbers = [int(input("Введите число: ")) for _ in range(10)]
print("Максимальное число:", max(numbers))


text = input("Введите строку: ")
print("".join([text[i] for i in range(len(text)) if i % 2 == 0]))


rows = 5


for i in range(1, rows + 1):
    print("*" * i)


for i in range(rows - 1, 0, -1):
    print("*" * i)




def calculate_profit(amount, percent, period):
    if amount == 0 or percent == 0 or period == 0:
        return 0

    for _ in range(period):
        amount += amount * (percent / 100)

    return round(amount - initial_amount, 2)


initial_amount = float(input("Введите сумму депозита: "))
percent = float(input("Введите процентную ставку: "))
years = int(input("Введите срок в годах: "))

profit = calculate_profit(initial_amount, percent, years)
print("Чистый доход:", profit)



def calculator():
    try:
        first_number = float(input("Введите число: "))
        result = first_number
        last_input_type = "number"

        while True:
            operator = input("Введите оператор (+, -, *, /) или '=' для результата: ")

            if operator == "=":
                print("Результат:", result)
                break

            if operator not in "+-*/":
                print("Ошибка! Некорректный оператор. Попробуйте снова.")
                continue

            if last_input_type == "operator":
                print("Ошибка! Два оператора подряд. Попробуйте снова.")
                continue

            second_number = float(input("Введите число: "))

            if last_input_type == "number":
                if operator == "+":
                    result += second_number
                elif operator == "-":
                    result -= second_number
                elif operator == "*":
                    result *= second_number
                elif operator == "/":
                    if second_number == 0:
                        print("Ошибка! Деление на ноль.")
                        continue
                    result /= second_number

            last_input_type = "operator"

    except ValueError:
        print("Ошибка! Некорректный ввод числа.")


calculator()
