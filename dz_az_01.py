# 1. Загрузите набор данных из CSV-файла в DataFrame.
# https://www.kaggle.com/datasets/huseyincot/vehicle-spare-parts-index

import pandas as pd

df = pd.read_csv('vehicle_spare_parts.csv')

# Выведите первые 5 строк данных, чтобы получить представление о структуре данных.
print(df.head())

# Выведите информацию о данных (.info()) и статистическое описание (.describe()).
print(df.info())
print(df.describe())
