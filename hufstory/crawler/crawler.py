from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

def getList(url_):
    url_ = "http://builder.hufs.ac.kr/user/indexSub.action?framePath=unknownboard&siteId=ces&boardId=43626718"
    html = urlopen(url_)
    soup = bs(html, 'html.parser')
    table = soup.find('table')
    titles = table.find_all(class_='title')

    for title in titles:
        x = title.get_text()
        x = x.replace("\t", "")
        x = x.replace("\n","")
        x = x.strip()
        link = title.a.get('href')
        link = "http://builder.hufs.ac.kr/user/"+link
        print(x)
        print(link)
        getDetail(link)

def getDetail(detail_link):
    detail_html = urlopen(detail_link)
    soup = bs(detail_html, 'html.parser')
    table = soup.find('table')
    contents = table.find(id = 'divView')
    contents = contents.find_all('p')
    for content in contents:
        content = content.get_text()
        content = content.strip()
        print(content)

getList("")