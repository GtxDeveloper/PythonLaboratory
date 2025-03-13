import os


def task_1():
    print("1")
    with open("name_surname.txt", "w") as file:
        file.write("Ім'я Прізвище")
    print("=================================================================")

def task_2():
    print("2")
    filename = "user_input.txt"
    lines = []
    while True:
        line = input("Введіть рядок (або натисніть Enter для завершення): ")
        if line == "":
            break
        lines.append(line)
    with open(filename, "w") as file:
        file.write("\n".join(lines))
    print(f"Кількість рядків: {len(lines)}")
    print(f"Кількість символів: {sum(len(line) for line in lines)}")
    print("=================================================================")

def task_3():
    print("3")
    with open("poetry.txt", "r") as file:
        lines = file.readlines()
    count_not_T = sum(1 for line in lines if not line.startswith("T"))
    count_ends_d = sum(1 for line in lines if line.rstrip().endswith("d"))
    words_capital = sum(1 for line in lines for word in line.split() if word.istitle())
    print(f"Рядки, що не починаються з 'T': {count_not_T}")
    print(f"Рядки, що закінчуються на 'd': {count_ends_d}")
    print(f"Слова з великої літери: {words_capital}")
    print("=================================================================")

def task_4():
    print("4")
    with open("mbox-short.txt", "r") as file:
        lines = file.readlines()
    max_word = ""
    for line in lines:
        print(f"{len(line.strip())} символів у рядку")
        words = line.split()
        for word in words:
            if len(word) > len(max_word):
                max_word = word
    print(f"Найдовше слово: {max_word}")
    print("=================================================================")

def task_5():
    print("5")
    with open("mbox-short.txt", "r") as file:
        for line in file:
            print(line.strip().upper())
    print("=================================================================")

def task_6():
    print("6")
    with open("mbox-short.txt", "r") as file:
        lines_with_at = [line.strip() for line in file if "@" in line]
    for line in lines_with_at:
        print(line)
    print(f"Кількість рядків з '@': {len(lines_with_at)}")
    print("=================================================================")

def task_7():
    print("7")
    with open("feedback.txt", "r") as file:
        lines = file.readlines()

    positive, negative = [], []
    for line in lines:
        if line.startswith("Positive:"):
            positive.append(line)
        elif line.startswith("Negative:"):
            negative.append(line)

    with open("positive.txt", "w") as pos_file:
        pos_file.writelines(positive)
    with open("negative.txt", "w") as neg_file:
        neg_file.writelines(negative)

    with open("feedback_analysis.txt", "w") as analysis_file:
        analysis_file.write(f"Total feedbacks: {len(lines)}\n")
        analysis_file.write(f"Count of positive feedbacks: {len(positive)}\n")
        analysis_file.write(f"Count of negative feedbacks: {len(negative)}\n")

    print("Аналіз завершено, результати збережено у файли.")
    print("=================================================================")

task_1()
task_2()
task_3()
task_4()
task_5()
task_6()
task_7()
