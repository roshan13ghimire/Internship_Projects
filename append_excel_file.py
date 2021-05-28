import pandas as pd

l = []
for i in range(1,157):
    df ="C:/Users/Roshan Ghimire/Desktop/Phase/Household" + str(i) +".csv"
    l.append(df)
df1 = pd.concat((pd.read_csv(file).assign(filename = file) for file in l),ignore_index=True)
df1.to_excel("C:/Users/Roshan Ghimire/Desktop/Finall.xlsx")
