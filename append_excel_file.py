import pandas as pd

l = []
for i in range(1,156):
    df ="C:/Users/Roshan Ghimire/Desktop/Phase/Household" + str(i) +".csv"
    l.append(df)
a = pd.concat((pd.read_csv(file).assign(filename = file) for file in l),ignore_index=True)
a.to_excel("C:/Users/Roshan Ghimire/Desktop/Final.xlsx")
