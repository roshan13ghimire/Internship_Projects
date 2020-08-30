import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup
import json
import time
from datetime import date
from datetime import datetime

print("Enter the Company's Name in lower case letter:")
Company_Name = input()

print("Enter the number of iterations that you need to see:")
t_iteration = int(input())

print("Enter the time that you need to check (in sec):")
d_sleep = int(input())


url = 'http://www.nepalstock.com/todaysprice?stock-symbol=' + Company_Name
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
s = soup.find(id='home-contents').getText().split('\n\n\n')

data = s[5]

data1 = s[7]
a = data1[17:]

data2 = s[8]
b = data2[15:]

data3 = s[9]
c = data3[25:]


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
s = []
t = []
u = []
v = []
w = []
x = []
y = []


while iteration < t_iteration:
    c_date = date.today().strftime("%B %d, %Y")
    c_time = datetime.now().strftime("%H:%M:%S")
    l.append(data_array[0])
    m.append(c_date)
    n.append(c_time)
    o.append(data_array[1])
    p.append(data_array[2])
    q.append(data_array[3])
    r.append(data_array[4])
    s.append(data_array[5])
    t.append(data_array[6])
    u.append(data_array[7])
    las = data_array[8]
    v.append(las[:len(las)-4])
    w.append(data_array[7])
    x.append(data_array[7])
    y.append(data_array[7])
    time.sleep(d_sleep)
    iteration = iteration + 1


df = pd.DataFrame({'Company Name': l,
                  'Date': m,
                  'Time': n,
                  'No. Of Transaction': o,
                   'Max Price': p,
                 'Min Price': q,
                  'Closing Price': r,
                  'Traded Shares': s,
                   'Amount': t,
                 'Previous Closing': u,
                   'Difference Rs.': v,
                   'Total Amount Rs.': w,
                   'Total Quantity': x,
                   'Total No of Transactions': y,
                  })
df.to_excel("C:/Users/rosha/Desktop/stock1.xlsx") 