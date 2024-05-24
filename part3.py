import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'gender': ['female', 'male', 'male', 'male', 'female'],
    'department': ['IT', 'Engineering', 'Marketing', 'Engineering', 'IT']
}

df = pd.DataFrame(data)

# Преобразуем столбцы в категориальные данные
df['gender'] = df['gender'].astype('category')
df['department'] = df['department'].astype('category')

# cat - атрибут, который используется для работы с категориальными данными в pandas
print(df['gender'].cat.categories)
print(df['department'].cat.categories)
# print(df['gender'].cat.codes)
# print(df['department'].cat.codes)

# Добавить категорию
df['department'] = df['department'].cat.add_categories(['Finance'])
print(df['department'].cat.categories)

# Удалить категорию
df['department'] = df['department'].cat.remove_categories(['IT'])
print(df['department'].cat.categories)

print(df)
