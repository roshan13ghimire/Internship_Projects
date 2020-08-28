import requests
from bs4 import BeautifulSoup

Book_Name = input()
Modify_Book_Name = ''
Save_Book_Name = ''

for i in Book_Name:
    if i == ' ':
        Modify_Book_Name += '+'
        Save_Book_Name += '_'
    else:
        Modify_Book_Name += i
        Save_Book_Name += i

url = 'http://libgen.rs/search.php?req=' + str(Modify_Book_Name)
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

links  = soup.findAll('a')
url_list = []
for i in links:
    if '[1]' in i:
        url_list.append(str(i))
        
        
one_link = url_list[0]        
link = one_link.split()
final_link = link[1]
final_url = final_link[6:len(final_link)-1]

response1 = requests.get(final_url)
soup1 = BeautifulSoup(response1.text, 'html.parser')

links1  = soup1.findAll('a')
one_link1 = str(links1[0])
link1 = one_link1.split()
final_link1 = link1[1]
final_url1 = final_link1[6:len(final_link1)-9]


r = requests.get(final_url1, allow_redirects=True)

Save = 'C:/Users/rosha/Desktop/' + Save_Book_Name + '.pdf'

open(Save, 'wb').write(r.content)
    
