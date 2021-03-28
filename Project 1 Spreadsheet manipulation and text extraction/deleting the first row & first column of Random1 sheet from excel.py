#python program for deleting the first row & first column of Random1 sheet and filling the blank cells of the table with 0.


import pandas as pd                                        #importing module

df = pd.read_excel("C:/Users/rosha/Desktop/file.xlsx")     #reading excel file and assigning it to  the dataframe

df.drop([ 'Unnamed: 0','Unnamed: 6']  , axis = 1 , inplace = True) #removing the last column (axis = 1) and storing the result into same dataframe so we need to write inplace function


df.drop(0 , axis = 0 ,inplace = True)                      #similarly removing the first row

df.fillna(0,inplace = True)                                #Replacing null values with 0

df.to_excel("C:/Users/rosha/Desktop/output.xlsx")          #exporting the dataframe to excel file
