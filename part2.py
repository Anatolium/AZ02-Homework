import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range(start='2022-07-26', periods=10, freq='D')
# Список из 10 случайных значений
values = np.random.rand(10)
df = pd.DataFrame({'Date': dates, 'Value': values})
# Установим колонку Date в качестве индекса всего датафрейма:
df.set_index('Date', inplace=True)
print(df)
# Ресэмплирование данных — это процесс изменения частоты временных рядов
# Ресэмплирование данных для месячного интервала, используя среднее значение
month = df.resample('M').mean()
print(month)

# Удаление выброса
data = {'value': [1, 2, 3, 3, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 55]}
df = pd.DataFrame(data)
# df['value'].hist()
df.boxplot(column='value')
plt.show()

Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)
IQR = Q3 - Q1

print(f"Q1={Q1} Q3={Q3} IQR={IQR}")

downside = Q1 - 1.5 * IQR
upside = Q3 + 1.5 * IQR

df_new = df[(df['value'] >= downside) & (df['value'] <= upside)]
df_new.boxplot(column='value')
plt.show()
