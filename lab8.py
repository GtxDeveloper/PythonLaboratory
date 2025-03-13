import os
import shutil
import random
import struct

def task_1():
    print("1")
    filename = "shopping_list.txt"
    items = []
    while True:
        item = input("Введіть назву продукту (або натисніть Enter для завершення): ")
        if item == "":
            break
        items.append(item)
    with open(filename, "w") as file:
        file.write("\n".join(items))
    print(f"Кількість продуктів у списку: {len(items)}")
    print("==========================================================================================")
def task_2():
    print("2")
    with open("article.txt", "r") as file:
        text = file.read()
    word_count = len(text.split())
    print(f"Кількість слів у файлі: {word_count}")
    print("==========================================================================================")
def task_3():
    print("3")
    with open("log.txt", "r") as file:
        lines = file.readlines()
    error_lines = [line for line in lines if "ERROR" in line]
    with open("errors.txt", "w") as file:
        file.writelines(error_lines)
    print(f"Кількість рядків з 'ERROR': {len(error_lines)}")
    print("==========================================================================================")
def task_4():
    print("4")
    shutil.copy("data.txt", "backup_data.txt")
    print("Файл скопійовано у backup_data.txt")
    print("==========================================================================================")
def task_5():
    print("5")
    with open("report.txt", "r") as file:
        text = file.read()
    fixed_text = text.replace("old", "new")
    with open("report_fixed.txt", "w") as file:
        file.write(fixed_text)
    print("Замінено 'old' на 'new' та збережено у report_fixed.txt")
    print("==========================================================================================")
def task_6():
    print("6")
    with open("reverse.txt", "r") as file:
        lines = file.readlines()
    reversed_lines = [line.strip()[::-1] + "\n" for line in lines]
    with open("reversed.txt", "w") as file:
        file.writelines(reversed_lines)
    print("Файл перевернуто та збережено у reversed.txt")
    print("==========================================================================================")
def task_7():
    print("7")
    filename = "numbers.dat"
    numbers = [random.randint(1, 100) for _ in range(10)]
    with open(filename, "wb") as file:
        file.write(struct.pack("10i", *numbers))
    with open(filename, "rb") as file:
        data = file.read()
        read_numbers = list(struct.unpack("10i", data))
    print(f"Прочитані числа: {read_numbers}")
    print(f"Сума чисел: {sum(read_numbers)}")
    print("==========================================================================================")

task_1()
task_2()
task_3()
task_4()
task_5()
task_6()
task_7()
