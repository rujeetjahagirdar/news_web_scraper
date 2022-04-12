import requests
from bs4 import BeautifulSoup
import re



with open('news_urls.txt','r') as f:
    urls=f.read().splitlines()
    print(type(urls))
    for url in urls:
        if(url[0]=='#'):
            continue
        else:
            print("url=",url)
            resp = requests.get(url)
            print(resp)
            soup = BeautifulSoup(resp.content, 'html.parser')
            print("Title:",soup.title.string)
            #print(soup.text)
            result=str(soup.find_all('div',class_='Article__subtitle'))
            l1=result.split('<')
            l2=[]
            regex = re.compile('[\[\]@_!#$%^&*()<>?/\|}{~:]')
            for i in l1:
                for j in i.split('>'):
                    if(regex.search(j)== None):
                        l2.append(j)
            print("Author:",l2[0])
            print("Date:",l2[2])