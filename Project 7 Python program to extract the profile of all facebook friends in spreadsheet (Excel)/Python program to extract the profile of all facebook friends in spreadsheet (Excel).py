import requests
from bs4 import BeautifulSoup
import os,sys,random,time
from selenium import webdriver
import pandas as pd

url = 'https://m.facebook.com/friends/center/friends/?mff_nav=1'

browser = webdriver.Chrome("C:/Users/rosha/Desktop/chromedriver.exe")
browser.get("https://m.facebook.com/login.php")

username = ''              #Your email
password = ''              #Your Password

elementID = browser.find_element_by_id('m_login_email')
elementID.send_keys(username)

elementID = browser.find_element_by_id('m_login_password')
elementID.send_keys(password)

elementID.submit()


browser.get(url)

SCROLL_PAUSE_TIME = 1

last_height = browser.execute_script("return document.body.scrollHeight")

 

while True:

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")


    time.sleep(SCROLL_PAUSE_TIME)

    new_height = browser.execute_script("return document.body.scrollHeight")

    if new_height == last_height:

        break

    last_height = new_height


page = BeautifulSoup(browser.page_source, 'html.parser')
content = page.find_all('a', {'class':"darkTouch"})

z = []
y = []
x = []
w = []
v = []
u = []
t = []
s = []

l = []
for contact in content:
    l.append(contact.get('href'))
for i in range(len(l)):
    if l[i][:12] != '/profile.php':
        name = 'https://m.facebook.com/' + l[i]
        browser.get(name)

        page2 = BeautifulSoup(browser.page_source, 'html.parser')
        co = page2.find('h3', {'class':"_6x2x"}).getText()  
        s.append(co)


        nurl = 'https://m.facebook.com/' + l[i] + '/about'
        browser.get(nurl)
        page = BeautifulSoup(browser.page_source, 'html.parser')
        d = []
        for i in page.find_all('div',{'class': '_55x2 _5ji7'}):
            a = i.getText()
            d.append(a)
    
        k = []
        for j in page.find_all('div', {'class': '__gx'}):
            b = j.getText()
            k.append(b)
    
        for a in range(len(d)):
            print(k[a] , ':' ,  d[a])
            print('\n')
    
        if 'Education' in k:
            h = k.index('Education')
            z.append(d[h])
        else:
            z.append('-')
        if 'Places lived' in k:
            q = k.index('Places lived')
            y.append(d[q])
        else:
            y.append('-')
        if 'Contact Info' in k:
            e = k.index('Contact Info')
            x.append(d[e])
        else:
            x.append('-')
        if 'Basic info' in k:
            r = k.index('Basic info')
            w.append(d[r])
        else:
            w.append('-')
        if 'Family members' in k:
            b = k.index('Family members')
            v.append(d[b])
        else:
            v.append('-')
        if 'Life events' in k:
            c = k.index('Life events')
            u.append(d[c])
        else:
            u.append('-')
        if 'Relationship' in k:
            r = k.index('Relationship')
            t.append(d[r])
        else:
            t.append('-')

        

df = pd.DataFrame({'Name': s,
                  'Education': z,
                  'Places lived': y,
                  'Contact Info':x ,
                   'Basic info':w ,
                   'Family members':v ,
                   'Life events':u ,
                   'Relationship':t,
                  })
df.to_excel("C:/Users/rosha/Desktop/face.xlsx")


