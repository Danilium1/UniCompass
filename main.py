
from method_bd import *
from method_excel import *
import pandas



df = pandas.read_excel("TestForTable.xlsx")
dik = excel_to_list(df)

insert_into_table(dik)


