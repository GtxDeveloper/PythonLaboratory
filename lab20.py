import numpy as np
import matplotlib.pyplot as plt

# Завдання 1 побудова графіків з масивів
x = np.arange(0, 100)
y = x * 2
z = x ** 2

# Всі лінії на одному графіку
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='y = x*2', color='red', marker='o', linewidth=2)
plt.plot(x, z, label='z = x^2', color='blue', marker='s', linewidth=2)
plt.xlabel('X-ось', fontsize=12)
plt.ylabel('Y-ось', fontsize=12)
plt.title('Один графік з кількома лініями', fontsize=14)
plt.legend()
plt.text(50, 100, 'y = x*2', fontsize=10)
plt.text(30, 900, 'z = x^2', fontsize=10)
plt.grid(True)
plt.show()

# Кожна лінія на окремому графіку в одному полі
fig, axs = plt.subplots(2, 1, figsize=(10, 10))

axs[0].plot(x, y, color='green', marker='^', linewidth=2)
axs[0].set_title('Графік y = x*2', fontsize=12)
axs[0].set_xlabel('X', fontsize=10)
axs[0].set_ylabel('Y', fontsize=10)
axs[0].legend(['y = x*2'])
axs[0].text(50, 100, 'y = x*2', fontsize=10)
axs[0].grid(True)

axs[1].plot(x, z, color='purple', marker='x', linewidth=2)
axs[1].set_title('Графік z = x^2', fontsize=12)
axs[1].set_xlabel('X', fontsize=10)
axs[1].set_ylabel('Z', fontsize=10)
axs[1].legend(['z = x^2'])
axs[1].text(30, 900, 'z = x^2', fontsize=10)
axs[1].grid(True)

plt.tight_layout()
plt.show()

# Завдання 2 побудова графіка з файлу
x_vals = []
y_vals = []

with open('test.txt', 'r') as file:
    for line in file:
        x, y = map(float, line.strip().split())
        x_vals.append(x)
        y_vals.append(y)

plt.plot(x_vals, y_vals, marker='o', color='orange', linewidth=2)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Графік з координат з файлу test.txt')
plt.grid(True)
plt.show()
