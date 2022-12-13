import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

"""
1. Побудувати стовпчикові діаграми, на яких відобразити 
    а) кількість клієнтів з підключеним роумінгом та без; 
    б) максимальну кількість хвилин в нічний час для клієнтів з підключеним роумінгом та без;
    в) середню кількість міжнародних дзвінків для клієнтів з підключеним роумінгом та без і з врахуванням лояльності.
2. Побудувати гістограму оплати в вечірній час, загальну і в залежності від лояльності.
3. Побудувати діаграму хвилин на міжнародні дзвінки (загальну і в залежності від підключеного роумінгу), визначити чи присутні викиди.
4. За допомогою діаграм розсіювання зробити висновки щодо залежності між 
    а) хвилинами і дзвінками в нічний час; 
    б) хвилинами і оплатою в нічний час. Порахувати коефіцієнт кореляції за допомогою відповідних функцій.
"""

data = pd.read_csv(r'C:\Users\Nestor\Desktop\Files\3\ADPy\lab4\telecom.csv')


#-----1----- Побудувати стовпчикові діаграми, на яких відобразити 

#---а) кількість клієнтів з підключеним роумінгом та без;

plt.barh(['without', 'with'], data.groupby(['international plan']).size())
plt.title('#1a international plan')
plt.show()


"""
#basic:
data.groupby(['international plan']).size().plot.barh([['without', 'with']])
plt.show()

#seaborn:
sns.countplot(x=data['international plan'])
plt.show()
"""

#---б) максимальну кількість хвилин в нічний час для клієнтів з підключеним роумінгом та без;

plt.bar(['without', 'with'], 
    np.array(data.groupby(['international plan'])['total night minutes'].max()))
plt.title('#1б max night minutes (international plan)')
plt.show()


#---в) середню кількість міжнародних дзвінків для клієнтів з підключеним роумінгом та без і з врахуванням лояльності.

plt.bar(['without', 'with'], data.groupby(['international plan'])['total intl calls'].mean(), 
    color='yellow', label='all', edgecolor='black')
plt.bar(['without', 'with'], data[data['churn']==True].groupby(['international plan'])['total intl calls'].mean(), 
    alpha=0.2, color='blue', label='loyal', edgecolor='black')
plt.legend()
plt.title('#1в intl calls mean')
plt.show()



#alternative
tic = pd.pivot_table(data, values='total intl calls', index='international plan', columns='churn', aggfunc=np.mean)
ax = tic.plot(kind='bar')
plt.title('#1в intl calls mean (alt)')
plt.legend()
plt.show()



#-----2----- Побудувати гістограму оплати в вечірній час, загальну і в залежності від лояльності.

plt.hist([data['total eve charge'], data[data['churn']==False]['total eve charge'], data[data['churn']==True]['total eve charge']],
    10, histtype='bar',  label=['total', 'unloyal', 'loyal'])
plt.title('#2 eve charge (1)')
plt.legend()
plt.show()


plt.hist(data['total eve charge'], label='total')
plt.hist(data[data['churn']==False]['total eve charge'], label='unloyal')
plt.hist(data[data['churn']==True]['total eve charge'], label='loyal')
plt.title('#2 eve charge (2)')
plt.legend()
plt.show()






#-----3----- Побудувати діаграму хвилин на міжнародні дзвінки (загальну і в залежності від підключеного роумінгу), визначити чи присутні викиди.

sns.boxplot(y='total intl minutes', data=data)
plt.title('#3 total intl minutes')
plt.show()

sns.boxplot(x='international plan', y='total intl minutes', data=data)
plt.title('#3 total intl minutes (box)')
plt.show()

sns.catplot(x='international plan', y='total intl minutes', data=data)
plt.title('#3 total intl minutes')
plt.show()



#-----4----- За допомогою діаграм розсіювання зробити висновки щодо залежності між 

#---а) хвилинами і дзвінками в нічний час;

plt.scatter(data['total night minutes'], data['total night calls'], alpha=0.7)
plt.title('#4a total night minutes/calls cor.')
plt.show()


#---б) хвилинами і оплатою в нічний час. Порахувати коефіцієнт кореляції за допомогою відповідних функцій.

sns.lmplot(x='total night minutes', y='total night charge', data=data)
plt.title('#4a total night minutes/charпу cor.')
plt.show()

print('correlation coefficient: ',
    stats.pearsonr(data['total night minutes'], data['total night charge']))

