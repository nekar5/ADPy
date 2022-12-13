import pandas as pd
import numpy as np


"""
Створити програму, яка:
1. Генерує випадкові і невипадкові масиви різними способами, 
зазначеними в теоретичних відомостях.
2. Демонструє звернення до елементів масиву за допомогою індексів, 
в тому числі від’ємних; виділення підмасивів як одновимірних, так і 
багатовимірних масивів.
3. Демонструє основні арифметичні операції над масивами, а також 
роботу методів reduce, accumulate, outer.
4. Вираховує статистичні характеристики, а саме, мінімальне і 
максимальне значення, вибіркові середнє, дисперсію, середньоквадратичне 
відхилення, медіану та 25 та 75 персентилі, величини ширина пелюстки 
(petal_width) з набору даних щодо квіток ірису (iris.csv).
"""


# 1
arr = np.array([1, 2, 3])  # 1x3
arr = np.array([[1, 2], [3, 4]])  # 2x2
arr = np.array([1, 2, 3], dtype='int')  # 1x3 int
arr = np.arange(0, 10, 1)  # 1x9 aranged 0,1..8,9
arr = np.ones(5)  # 1x5 ones
arr = np.zeros(5)  # 1x5 zeros
arr = np.empty(5)  # 1x5 empty
arr = np.ones((2, 5))  # 2x5 ones
arr = np.linspace(0, 1, 10)  # 1x10   0, 0.11111111 ... 0.88888888, 1
arr = np.random.random((2, 5))  # 2x5 0 to 1
arr = np.random.randint(0, 10, (2, 5))  # 2x5 random 0 to 10


# 2
print("-----2-----")
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], dtype='int')
print(arr)
print(arr[5])  # 5th
print(arr[-1])  # last
print(arr[3:8:1])  # 3rd to 7th w/ step 1
print(arr[7:2:-1])  # 7th to 3rd w/ step 1
print()
arr = np.array([[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]], dtype='int')
print(arr)
print(arr[0:3:1, 0:3:1])  # 1&2d 0 to 3rd
print('\n')


# 3
print("-----3-----")


def assign_rand(amnt):
    temp = np.random.randint(0, 10, amnt)
    return temp


print("add +")
arr = assign_rand(10)
arr2 = assign_rand(10)
print(arr, '\n+\n', arr2, '\n=')
arr = np.add(arr, arr2)
print(arr, '\n')

print("subtract -")
arr2 = assign_rand(10)
print(arr, '\n-\n', arr2, '\n=')
arr = np.subtract(arr, arr2)
print(arr, '\n')

print("multiply *")
arr2 = assign_rand(10)
print(arr, '\n*\n', arr2, '\n=')
arr = np.multiply(arr, arr2)
print(arr, '\n')

print("divide /")
arr2 = 2 * np.ones(10, dtype='int') # division on array example
print(arr, '\n/\n', arr2, '\n=')
arr = np.divide(arr, arr2)
print(arr, '\n')

print("power **")
arr = assign_rand(10)
power = 2
print(arr, '\n**\n', power, '\n=')
arr = np.power(arr, power)
print(arr, '\n')

print("mod %")
arr = assign_rand(10)
mod = 3
print(arr, '\n%\n', mod, '\n=')
arr = np.mod(arr, mod)
print(arr, '\n')

print("negative *-1")
arr = assign_rand(10)
print(arr, '\n*(-1)\n=')
arr = np.negative(arr)
print(arr, '\n')

print('reduce')
arr = assign_rand(10)
print(arr, '\nresult:')
arr = np.add.reduce(arr)
print(arr, '\n')

print('acumulate')
arr = assign_rand(10)
print(arr, '\nresult:')
arr = np.add.accumulate(arr)
print(arr, '\n')

print('outer')
arr = assign_rand(3)
arr2 = assign_rand(3)
print(arr, '\n', arr2, '\nresult:')
arr = np.add.outer(arr, arr2)
print(arr, '\n')


# 4
print("-----4-----")

data = pd.read_csv(r'C:\Users\Nestor\Desktop\Files\3\ADPy\lab1\iris.csv')
petal = np.array(data['petal_length'])

# min
print('min: ', np.min(petal))
# max
print('max: ', np.max(petal))
# mean
print('mean: ', np.mean(petal))
# var
print('var: ', np.var(petal))
# std
print('std: ', np.std(petal))
# median
print('median: ', np.median(petal))
# 25 percentile
print('25 percentile: ', np.percentile(petal, 25))
# 75 percentile
print('75 percentile: ', np.percentile(petal, 75))
