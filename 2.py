import pandas as pd

# На основе списка ['a', 'b', 'c', 'd', 'e'] создайте объект класса Index.
data = ['a', 'b', 'c', 'd', 'e']
ind = pd.Index(data)


# Создайте объект класса Index с 4-мя элементами и именем "my_index".
ind = pd.Index([1,2,3,4], name = "my_index")

# В программе создан DataFrame и записан в переменную df.
# С помощью специальных свойств DataFrame получите индексы строк и столбцов и запишите их в соответствующие переменные ind и cols
data = {"col_1":[1,2,3,4,5], "col_2":[1,2,3,4,5], "col_3": [1,2,3,4,5], "col_4": [1,2,3,4,5], "col_5": [1,2,3,4,5]} 
indx = [1,2,3,4,5]

df = pd.DataFrame(data, index = indx)

ind = df.index
cols = df.columns


# На основе данного словаря создайте DataFrame и запишите его в переменную df.
# После чего поменяйте индексы строк на row_1, row_2, row_3, row_4, row_5.
import pandas as pd

dict_in = {'col_1': [1, 2, 3, 4, 5],
           'col_2': [1, 2, 3, 4, 5],
           'col_3': [1, 2, 3, 4, 5]}
indexes = ["row_1", "row_2", "row_3", "row_4", "row_5"]
df = pd.DataFrame(dict_in)
df.index = indexes

# В программе создан DataFrame и записан в переменную df.
# С помощью специального свойства определите есть ли пропуски в индексах строк.
nan_in_indx = df.index.hasnans

# В программе создан DataFrame и записан в переменную df.
# Получите уникальные значения в индексах строк и столбцов и запишите их в переменные unique_ind и unique_cols соответственно.
unique_ind = df.index.unique()
unique_cols = df.columns.unique()

# В программе создан DataFrame и записан в переменную df.
# Получите количество уникальных значений в индексах строк и столбцов и запишите их в переменные nunique_ind и nunique_cols соответственно.
nunique_ind = df.index.nunique()
nunique_cols = df.columns.nunique()

# В программе создан DataFrame и записан в переменную df.
# С помощью метода rename() получите новый DataFrame с измененными метками столбцов col_2 и col_3 на new_col_2 и new_col_3 соответственно. 
new_df = df.rename({"col_2": "new_col_2", "col_3": "new_col_3"}, axis = 1)

# В программе создан DataFrame и записан в переменную df.
# С помощью метода rename() поменяйте в DataFrame метки столбцов col_2 и col_3 на new_col_2 и new_col_3 соответственно. 
df = df.rename({"col_2": "new_col_2", "col_3": "new_col_3"}, axis = 1)