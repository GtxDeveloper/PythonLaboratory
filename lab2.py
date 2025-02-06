import json
from locale import currency

import requests

#1
a,b = map(int, input("#1 Input two numbers: ").split())
print(f"{a} + {b} = {a + b}")

#2
userInput = input("#2 Try to solve: 4 * 100 - 54 =  ")
print("Your answer: " + userInput + " and the correct answer: " + str(4* 100 - 54))

#3
class SimpleCalculator:
    def __init__(self, a: float, b: float):
        self.a = a
        self.b = b

    def add(self):
        print(f"{self.a} + {self.b} = {self.a + self.b}")

    def subtract(self):
        print(f"{self.a} - {self.b} = {self.a - self.b}")

    def multiply(self):
        print(f"{self.a} * {self.b} = {self.a * self.b}")

    def power(self):
        print(f"{self.a} ^ {self.b} = {self.a ** self.b}")

    def increment(self):
        print(f"{self.a} incremented by 1 = {self.a + 1}")



a = float(input("#3 Input value of a: "))
b = float(input("Input value of b: "))

calculator = SimpleCalculator(a, b)
calculator.add()
calculator.subtract()
calculator.multiply()
calculator.power()
calculator.increment()

#4
a,b,c,d = map(int, input("#4 Input four numbers: ").split())
print(f"Trying to solve ({a} + {b}) / ({c} + {d})")
if c + d == 0:
    print("impossible to divide by 0")
else:
    print(f"({a} + {b}) / ({c} + {d}) = {(a + b) / (c + d)}")

#5
a = int(input("#5 Input value of a: "))
while a >= 10:
    a = a%10
print(f"Last digit = {a}")

#6
a = input("#6 Input value of a: ")
result = 0
for i in a:
    result += int(i)
print(f"Sum = {result}")
#7
kilometers = int(input("#7 Input number of kilometers: "))
print(f"{kilometers * 1000} meters")

#8
api_key = "fca_live_X4AplbUkP7LbpunzHDmgyvQGlO0eRdJN0wIBKsQb"
currency = "MXN"
url = f"https://api.freecurrencyapi.com/v1/latest?apikey={api_key}&currencies={currency}"
response = requests.get(url)
data = json.loads(response.text)
price = data["data"]["MXN"]
usd_value = int(input("#8 Input USD value: "))
print(f"Value of pessos by {usd_value} USD : {price * usd_value}")