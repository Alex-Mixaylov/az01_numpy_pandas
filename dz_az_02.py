
# 2. Определите среднюю зарплату (Salary) по городу (City) - используйте файл приложенный к дз - dz.csv

import pandas as pd

df = pd.read_csv('dz.csv')

# Вывод данных, чтобы получить представление о структуре данных.
print(df)
# Есть  пустые ячейки, в том числе и в столбце Salary и City. Если  заполнить их нулями, то это будет некооретно
# так как  запрлата  не может  быть нулевой

# ДЛЯ МЕНЯ ЛОГИЧНЕЕ ИСКЛЮЧИТЬ СТРОКИ С НЕОПРЕДЕЛЕННОЙ ЗАРПЛАТОЙ И ГОРОДОМ
# удаление строк с пропусками  в столбце Salary и City

df = df.dropna(subset=['Salary', 'City'])
print(df)

# Группируем по городу и вычисляем среднюю зарплату
average_salary_by_city = df.groupby('City')['Salary'].mean()

# Печатаем результат
print(average_salary_by_city)

# Сохраняем результат
average_salary_by_city.to_csv('average_salary_by_city.csv')
