import re

# Зчитуємо словник
dictionary = {}
with open("dict.txt", "r", encoding="utf-8") as f:
    for line in f:
        eng, ukr = line.strip().split("\t-\t")
        dictionary[eng] = ukr

# Зчитуємо текст для перекладу
with open("translate.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Регулярний вираз для виділення слів + розділових знаків
words = re.findall(r"[\w']+|[.,!?;]", text)

# Перекладаємо кожне слово, якщо є в словнику
translated_words = [dictionary.get(word, word) for word in words]

# Записуємо у файл
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(translated_words))



#2
# Зчитуємо країни та мови
countries = {}
with open("input_countries.txt", "r", encoding="utf-8") as f:
    for line in f:
        country, languages = line.strip().split(" : ")
        countries[country] = languages.split()

# Отримуємо введення користувача
search_language = input("Введіть мову: ").strip().lower()

# Шукаємо країни, де говорять цією мовою
matching_countries = [country for country, langs in countries.items() if search_language in langs]

# Виводимо результат
if matching_countries:
    print("Країни, де розмовляють цією мовою:", ", ".join(matching_countries))
else:
    print("Такої мови немає у списку.")



#3
# Дані про зайнятість місць у вагоні
wagon = [
    {1: 'м', 2: None, 3: None, 4: 'ж'},  # Купе 0
    {1: None, 2: None, 3: None, 4: None},  # Купе 1 (повністю вільне)
    {1: 'ж', 2: None, 3: 'м', 4: None},  # Купе 2
    {1: None, 2: None, 3: None, 4: None}  # Купе 3 (повністю вільне)
]

# 1. Знаходимо повністю вільні купе
free_compartments = [i for i, compartment
                     in enumerate(wagon)
                     if all(place is None for place in compartment.values())]

# 2. Знаходимо всі вільні місця
free_seats = [(i, seat) for i, compartment
              in enumerate(wagon)
              for seat, status
              in compartment.items() if status is None]

# 3. Вільні нижні (1, 3) чи верхні (2, 4) місця
free_lower_seats = [(i, seat) for i, seat
                    in free_seats
                    if seat in [1, 3]]

free_upper_seats = [(i, seat) for i, seat
                    in free_seats
                    if seat in [2, 4]]

# 4. Вільні місця у купе з тільки чоловіками
male_only_seats = [(i, seat) for i, compartment
                   in enumerate(wagon)
                   if all(v in ["м", None]
                          for v in compartment.values()) for seat, status in compartment.items() if status is None]

# 5. Вільні місця у купе з тільки жінками
female_only_seats = [(i, seat) for i, compartment in enumerate(wagon)
                     if all(v in ["ж", None]
                            for v in compartment.values()) for seat, status in compartment.items() if status is None]

# Виводимо результати
print("Повністю вільні купе:", free_compartments)
print("Вільні місця:", free_seats)
print("Вільні нижні місця:", free_lower_seats)
print("Вільні верхні місця:", free_upper_seats)
print("Вільні місця у купе з тільки чоловіками:", male_only_seats)
print("Вільні місця у купе з тільки жінками:", female_only_seats)
