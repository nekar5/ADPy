import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import pylab

"""
1.	Знайти середню довжину хвоста та її середньоквадратичне відхилення. 
2.	Перевірити чи нормально розподілена ширина голови. 
3.	Перевірити за допомогою статистичних гіпотез чи відрізняється довжина 
    хвоста опосумів з 1-го місця і 7-го.  
4.	Побудувати лінійну регресійну модель залежності довжини тіла від віку. 
"""

data = pd.read_csv(r'C:\Users\Nestor\Desktop\Files\3\ADPy\lab2\possum.csv')


# 1
print("-----1-----")
tail_lengths = np.array(data['taill'])
avg_tail_length = np.average(tail_lengths)
std_tail_length = np.std(tail_lengths)
print("Середня довжина хвоста: ", avg_tail_length)
print("Середньоквадратичне відхилення: ", std_tail_length)


# 2
print("\n-----2-----")
skull_width = np.array(data['skullw'])
alpha = 0.05


def check_pvalue(pvalue):
    if pvalue > alpha:
        print(f"Нормальний, П-значення = ", pvalue)
    else:
        print(f"Не нормальний, П-значення = ", pvalue)


print("normaltest:")
result = stats.normaltest(skull_width)
check_pvalue(result.pvalue)

print("shapiro:")
result = stats.shapiro(skull_width)
check_pvalue(result.pvalue)

print("Kolmogorov-Smirnov:")
result = stats.kstest(skull_width, 'norm')
check_pvalue(result.pvalue)

print("Jarque-Bera:")
result = stats.jarque_bera(skull_width)
check_pvalue(result[1])

print("anderson:")
result = (stats.anderson(skull_width, dist='norm'))
if result[0] < result[1][2]:
    print(f"Нормальний, П-значення = ", result[0])
else:
    print(f"Не нормальний, П-значення = ", result[0])
"""
print(f"A-D statistic: {result[0]}")
print(f"Critical values: {result[1]}")
print(f"Significance levels: {result[2]}")
"""


plt.hist(skull_width, bins=10, alpha=0.5, label="skullw")
plt.title("Ширина черепа")
plt.legend()
plt.show()

stats.probplot(skull_width, dist="norm", plot=pylab)
pylab.title("Ширина черепа")
pylab.show()


# 3
print("\n-----3-----")
sites_n_lengths = data[['site', 'taill']]
s1_length = np.array(sites_n_lengths[sites_n_lengths['site'].isin(
    [1])].drop(['site'], axis=1)).flatten()
s7_length = np.array(sites_n_lengths[sites_n_lengths['site'].isin(
    [7])].drop(['site'], axis=1)).flatten()

result = stats.ttest_ind(s1_length, s7_length, alternative="two-sided")
if result.pvalue > alpha:
    print(f"Не відрізняється. П-значення = {result.pvalue}")

else:
    print(f"Відрізняється. П-значення = {result.pvalue}")
    result = stats.ttest_ind(s1_length, s7_length, alternative="less")  # 1 < 7
    if result.pvalue > alpha:
        print(f"з 1 більше. П-значення = {result.pvalue}")
    else:
        print(f"з 7 більше. П-значення = {result.pvalue}")


# 4
print("\n-----4-----")
total_lengths = np.array(data['totlngth'])
ages = np.array(data['age'])

res = stats.linregress(ages, total_lengths)
#res = stats.linregress(total_lengths, ages)
print(res)

plt.scatter(ages, total_lengths, label='data')
plt.plot(ages, res.intercept + res.slope*ages, 'r', label='regression')
plt.legend()
plt.xlabel("age")
plt.ylabel("total_length")
"""
plt.scatter(total_lengths, ages, label='data')
plt.plot(total_lengths, res.intercept + res.slope*total_lengths, 'r', label = 'regression')
plt.legend()
plt.xlabel("total_length")
plt.ylabel("age")
"""
plt.title("Залежність довжини тіла від віку")
plt.show()
