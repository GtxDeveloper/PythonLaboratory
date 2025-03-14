# Завдання 1: Підрахунок кількості входжень елемента у кортежі
def count_occurrences(tup, element):
    return tup.count(element)

# Завдання 2: Знаходження індексу елемента у кортежі
def find_index(tup, element):
    return tup.index(element) if element in tup else -1

# Завдання 3: Отримання кортежу з першим і останнім елементом
def first_last_tuple(tup):
    return (tup[0], tup[-1]) if tup else ()

# Завдання 4: Перевірка, чи всі елементи однакові
def all_equal(tup):
    return len(set(tup)) == 1

# Завдання 5: Обчислення суми всіх числових елементів, включаючи рядкові числа
def sum_numeric(*args):
    return sum(int(x) for x in args if isinstance(x, (int, float)) or (isinstance(x, str) and x.isdigit()))

# Завдання 6: Зміна останнього елемента у вкладених кортежах
def replace_last(lst, number):
    return [t[:-1] + (number,) for t in lst]

# Завдання 7: Підрахунок частоти появи годин у файлі mbox-short.txt
def count_hours(filename="mbox-short.txt"):
    with open(filename, "r", encoding="utf-8") as file:
        hour_count = {}
        for line in file:
            if line.startswith("From "):
                words = line.split()
                time = words[5]
                hour = time.split(":")[0]
                hour_count[hour] = hour_count.get(hour, 0) + 1
        return sorted(hour_count.items())

# Завдання 8: Підрахунок загальної відстані польоту дрона
def total_distance(route, points):
    total = 0
    for i in range(len(route) - 1):
        key = tuple(sorted((route[i], route[i+1])))
        total += points.get(key, 0)
    return total

# 1: Підрахунок входжень
print(count_occurrences((1, 2, 3, 2, 4, 2, 5), 2))

# 2: Пошук індексу
print(find_index((10, 20, 30, 40, 50), 30))

# 3: Перший і останній елементи
print(first_last_tuple((5, 10, 15, 20, 25)))

# 4: Чи всі елементи однакові?
print(all_equal((7, 7, 7, 7)))

# 5: Сума числових елементів
print(sum_numeric(10, 20, 'a', '30', 'bcd'))

# 6: Зміна останнього елемента у вкладених кортежах
print(replace_last([(10, 20, 40), (40, 50, 60), (70, 80, 90)], 100))

# 7: Підрахунок частоти появи годин у файлі
print(count_hours())

# 8: Підрахунок відстані польоту
points = {(0, 1): 2, (0, 2): 3.8, (0, 3): 2.7, (1, 2): 2.5, (1, 3): 4.1, (2, 3): 3.9}
route = [0, 1, 3, 2, 0]
print(total_distance(route, points))
