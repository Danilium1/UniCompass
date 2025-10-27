import pandas

df = pandas.read_excel("TestForTable.xlsx")


ages = df['age'].tolist()


def excel_to_dict(dataFrame): #делает словарь, где подряд идут имена, потом фамилии
    final_dict = {}
    names_of_columns = dataFrame.columns
    count_of_columns = len(names_of_columns)
    for i in range(count_of_columns):
        temp_column = dataFrame[names_of_columns[i]]
        temp_dict = {names_of_columns[i] : temp_column.tolist()}
        final_dict.update(temp_dict)
    return  (final_dict)



def perebor(data_dict):
    count_of_column = len(data_dict)
    columns_names = list(data_dict.keys())
    for i in range(count_of_column):
        name_of_column = columns_names[i]
        print(f"========={name_of_column}")
        for j in range(len(data_dict[name_of_column])):
            print(data_dict[name_of_column][j])

def excel_to_list(data_frame): #как же НЕ ЗАПАРНО
    final_list = data_frame.values.tolist()
    return final_list

def excel_names_of_columns(data_frame):
    final_names = data_frame.columns.tolist()
    return final_names

# print(excel_names_of_columns(df))
# listik = excel_to_list(df)
# print(listik)
# print("===========")
#
#
# for i in range(len(listik)):
#     print(listik[i])