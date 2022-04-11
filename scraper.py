import requests
from bs4 import BeautifulSoup



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
            print(soup.title.string)
            print(soup.text)
            #print(soup.find('div',id='body'))