import numpy as np

# Завдання 1: Створити вектор з 10 нульових значень з використанням методу .zeros().
vector1 = np.zeros(10)
print("Завдання 1:", vector1)

# Завдання 2: Створити вектор з 10 нульових значень з використанням методу .zeros(). Змінити кожне четверте значення на 5.
vector2 = np.zeros(10)
vector2[3::4] = 5  # Змінюємо кожне 4-те значення на 5
print("Завдання 2:", vector2)

# Завдання 3: Створити вектор, що містить послідовність чисел 25-50 з використанням методу .arange().
vector3 = np.arange(25, 51)
print("Завдання 3:", vector3)

# Завдання 4: Генеруємо матрицю розміром 4x4
matrix = np.random.randint(1, 100, size=(4, 4))

# 1. Елементи першого ряду
first_row = matrix[0]
print("1. Перший ряд:", first_row)

# 2. Елементи другого стовпця
second_column = matrix[:, 1]
print("2. Другий стовпець:", second_column)

# 3. Сума елементів третього ряду
third_row_sum = np.sum(matrix[2])
print("3. Сума елементів третього ряду:", third_row_sum)

# 4. Середнє значення елементів четвертого стовпця
fourth_column_mean = np.mean(matrix[:, 3])
print("4. Середнє значення четвертого стовпця:", fourth_column_mean)

# 5. Мінімальний та максимальний елемент матриці та їх індекси
min_val = np.min(matrix)
max_val = np.max(matrix)
min_index = np.unravel_index(np.argmin(matrix), matrix.shape)
max_index = np.unravel_index(np.argmax(matrix), matrix.shape)
print(f"5. Мінімальний елемент: {min_val} на індексах {min_index}")
print(f"Максимальний елемент: {max_val} на індексах {max_index}")

# 6. Добуток ненульових елементів головної діагоналі
diagonal_product = np.prod(np.diagonal(matrix))
print("6. Добуток ненульових елементів головної діагоналі:", diagonal_product)

# 7. Переставити 2-й та 4-й стовпці місцями
matrix[:, [1, 3]] = matrix[:, [3, 1]]
print("7. Матриця після перестановки стовпців:", matrix)

# Завдання 5: Температурні дані
temperature_data = np.array([
    [-8, -14, -19, -18],  # Станція 1
    [25, 28, 26, 20],      # Станція 2
    [11, 18, 20, 25]       # Станція 3
])

# 1. Вивести температуру на 2-й метеостанції за 4 день
temp_station2_day4 = temperature_data[1, 3]
print("Завдання 5.1: Температура на 2-й метеостанції за 4 день:", temp_station2_day4)

# 2. Вивести показники всіх метеостанцій за 2-й день
temp_all_stations_day2 = temperature_data[:, 1]
print("Завдання 5.2: Показники всіх метеостанцій за 2-й день:", temp_all_stations_day2)

# 3. Середня температура за 4 дні по 3 метеостанції
avg_temp_4_days = np.mean(temperature_data, axis=0)
print("Завдання 5.3: Середня температура за 4 дні по 3 метеостанції:", avg_temp_4_days)

# 4. Вивести в які дні та на яких метеостанціях температура була в діапазоні 24-26 градусів тепла
temp_in_range = np.where((temperature_data >= 24) & (temperature_data <= 26))
print("Завдання 5.4: Дні та метеостанції з температурою в діапазоні 24-26:", temp_in_range)

# Завдання 6: Сортування масиву 2х2 вздовж першої та останньої вісі
array_2x2 = np.array([[4, 2], [7, 5]])
sorted_first_axis = np.sort(array_2x2, axis=0)  # Вдоль першої вісі
sorted_last_axis = np.sort(array_2x2, axis=1)   # Вдоль останньої вісі
print("Завдання 6.1: Сортування вдовж першої вісі:", sorted_first_axis)
print("Завдання 6.2: Сортування вдовж останньої вісі:", sorted_last_axis)

# Завдання 7: Заміна NAN значень середнім значенням іншого масиву
array_with_nan = np.array([1, np.nan, 3, np.nan, 5])
array_for_replacement = np.array([2, 4, 6, 8, 10])
mean_value = np.mean(array_for_replacement)
array_with_nan = np.nan_to_num(array_with_nan, nan=mean_value)
print("Завдання 7: Масив після заміни NAN значень:", array_with_nan)

# Завдання 8: Вивести елементи масиву 4х5, які або більше 6, або кратні 3
array_4x5 = np.random.randint(1, 15, (4, 5))
condition = (array_4x5 >= 6) | (array_4x5 % 3 == 0)
filtered_elements = array_4x5[condition]
print("Завдання 8: Елементи масиву, які більше 6 або кратні 3:", filtered_elements)

# Завдання 9: Перевірка на нульові стовпці в масиві nxn
n = 4
array_nxn = np.random.randint(0, 2, (n, n))  # 0 або 1 в масиві
zero_columns = np.any(array_nxn != 0, axis=0)  # Перевірка чи є ненульові елементи в кожному стовпці
zero_column_indexes = np.where(~zero_columns)[0]  # Пошук стовпців з нулями
print("Завдання 9: Нульові стовпці в масиві:", zero_column_indexes)

# Завдання 10: Сума діагональних елементів масиву
sum_diagonal = np.trace(array_nxn)
print("Завдання 10: Сума діагональних елементів масиву:", sum_diagonal)

# Завдання 11: Заміна знаку елементів в проміжку [10; 20], або множення в 3 рази для [0; 9]
array_for_condition = np.random.randint(0, 30, 10)
modified_array = np.copy(array_for_condition)
modified_array[(modified_array >= 10) & (modified_array <= 20)] = -modified_array[(modified_array >= 10) & (modified_array <= 20)]
modified_array[(modified_array >= 0) & (modified_array < 10)] *= 3
print("Завдання 11: Масив після змін:", modified_array)
