import pandas as pd
import numpy as np


"""
1. Виділити один зі стовпців (на вибір) з файлу як об’єкт Series, виділити з нього підмасив. 
Задати назви індексів цього об’єкту. Виділити підмасиви за допомогою прямої та непрямої індексацій.
2. До об’єкту DataFrame, в який записано вміст файлу, додати новий стовпець, що є результатом 
операцій над іншими стовпцями. Також продемонструвати додавання та видалення рядків, видалення стовпців.
3. Встановити один зі стовпців індексом. Визначити основні статистичні характеристики та типи 
даних всіх стовпців. Змінити тип даних для одного з стовпців. Згрупувати дані за одним зі стовпців, 
застосувати кілька агрегуючих функцій, виділити підмасив за певними ознаками.
4. Створити декілька власних об’єктів DataFrame за такою ж тематикою, що й файл. Наприклад, якщо 
тема файлу – жаби, можна створити об’єкти, що містять розміри жаб, вагу, стать, кількість особин в 
популяції і т.д. Використати описані в теоретичних відомостях параметри методів merge та concat для 
різних видів злиття та об’єднання даних цих об’єктів.
"""

data = pd.read_csv(r'C:\Users\Nestor\Desktop\Files\3\ADPy\lab2\possum.csv')

# 1
print('-----1-----')
# Виділити один зі стовпців (на вибір) з файлу як об’єкт Series
srs = pd.Series(data['totlngth'].loc[1:26])
# print(srs)

# виділити з нього підмасив
print(srs.loc[5:15])

# Задати назви індексів цього об’єкту
srs.index = list('abcdefghijklmnopqrstuvwxyz')

# виділити з нього підмасив (пряма)
print(srs.loc['f':'o'])

# виділити з нього підмасив (непряма)
print(srs.iloc[5:15])


# 2
print('-----2-----')
# До DataFrameдодати новий стовпець, що є результатом операцій над іншими стовпцями
data['tailtototal'] = (data['taill']/data['totlngth']) * \
    100  # %довжини хвоста від загальної
print(data)

# додавання рядків
data2 = pd.DataFrame([
    [104, 105, 2, 'Vic', 'f', 6.0, 94.0, 60.0, 95.5,
        39.0, 75.4, 51.9, 15.5, 30.0, 34.0, 40.888888],
    [105, 106, 3, 'other', 'm', 3.5, 100.0, 62.0, 96.0, 40.0, 77.0, 55.0, 17.0, 33.0, 29.0, 38.123456]],
    columns=['Unnamed: 0', 'case', 'site', 'Pop', 'sex', 'age', 'hdlngth', 'skullw', 'totlngth', 'taill',
             'footlgth', 'earconch', 'eye', 'chest', 'belly', 'tailtototal'],
    index=['+1', '+2'])
data = data.append(data2)
print(data)

# видалення рядків
print(data.drop(labels='+2', axis=0, inplace=False))

# видалення стовпців
print(data.drop(labels='tailtototal', axis=1, inplace=False))


# 3
print('-----3-----')
# Встановити один зі стовпців індексом
data_bu = data
data = data.set_index('case')
print(data)

# Визначити основні статистичні характеристики
print(data.describe())
# та типи даних всіх стовпців
print(data.dtypes)

# Змінити тип даних для одного з стовпців
print(data.astype({'age': 'int64'}).dtypes)  # float64 -> int64

# Згрупувати дані за одним зі стовпців
print(data.groupby('sex').mean())

# застосувати кілька агрегуючих функцій
print(data.groupby('site').agg([sum, np.mean]))

# виділити підмасив за певними ознаками
print(data[data['age'] > 7])


# 4
print('-----4-----')
#data_bu.drop(data_bu.index[5:106], inplace=True)
data = data_bu
print(data)

# Створити декілька власних об’єктів DataFrame за такою ж тематикою
apptt_n_actvt = pd.DataFrame([  # апетити та активності
    [1, 'high', 'active'],
    [2, 'medium', 'active'],
    [3, 'high', 'active'],
    [4, 'high', 'lazy'],
    [5, 'low', 'lazy']],
    columns=['case', 'appetite', 'activity'])
print(apptt_n_actvt)

weights = pd.DataFrame([  # ваги
    [3.5], [3.3], [4.5], [4.7], [2.8]],
    columns=['weight'])
print(weights)

# merge
upd_data = pd.merge(data, apptt_n_actvt, how='outer')
print(upd_data)
upd_data = pd.merge(data, apptt_n_actvt, on='case')
print(upd_data)

# concat
upd_data = pd.concat([data, apptt_n_actvt.drop(
    labels='case', axis=1), weights], axis=1, join='inner')
print(upd_data)
