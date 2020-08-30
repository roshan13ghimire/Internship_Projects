import sys
import requests
import pandas as pd
from bs4 import BeautifulSoup
import json
import time
from datetime import date
from datetime import datetime

stock_code = '403'
t_iteration = 10
d_sleep = 1 

url = 'http://www.nepalstock.com/company/display/' + stock_code
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
data_array = soup.find(id='company-view').getText().strip().split(" ")


for i in data_array:
    if 'Change' in i:
        last_trade_price = i[6:len(i) - 9]
    if i[:4] == '(%)\n' and i[len(i) - 8:] == '\n\n\nTotal':
        change = i[4:len(i)-8]
    if 'Shares' in i:
        total_listed_shares = i[7:len(i) - 8]
    if i[:6] == '(Rs.)\n' and i[len(i) - 8:] == '\n\n\nTotal':
        paid_up_value = i[6:len(i) - 8]
    if 'Closing' in i:
        total_paid_up_value = i[6:len(i)-10]
    if 'Market' in i:
        closing_market_price = i[6:len(i)-9]
    if 'Capitalization' in i:
        da = data_array[data_array.index(i)+1]
        market_capitalization = da[6:]
        
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

while iteration < t_iteration:
    c_date = date.today().strftime("%B %d, %Y")
    c_time = datetime.now().strftime("%H:%M:%S")
    #print (stock_code + ',' + c_date + '  '  + c_time + '  ' + str(last_trade_price) + '  ' + str(change) + '  '  + str(total_listed_shares) + '  ' + str(paid_up_value) + '  ' + str(total_paid_up_value) + '  ' + str(closing_market_price) + '  ' + str(market_capitalization) )
    #print(stock_code + ',' + c_date + ','  + c_time + ',' + str(current_stock_price), file=data_file)
    l.append(stock_code)
    m.append(c_date)
    n.append(c_time)
    o.append(last_trade_price)
    p.append(change)
    q.append(total_listed_shares)
    r.append(paid_up_value)
    s.append(total_paid_up_value)
    t.append(closing_market_price)
    u.append(market_capitalization)
    time.sleep(d_sleep)
    iteration = iteration + 1


df = pd.DataFrame({'Code': l,
                  'Date': m,
                  'Time': n,
                  'Last Traded Price (Rs.)': o,
                   'Change (Rs.) and (%)': p,
                 'Total Listed Shares': q,
                  'Paid Up Value (Rs.)': r,
                  'Total Paid Up Value (Rs.)': s,
                   'Closing Market Price (Rs.)': t,
                 'Market Capitalization (Rs.)': u,
                  })
df.to_excel("C:/Users/rosha/Desktop/stock.xlsx") 
