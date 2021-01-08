import pandas as pd

a = []
b = []

for i in range(1,4):
    df = pd.read_excel("C:/Users/Roshan Ghimire/Desktop/data" + str(i) +".xlsx")
    for j in df['number'].values.tolist():
        a.append(j)
    for k in df['letter'].values.tolist():
        b.append(k)
    
df = pd.DataFrame({"Number":a,
                   "letter":b})
df.to_excel("C:/Users/Roshan Ghimire/Desktop/final.xlsx")
