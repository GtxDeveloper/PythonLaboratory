import pandas as pd

print("\nЗавдання 1: Дані найбільших міст України\n")

# Завдання 1: Дані найбільших міст України
population_dict = {
    'Київ': 2967360,
    'Харків': 1443207,
    'Одеса': 1017699,
    'Дніпро': 990724,
    'Донецьк': 908456,
    'Запоріжжя': 731922,
    'Львів': 717273,
    'Кривий Ріг': 619278,
    'Миколаїв': 480080,
    'Севастополь': 449138
}

population = pd.Series(population_dict)

print("Серія населення по містах України:")
print(population)

print("\nНайбільше населення:", population.max())
print("Найменше населення:", population.min())
print("Середнє населення:", population.mean())
print("Населення Києва:", population['Київ'])

print("\nПерші 5 міст:")
print(population.head(5))

# Додавання Полтави
population['Полтава'] = 286649

print("\nМіста з населенням понад 1 млн:")
print(population[population > 1_000_000])

print("\nСписок усіх міст:")
print(list(population.index))


print("\nЗавдання 2: Дані найбільших міст світу\n")

# Завдання 2: Дані найбільших міст світу
data = {
    'town': ['Токіо', 'Шанхай', 'Делі', 'Сан-Паулу', 'Мумбаї', 'Мехіко', 'Пекін', 'Каїр', 'Дакка', 'Осака'],
    'population': [37400000, 24150000, 22157000, 22048504, 20041000, 22460000, 21500000, 20901000, 14648000, 20000000],
    'square': [13500, 6340.5, 33578, 7946.96, 1097, 7815, 16411, 1709, 1600, 225],
    'country': ['Японія', 'Китай', 'Індія', 'Бразилія', 'Індія', 'Мексика', 'Китай', 'Єгипет', 'Бангладеш', 'Японія']
}

towns = pd.DataFrame(data)
towns['density'] = towns['population'] / towns['square']

print("\nМіста та країни:")
print(towns[['town', 'country']])

print("\nПерші п’ять міст:")
print(towns.head(5))

towns.set_index('town', inplace=True)

print("\nДані по Токіо:")
print(towns.loc['Токіо'])

print("\nМіста з населенням понад 12 млн:")
print(towns[towns['population'] > 12000000])

print("\nМіста з площею понад 5000 км2:")
print(towns[towns['square'] > 5000])

print("\nМіста з КНР:")
print(towns[towns['country'] == 'Китай'])
