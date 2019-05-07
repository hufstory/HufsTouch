from selenium import webdriver
from bs4 import BeautifulSoup as bs4
import time

driver = webdriver.Chrome('/Users/gobyeonghag/Documents/vscode_workspace/chromedriver')
driver.implicitly_wait(3)

urls = {
    #자연대
    'math':'http://builder.hufs.ac.kr/user/indexSub.action?framePath=unknownboard&siteId=math&dum=dum&boardId=20197155&page=1&command=list',
    'statistic':'http://builder.hufs.ac.kr/user/indexSub.action?framePath=unknownboard&siteId=stat2&dum=dum&boardId=84502583&page=1&command=list',
    'physics':'http://builder.hufs.ac.kr/user/indexSub.action?framePath=unknownboard&siteId=physics&dum=dum&boardId=6923983&page=1&command=list',
    'bio':'http://builder.hufs.ac.kr/user/indexSub.action?framePath=unknownboard&siteId=bio&dum=dum&boardId=1025968&page=1&command=list',
    #화학과는 공지 안씀
    'chemi':'http://builder.hufs.ac.kr/user/indexSub.action?framePath=unknownboard&siteId=chem&dum=dum&boardId=6777189&page=1&command=list',
    #예외처리 필요
    'envi':'http://www.envi.hufs.ac.kr/contents/layout.asp?link_type=3&table_id=A0&cate_id=F001',

    #공대
    'ces' : "http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=43628219&siteId=ces&menuType=T&uId=6&sortChar=AA&linkUrl=5_1.html&mainFrame=right",
    'ice':'http://builder.hufs.ac.kr/user/indexSub.action?framePath=unknownboard&siteId=ice&dum=dum&boardId=119774575&page=1&command=list',
    'ee':'http://builder.hufs.ac.kr/user/indexSub.action?framePath=unknownboard&siteId=hufsece&dum=dum&boardId=23011534&page=1&command=list',
    'ime':'http://builder.hufs.ac.kr/user/indexSub.action?framePath=unknownboard&siteId=ime&dum=dum&boardId=69047159&page=1&command=list',

    #바메
    'bme':'http://builder.hufs.ac.kr/user/indexSub.action?framePath=unknownboard&siteId=bme&dum=dum&boardId=68967985&page=1&command=list',

    #통대
    'jp' : "http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=24920747&siteId=hufsjp&menuType=T&uId=4&sortChar=A&linkUrl=4_1.html&mainFrame=right",
    'english':'http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=93090369&siteId=englishit&menuType=T&uId=3&sortChar=A&menuFrame=left&linkUrl=3_3.html&mainFrame=right',
    'deutsch':'http://builder.hufs.ac.kr/user/indexSub.action?framePath=unknownboard&siteId=hufsdeutsch&dum=dum&boardId=63263791&page=1&command=list',
    #스통
    'hufsit' : 'http://builder.hufs.ac.kr/user/indexSub.action?framePath=unknownboard&siteId=hufses&dum=dum&boardId=110290868&page=1&command=list',
    'italy':'http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=8813736&siteId=italia&menuType=E&uId=7&sortChar=AA&linkUrl=2_1.html&mainFrame=right',
    'china':'http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=39471832&siteId=china3&menuType=T&uId=8&sortChar=A&menuFrame=left&linkUrl=3_1.html&mainFrame=right',
    #아통 안씀
    'ait':'http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=69930918&siteId=ait&menuType=T&uId=4&sortChar=A&menuFrame=left&linkUrl=4_1.html&mainFrame=right',
    #말레이인도네시아 (회원권한 필요)
    #'bahasa':'http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=53002299&siteId=bahasa&menuType=T&uId=4&sortChar=A&menuFrame=left&linkUrl=4_1.html&mainFrame=right',
    #태통 안씀
    'thai':'http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=8897584&siteId=thai&menuType=E&uId=7&sortChar=A&menuFrame=left&linkUrl=2_1.html&mainFrame=right',

    #국지대
    'france':'https://www.hufsfrance.com/notice',
    # 브라질 권한필요
    #'brazil':'http://builder.hufs.ac.kr/user/indexSub.action?framePath=unknownboard&siteId=hufsbrazil&dum=dum&boardId=7377047&page=1&command=list',
    #그리스 불가리아
    'gb':'http://builder.hufs.ac.kr/user/indexSub.action?framePath=unknownboard&siteId=gb&dum=dum&boardId=69931135&page=1&command=list',
    #인도학과 안씀
    'india':'http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=45564044&siteId=hufsindia&menuType=T&uId=4&sortChar=A&menuFrame=left&linkUrl=4_1.html&mainFrame=right',
    'centralAsia' : 'http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=8897497&siteId=centralasia&menuType=E&uId=6&sortChar=A&menuFrame=left&linkUrl=2_1.html&mainFrame=right',
    'africa':'http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=103938524&siteId=africa&menuType=T&uId=7&sortChar=AAE&menuFrame=left&linkUrl=5_1_2.html&mainFrame=right',
    'russia':'http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=23207306&siteId=russianstudied&menuType=E&uId=7&sortChar=AA&linkUrl=2_1.html&mainFrame=right',
    'sport':'http://sporthufs.com/inspot/%EA%B5%AD%EC%A0%9C%EC%8A%A4%ED%8F%AC%EC%B8%A0%EB%A0%88%EC%A0%80%ED%95%99%EB%B6%80-%EA%B3%B5%EC%A7%80%EC%82%AC%ED%95%AD/',
    'korean':'http://builder.hufs.ac.kr/user/indexSub.action?framePath=unknownboard&siteId=koreanstudies&dum=dum&boardId=36212025&page=1&command=list',

    #동유럽
    # 폴란드 권한필요
    #'polski':'http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=59089255&siteId=polski&menuType=T&uId=3&sortChar=A&linkUrl=3-1.html&mainFrame=right',
    'romania':'http://builder.hufs.ac.kr/user/indexSub.action?framePath=unknownboard&siteId=romania&dum=dum&boardId=140040&page=1&command=list',
    'czechandslovak':'http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=4619869&siteId=czeh&menuType=T&uId=6&sortChar=AA&linkUrl=6_1.html&mainFrame=right',
    # 헝가리 권한필요
    #'hungary':'http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=57989320&siteId=hungary&menuType=T&uId=3&sortChar=ABB&menuFrame=left&linkUrl=3_5_2.html&mainFrame=right',
    'yugo':'http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=16442049&siteId=yugo&menuType=T&uId=1&sortChar=A&menuFrame=left&linkUrl=1_9.html&mainFrame=right',
    'ukraine':'http://builder.hufs.ac.kr/user/indexSub.action?codyMenuSeq=18805252&siteId=ukraine&menuType=E&uId=7&sortChar=A&menuFrame=left&linkUrl=2_1.html&mainFrame=right',

    #인문대

    #경상대

}

def getPosts(major, url):
    try:
        for i in range(46):
            driver.get(url)
            #예외처리 필요
            #환경학과 "body > table > tbody > tr > td > table:nth-child(5) > tbody > tr"
            #정통 "#board-container > div.list > form:nth-child(2) > table > tbody > tr"
            #프랑스 "#con0_wrap0 > div.board-wrapper > div.absc.list.rs > table > tbody > tr"
            #국스레 "#kboard-default-list > div.kboard-list > table > tbody > tr"
            posts = driver.find_elements_by_css_selector('#board-container > div.list > form:nth-child(2) > table > tbody > tr')
            print(i, end=", ")
            with posts[i].find_elements_by_css_selector('#mini_eng')[0].text as id_num:
                print(id_num, end=" : ")
            print(posts[i].find_elements_by_css_selector('a')[0].text)
            posts[i].find_elements_by_css_selector('a')[0].click()
            print("url : " + driver.current_url)
            
    except:
        print("ERROR")
        pass

for major, url in urls.items():
    print("==================================================")
    print(major)
    getPosts(major, url)
driver.close()