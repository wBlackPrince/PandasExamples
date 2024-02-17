import pandas as pd;

# Создайте серию.Результат запишите в переменную series
list_in = [1, 2, 3, 4, 5]
series = pd.Series(list_in)

# Создайте серию состоящую из 4 строк
series = pd.Series(["wolf", "fox", "bear", "rabbit"])

# Создайте серию с 5 элементами. Индексы строк должны иметь значение row_1, row_2, row_3, row_4, row_5
series = pd.Series([1,2,3,4,5], index = ("row_1", "row_2", "row_3", "row_4", "row_5"))

# На основе указанного словаря dict_in = {'row_1': 1, 'row_2': 2, 'row_3': 3, 'row_4': 4}
# создайте серию содержащую только строки row_2 и row_4
dict_in = {'row_1': 1, 'row_2': 2, 'row_3': 3, 'row_4': 4}
series = pd.Series(dict_in, index = ["row_2", "row_4"])

# Создайте DataFrame из указанного словаря dict_in = {'col_1': [1, 2, 3], 'col_2': [4, 5, 6]}
dict_in = {'col_1': [1, 2, 3], 'col_2': [4, 5, 6]}
df = pd.DataFrame(dict_in)

#Создайте DataFrame содержащий 3 столбца и 3 строки.
dict_in = {"column a":[1, 2, 3], "column b":[4, 5, 6], "column c": [7, 8, 9]}
df = pd.DataFrame(dict_in)

# Создайте DataFrame содержащий 3 столбца и 3 строки, индексы строк должны иметь следующие имена: row_1, row_2, row_3
dict_in = {'col_1': [1, 2, 3], 'col_2': [4, 5, 6], 'col_3': [7, 8, 9]}
df = pd.DataFrame(dict_in, index = ["row_1", "row_2", "row_3"])

# На основе данного словаря создайте DataFrame.
dict_in = {'col_1': [1, 2, 3], 
           'col_2': [4, 5, 6],
           'col_3': [7, 8, 9], 
           'col_4': [10, 11, 12]}
df = pd.DataFrame(dict_in)

# На основе данного словаря создайте DataFrame состоящий только из col_1 и col_3.
dict_in = {'col_1': [1, 2, 3], 
           'col_2': [4, 5, 6],
           'col_3': [7, 8, 9], 
           'col_4': [10, 11, 12]}
df = pd.DataFrame(dict_in, columns = ["col_1", "col_3"])

# На основе данного словаря создайте DataFrame состоящий только из col_2 и col_3, 
# индексы строк должны иметь следующие имена: row_1, row_2, row_3.
dict_in = {'col_1': [1, 2, 3], 
           'col_2': [4, 5, 6],
           'col_3': [7, 8, 9], 
           'col_4': [10, 11, 12]}
indexes = ["row_1", "row_2", "row_3"]

df = pd.DataFrame(dict_in, index = indexes, columns = ["col_2", "col_3"])

ser_1 = pd.Series([1,2,3,4,5])
ser_2 = pd.Series([1,2,3,4,5])

# В программе созданы две серии и записаны в переменные ser_1 и ser_2. 
# Сформируйте DataFrame с двумя столбцами, имена столбцов col_1 и col_2.
# Столбец col_1 сформируйте на основе данных из ser_1, а col_2 из ser_2
df = pd.DataFrame({"col_1": ser_1, "col_2": ser_2})

#Series ser_1 содержит количество нерешенных упражнений каждым студентом курса "Pandas для анализа данных",
# а ser_2 содержит количество решенных упражнений каждым студентом курса.
# Получите DataFrame в котором каждому студенту сопоставлено количество решенных и нерешенных упражнений. 
#Обратите внимания на названия столбцов в DataFrame.

ser_1 = pd.Series([40,34,23,16,45], indexes = ("name_1", "name_2", "name_3", "name_4", "name_5"))
ser_1 = pd.Series([60, 78,99,78,80], indexes = ("name_1", "name_2", "name_3", "name_4", "name_5"))

df = pd.DataFrame({"Нерешенные": ser_1, "Решенные": ser_2})



# Представьте данные в виде DataFrame файл
df = pd.read_csv("data.csv")

df = pd.read_csv("data.csv", sep = ";")

#  Представьте данные в виде DataFrame в котором столбец 'date' установите в качестве индексов строк.
df = pd.read_csv("data.csv",sep = ":", index_col = ["date"])

# Импортируйте данные из столбцов ['col_2', 'col_3', 'col_5'] и представьте их в виде DataFrame.
c = ['col_2', 'col_3', 'col_5']
df = pd.read_csv("data.csv", sep = ";", usecols = c) 

# Импортируйте данные из файла так, чтобы получить DataFrame со столбцами ['col_2', 'col_3', 'col_5'] и столбцом "date" в качестве индексов строк, 
clm = ['col_2', 'col_3', 'col_5', 'date']
df = pd.read_csv("data.csv", sep = ",", index_col = "date", usecols = clm)

# Импортируйте данные из файла и присвойте столбцу 'city' тип данных 'category', столбцу 'col_2' - 'string', а 'col_3' - 'int'.
df = pd.read_csv("data.csv",sep = ';', dtype = {"city":'category', "col_2": 'string', "col_3": 'int' })

# Импортируйте данные из файла и присвойте столбцу 'city' тип данных 'category', столбцу 'col_2' - 'string', а 'col_3' - 'int'. Столбец 'date' установите в качестве индексов строк.
df = pd.read_csv("data.csv", sep = ':', index_col = "date", dtype = {"city": "category", "col_2": "string", "col_3": "int"})


# Импортируйте 5 строк из столбцов ['col_2', 'col_3', 'col_5'] и представьте их в виде DataFrame.
df = pd.read_csv("data.csv", sep = ",", usecols = ['col_2', 'col_3', 'col_5'], nrows = 5)

# В программе создан DataFrame и записан в переменную df. Запишите df в файл 'data.csv'.
df.to_csv("data.csv")

# В программе создан DataFrame и записан в переменную df. Столбцы ['client', 'product'] запишите в файл 'data.csv'
df.to_csv("data.csv", columns = ['client', 'product'] )

# В программе создан DataFrame и записан в переменную df. Столбцы ['client', 'product'] запишите в файл 'data.csv'. 
# Файл 'data.csv' не должен содержать индексы строк df.
df.to_csv("data.csv", columns = ['client', 'product'], index = False)