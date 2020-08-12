#program to present data on bar chart race


import pandas as pd                         #importing libraries
import bar_chart_race as bcr


df = pd.read_excel("C:/Users/rosha/Desktop/demo.xlsx")         #importing data
df = df.set_index("Date")                                      #initializing index as Date


bcr.bar_chart_race(df = df , filename = "C:/Users/rosha/Desktop/demo.mp4", figsize = (4,3) , title = 'DEMO')  