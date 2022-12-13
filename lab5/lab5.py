import random
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt

"""
Створити не менше двох об’єктів TimeSeries, у яких індекси створені за 
допомогою date_range(). Виділити підмасиви у цих об’єктів.
1. Побудувати графік зміни об’єму продаж:
 а) загальний;
 б) за 2020 рік;
 в) за лютий 2019 року; 
 г) з червня 2018 – до липня 2020; 
 д) за 2018 та 2020 на одному графіку.
2. Знайти середні значення ціни на час закриття біржі (в доларах): 
 а) за 2020 рік;
 б) за кожний місяць; 
 в) за кожні два тижні весни та літа 2019 року. 
 г) Розрахувати і зобразити зміни ціни на час закриття біржі (в доларах) у 
    відсотках за кожен день впродовж 2019 року. 
 д) Знайти та зобразити графічно ковзне середнє ціни на час закриття 
    біржі (в доларах) за 2020 рік з вікном в робочий тиждень.
"""

data = pd.read_csv(
    r'C:\Users\Nestor\Desktop\Files\3\ADPy\lab5\digital_currency.csv')
data = data.rename(columns={"Unnamed: 0": "Date"})
data = data.astype({"Date": "datetime64"})
data.set_index("Date", inplace=True)
#data.explode('volume')
print(data)

# -----0

print("-----0")
idx = pd.date_range("2018-05-07", periods=12, freq="M")

ts1 = pd.Series([random.random() for x in range(12)], index=idx)[:"2019-01-01"]
print(ts1, end="\n\n")
idx = pd.date_range("2018-05-07", periods=365, freq="D")
ts2 = pd.Series([random.random() for x in range(365)], index=idx)[:8]
print(ts2, end="\n\n")


print("-----1")
# -----1 Побудувати графік зміни об’єму продаж:

# ---a загальний;

sns.lineplot(data=data, x=data.index, y="volume", hue=data.index.year)
plt.title('#1a загальний')
plt.show()


# ---б за 2020 рік;

temp = data.loc["2020-01-01":"2021-01-01"]
sns.lineplot(data=temp, x=temp.index, y="volume", hue=temp.index.year)
plt.title('#1б за 2020 рік')
plt.show()


# ---в за лютий 2019 року;

temp = data.loc["2019-02-01":"2019-02-28"]
sns.lineplot(data=temp, x=temp.index, y="volume", hue=temp.index.year)
plt.title('#1в за лютий 2019 року')
plt.show()


# ---г з червня 2018 – до липня 2020;

temp = data.loc["2018-06-01":"2020-07-01"]
sns.lineplot(data=temp, x=temp.index, y="volume", hue=temp.index.year)
plt.title('#1г з червня 2018 – до липня 2020')
plt.show()


# ---д за 2018 та 2020 на одному графіку.

temp = data.loc["2018-01-01":"2019-01-01"]
temp = temp.append(data.loc["2020-01-01":"2021-01-01"])
sns.lineplot(data=temp, x=temp.index, y="volume", hue=temp.index.year)
plt.title('#1д за 2018 та 2020 на одному графіку')
plt.show()
print(temp)


print("-----2")
# -----2 Знайти середні значення ціни на час закриття біржі (в доларах):

# ---a за 2020 рік;

print("середня ціна на час закриття біржі за 2020:  ",
      data.groupby(data.index.year).mean()["close_USD"][2020])
temp = data.loc["2020-01-01":"2021-01-01"]
temp['week'] = pd.to_datetime(
    data.loc["2020-01-01":"2021-01-01"].index).to_period('W-MON')
temp = temp.groupby('week').mean()
sns.lineplot(data=temp, x=temp.index.astype(str),
             y=temp['close_USD'], hue=temp.index.year)
plt.title('#2a сер. знач. ціни за 2020 рік (потижнево)')
plt.show()


# ---б за кожний місяць;

temp = data.resample("M").mean()
sns.lineplot(data=temp, x=temp.index, y=temp["close_USD"])
plt.title('#2б сер. знач. ціни за кожний місяць')
plt.show()


# ---в за кожні два тижні весни та літа 2019 року.

temp = data["2019-03-01":"2019-9-01"].resample("2W").mean()
sns.lineplot(data=temp, x=temp.index, y=temp["close_USD"])
plt.title('#2в сер. знач. ціни за кожні два тижні весни та літа 2019 року')
plt.show()


# ---г Розрахувати і зобразити зміни ціни на час закриття біржі (в доларах) у
#    відсотках за кожен день впродовж 2019 року.

temp = data["2019-01-01":"2020-01-01"].pct_change()[1:]
sns.lineplot(data=temp, x=temp.index, y=temp["close_USD"])
plt.title('#2г сер. знач. ціни на час закриття біржі (в доларах) у відсотках за кожен день впродовж 2019 року')
plt.show()


# ---д Знайти та зобразити графічно ковзне середнє ціни на час закриття
#    біржі (в доларах) за 2020 рік з вікном в робочий тиждень.

temp = data["2020-01-01":"2021-01-01"].rolling(30).mean()
sns.lineplot(data=temp, x=temp.index, y=temp["close_USD"])
plt.title('#2д ковзне середнє ціни на час закриття біржі (в доларах) за 2020 рік з вікном в робочий тиждень')
plt.show()
