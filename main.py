import pandas
df = pandas.read_excel(r"C:\Users\Danilium1\Downloads\TestForTable.xlsx")
print(df['name'])

ages = df['years'].tolist()
print(sum(ages)/len(ages))

