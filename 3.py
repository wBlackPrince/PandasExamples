import pandas as pd

dict_in = {'data': [1, 2, 3], 
           'age': 1[4, 65, 26],
           'name': ["Mark", "Tom", "Robert"], 
           'col_4': [10, 11, 12]}

df = pd.DataFrame(dict_in)

ser = pd.Series([1,0,1])
ser_1 = pd.Series([901, 765, 344])
ser_2 = pd.Series([200, 400, 500])

# В программе создан DataFrame и записан в переменную df. Он содержит столбец с именем "data". 
# Установите этот столбец в качестве индексов строк.

new_df = df.set_index("data")

# В программе создан DataFrame и записан в переменную df. 
# Он содержит столбцы с именами "data" и "age". Установите эти столбцы в качестве индексов строк.

new_df = df.set_index(["data", "age"])

# В программе создан DataFrame и записан в переменную df. В текущем DataFrame поменяйте индексы строк на столбец "data"
df.set_index("data", inplace = True)


# В программе создан DataFrame и записан в переменную df.
# В данном DataFrame "сбросьте" индексы строк, представив их в виде столбца df.

df = df.reset_index()

# В программе создан DataFrame и записан в переменную df.
#  Столбец с именем "name" присвойте переменной series. В переменной series должна быть Series, а не DataFrame.
series = df['name']

# В программе создан DataFrame и записан в переменную df. 
# Столбец с именем "name" присвойте переменной df_1. В переменной df_1 должен быть  DataFrame, а не Series.
df_1 = df[["name"]]

# В программе созданы DataFrame и Series и записаны в переменные df и ser.
# Создайте новый столбец "new_col" и запишите в него ser.

df["new_col"] = ser

# В программе создан DataFrame и записан в переменную df.
# Создайте новый столбец "new_col" и запишите в него значение из столбца "age".
df["new_col"] = df["age"]

# В прошлом задании вы создали столбец "new_col". Он явно там лишний, удалите его. 
del df["new_col"]

# В программе создан DataFrame и две серии Series и записаны в переменные df, ser_1, ser_2.
# В df создайте новые столбцы "new_col_1" и new_col_2, запишите в них ser_1 и ser_2 соответственно. 
# Столбец "date" установите в качестве индексов строк.

df["new_col_1"] = ser_1
df["new_col_2"] = ser_2

df = df.set_index("date")