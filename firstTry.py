from method_bd import *
from method_excel import *
import pandas

df = pandas.read_excel("TestForTable.xlsx")

names_str = ""
columns_names = list(df.keys())
stri = ""
print ( columns_names[1])
for f in range(len(columns_names)):
    names_str += f"{columns_names[f]}, "


print(', '.join(columns_names))