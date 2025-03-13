from audioop import reverse

letters = [1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
print("1.	Отримати послідовність символів від початку і до кінця.")
for letter in letters:
    print(letter)
print("2.	Отримати послідовність символів від 20-го символа і до кінця.")
for i in range(19, len(letters)):
    print(letters[i])
print("3.	Отримати послідовність символів від 12-го символа по 15-й (15-й символ не включається).")
for i in range(11,14):
    print(letters[i])
print("4.	Отримати послідовність останніх 5 символів.")
for i in range(len(letters) - 5, len(letters)):
    print(letters[i])
print("5.	Отримати послідовність символів від 18-го символа і до 3-го з кінця (3-й символ з кінця не включається).")
for i in range(17, len(letters) -3):
    print(letters[i])

print("6.	Отримати послідовність символів від 6-го символа з кінця і до 2-го символа з кінця (2-й символ з кінця не включається).")
for i in range(len(letters) - 7, len(letters)-3):
    print(letters[i])
print("7.	Отримати кожний 7-й символ з початку і до кінця.")
for i in range(6, len(letters)):
    if i % 7 == 0:
        print(letters[i - 1])

print("8.	Отримати кожний 3-й символ від 4-го символа з початку і до 20-го символа (20-й символ не включається).")
for i in range(4, 19):
    if i % 3 == 0:
        print(letters[i - 1])

print("9.	Отримати кожний 4-й символ починаючи від 19-го символа і до кінця.")
for i in range(18 , len(letters)):
    if i  % 4 == 0:
        print(letters[i - 1])

print("10.	Отримати кожний 5-й символ починаючи з початку і до 21-го символа (21-й символ не включається).")
for i in range(0, 21):
    if i > 0 and i % 5 == 0:
        print(letters[i - 1 ])


print("11.	Перевернути рядок з кінця на початок. - [ : : −1 ]")
for letter in reversed(letters):
    print(letter)
print("12.	Вивести довжину рядка.")
print(len(letters))

print("2.1")
urlString  = 'http://dl.dropbox.com/u/7334460/Magick_py/py_magick.pdf'

splitted = urlString.split('/')

file_name = splitted[len(splitted) - 1]

print(file_name)

poem =  ("  Думи мої, думи мої, Лихо мені з вами! "
         "Нащо стали на папері Сумними рядами?.."
         "Чом вас вітер не розвіяв В степу, як пилину? "
         "Чом вас лихо не приспало, Як свою дитину?... ")

print("3.1")
print(poem.strip().count(" "))
print("3.2")
print(len(poem))
print("3.3")
poem = poem.strip()
print(poem)
print("3.4")
start = poem.find("Нащо стали на папері")  # Початок фрагмента
end = poem.find("Як свою дитину?") + len("Як свою дитину?")  # Кінець фрагмента

text1 = poem[start:end]  # Вирізаний фрагмент
print(text1)
print("3.5")
splitted_poem = text1.split("?")
print(splitted_poem)
print("3.6")
print( poem.replace("степу", "полі"))
print("3.7")
print(poem.find("вітер"))
print("3.8")
poem_upper   = poem.upper()
print(poem_upper)
print("3.9")
lower = poem.lower()
print(lower)



