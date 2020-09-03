import requests
import pandas as pd
from bs4 import BeautifulSoup
import json
import time
from datetime import date
from datetime import datetime

print("Enter the Company's Name in lower case letter:")
Company_Name = input()



print("Enter the time interval that you need to check (in sec):")
d_sleep = float(input())

print("Enter the total time that you need to see in sec:")
total_time = int(input())


t_iteration = int(d_sleep * total_time)


url = 'http://www.nepalstock.com/todaysprice?stock-symbol=' + Company_Name
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
s = soup.find(id='home-contents').getText().split('\n\n\n')

data11 = s[7]
Total_Amount_Rs1 = data11[17:]

data22 = s[8]
Total_Quantity1 = data22[15:]

data33 = s[9]
Total_No_of_Transactions1 = data33[25:]



data = s[5]

data_array = data.split('\n')



data_array.remove(data_array[0])
data_array.remove(data_array[len(data_array)-1])


iteration = 0

l = []
m = []
n = []
o = []
p = []
q = []
r = []
ss = []
t = []
u = []
v = []
w = []
x = []
y = []

nnl = []
lis = []

lis.append(data_array[1])
lis.append(data_array[2])
lis.append(data_array[3])
lis.append(data_array[4])
lis.append(data_array[5])
lis.append(data_array[6])
lis.append(data_array[7])
last = data_array[8]
lis.append(last[:len(last)-1])
lis.append(Total_Amount_Rs1)
lis.append(Total_Quantity1)
lis.append(Total_No_of_Transactions1)


t_date = date.today().strftime("%B %d, %Y")
t_time = datetime.now().strftime("%H:%M:%S")


l.append(data_array[0])
m.append(t_date)
n.append(t_time)
o.append(data_array[1])
p.append(data_array[2])
q.append(data_array[3])
r.append(data_array[4])
ss.append(data_array[5])
t.append(data_array[6])
u.append(data_array[7])
las = data_array[8]
v.append(las[:len(las)-1])
w.append(Total_Amount_Rs1)
x.append(Total_Quantity1)
y.append(Total_No_of_Transactions1)

time.sleep(d_sleep)

while iteration < t_iteration:
    
    data1 = s[7]
    Total_Amount_Rs = data1[17:]

    data2 = s[8]
    Total_Quantity = data2[15:]

    data3 = s[9]
    Total_No_of_Transactions = data3[25:]
    
    
    nl = []

    
    No_Of_Transaction = data_array[1]
    Max_Price = data_array[2]
    Min_Price = data_array[3]
    Closing_Price = data_array[4]
    Traded_Shares = data_array[5]
    Amount = data_array[6]
    Previous_Closing = data_array[7]
    las = data_array[8]
    Difference_Rs = las[:len(las)-1]
    nl.append(No_Of_Transaction)
    nl.append(Max_Price)
    nl.append(Min_Price)
    nl.append(Closing_Price)
    nl.append(Traded_Shares)
    nl.append(Amount)
    nl.append(Previous_Closing)
    nl.append(Difference_Rs)
    nl.append(Total_Amount_Rs)
    nl.append(Total_Quantity)
    nl.append(Total_No_of_Transactions)
    c_date = date.today().strftime("%B %d, %Y")
    c_time = datetime.now().strftime("%H:%M:%S")

    
    if nnl != nl:
        l.append(data_array[0])
        m.append(c_date)
        n.append(c_time)
        o.append(data_array[1])
        p.append(data_array[2])
        q.append(data_array[3])
        r.append(data_array[4])
        ss.append(data_array[5])
        t.append(data_array[6])
        u.append(data_array[7])
        las = data_array[8]
        v.append(las[:len(las)-1])
        w.append(Total_Amount_Rs)
        x.append(Total_Quantity)
        y.append(Total_No_of_Transactions)
        time.sleep(d_sleep)
        nnl = nl
        iteration = iteration + 1
    else:
        iteration = iteration + 1

   



liss = []

liss.append(o[0])
liss.append(p[0])
liss.append(q[0])
liss.append(r[0])
liss.append(ss[0])
liss.append(t[0])
liss.append(u[0])
liss.append(v[0])
liss.append(w[0])
liss.append(x[0])
liss.append(y[0])

if liss == lis:
    l.remove(l[0])
    m.remove(m[0])
    n.remove(n[0])
    o.remove(o[0])
    p.remove(p[0])
    q.remove(q[0])
    r.remove(r[0])
    ss.remove(ss[0])
    t.remove(t[0])
    u.remove(u[0])
    v.remove(v[0])
    w.remove(w[0])
    x.remove(x[0])
    y.remove(y[0])
    


df = pd.DataFrame({'Company Name': l,
                   'Date': m,
                  'Time': n,
                  'No. Of Transaction': o,
                   'Max Price': p,
                 'Min Price': q,
                  'Closing Price': r,
                  'Traded Shares': ss,
                   'Amount': t,
                 'Previous Closing': u,
                   'Difference Rs.': v,
                   'Total Amount Rs.': w,
                   'Total Quantity': x,
                   'Total No of Transactions': y,
                  })
df.to_excel("C:/Users/rosha/Desktop/stock0.xlsx") 


