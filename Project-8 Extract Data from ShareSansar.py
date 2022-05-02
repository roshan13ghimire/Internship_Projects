import requests
from bs4 import BeautifulSoup

Company_Name = input()

url1 = "https://www.sharesansar.com/company/" + Company_Name

response2 = requests.get(url1)
soup2 = BeautifulSoup(response2.text,'html.parser')
s2 = soup2.find("table",{"class":"table table-bordered table-striped table-hover text-center company-table"})


l1 = []
m1 = []
n1 = []
for i in s2.find_all('td'):
    l1.append(i.getText())

if l1[0] == "NO RECORD FOUND":
    print(l1[0])

else:
    for j in range(0,len(l1),2):
        m1.append(l1[j])

    for k in range(1,len(l1),2):
        g = l1[k].replace(" ", "")
        n1.append(g.replace("\n", ""))

    for _ in range(len(m1)):
        print(m1[_] , " : ", n1[_]) 
        
print("\n\n\n")
        
        
        

response1 = requests.get(url1)
soup1 = BeautifulSoup(response1.text,'html.parser')
id = soup1.find("div",{"id":"companyid"}).getText()

sector = soup1.find("div",{"id":"sector"}).getText()


url = "https://www.sharesansar.com/company-quarterly-report?company="+ id + "&symbol=" + Company_Name + "&sector=" + sector

payload={}
headers = {
  'Connection': 'keep-alive',
  'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not\\A"Brand";v="99"',
  'Accept': '*/*',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua-mobile': '?1',
  'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Mobile Safari/537.36',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://www.sharesansar.com/company/slicl',
  'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8,mt;q=0.7',
  'Cookie': '__cfduid=db6834b50a1002a0624cc18bba0ec56cf1615366891; _ga=GA1.2.1422090222.1615366891; _gid=GA1.2.1325355787.1615366891; _gat_gtag_UA_24700594_1=1; XSRF-TOKEN=eyJpdiI6IitUTEg1YVBXZzdjUDZhR2t6K1l0UFE9PSIsInZhbHVlIjoiM0dMRE53ZDZRalBIQVlvZ2hHYzF2S1pRQ1BONkg3VitQU2JDenQwRUVEazYyMnh1dm9QaVAwa2R4SDBXcWNuMiIsIm1hYyI6IjE5ZGFhMGVhNjcwZWVhNDQwYWZhNGMwNzI3YjE2MjFmODUzOWJkZjNkM2FjODI4NmFlMjU2ZDE3YWIxZDEzNDUifQ%3D%3D; sharesansar_session=eyJpdiI6ImxQNVJvOERhenRXK2dTTTdVNFFvYkE9PSIsInZhbHVlIjoiZWdvbjFxb2JhbERnTlRjZStPQ05tTG4wOG92STB5ZUVNbVZ1YlQwdUNTTkZWWVBTSlhpNDRhNkgzcWlmRG9NYlNXMWdZa3lkXC95Wk42alpUUjgzN0V0b09PdEFzWUM0T0I4SkNkTVwvU3ZtaXpFM0NqN3RwSGRJUjlnOW12bUdYKyIsIm1hYyI6IjEzMTA1N2NlYWQwOGRmOThkNGRhMGUwMzA0NTRkZGFhYjIyMmEzZGU4ZjZlNGE5ODQyYzBkMGNmMjdhZDFiYzcifQ%3D%3D; XSRF-TOKEN=eyJpdiI6IkRIZlVDc0tlcDlUYlYxSVNPSHpGYnc9PSIsInZhbHVlIjoiVFI2UUdHYVwvbGY3YVdnOExDVTRaVXdLUlQrZ2dFMTNEV005SW03UER2YllpbWVLdTYyTE9SZWNjTm11cDJKK0IiLCJtYWMiOiI0M2ZmMmJiNDNjMzZkMmJjODY5ZjJmMGQzMjAxZDBlNzI4ZmQ3NmQ3YmFjOTg2MzU0NzZmYjE5M2NiMTFmMTE1In0%3D; sharesansar_session=eyJpdiI6IjNIYlFGNFVYOE9JVDlLMkRGazY1REE9PSIsInZhbHVlIjoicDNBWkk0UzhrbXIzMlUyOHNYczRUQVBid3ZWZmhXMFRUdWRjR3hLOFpjejVJVjdqcDBqMjRkMWx4Y1VVeTFBaVhINmYybmRGRmVrd3RcL0gzUGE0Z29cL1IrcU8xQ2VQVmplUWhKcjJJR2tMU2Q5aWJmYXhjdERrM3h5N3d3V0s5WCIsIm1hYyI6IjNiYjRiOGZiODVlNjIwOWQ1MWU1ZGQ4YWQ0YmQwOTUzYWI4OTVlNDg2MjdiYmM4MzJlNjE4YWE0ZTIwNGMxZjgifQ%3D%3D'
}

response = requests.request("GET", url, headers=headers, data=payload)

soup = BeautifulSoup(response.text, 'html.parser')

l = []
m = []
n = []

s = soup.find("div",{"id":"keyratios"})

if s:
    for i in s.findAll("td"):
        l.append(i.getText())

    for j in range(0,len(l),2):
        m.append(l[j])
    for k in range(1,len(l),2):
        n.append(l[k])
    for _ in range(len(m)):
        print(m[_] , " : " , n[_])
else:
    print("NO DATA AVAILABLE")