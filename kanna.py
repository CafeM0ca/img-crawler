# -*- coding: utf-8 -*- 
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib
import getpass
import re
import os


image_url = []
image_ext = []
reg = re.compile('.*(?P<img>http://cafefiles.naver.net/.*[.][a-z]{3,4})\W{3}')
ext = re.compile('(?P<ext>[.][a-z]{3,4})$')
def NextPage(url,page,num):
    driver.get(url+str(page))
    driver.implicitly_wait(3)
    soup = BeautifulSoup(driver.page_source,'lxml')
    #범위축소 
    images = soup.select('body > table > tbody > tr > td.line-content > span > span')
    check=0
    for image in images:
        m = reg.search(str(image))
        if bool(m):
            e = ext.search(m.group('img'))
            print(m.group('img'))
            image_url.append(m.group('img'))
            image_ext.append(e.group('ext'))
            check=1
        num+=1
    if check == 0:
        return;
    NextPage(url,page+1,num)
        

nid = raw_input("ID: ")
npw = getpass.getpass("PW is blinding : ")
print "wait. . ."
driver = webdriver.Chrome('/home/moca/coding/python/chromedriver')
driver.implicitly_wait(1)

#id/pw sned
driver.get('https://nid.naver.com/nidlogin.login')
driver.find_element_by_name('id').send_keys(nid)
driver.find_element_by_name('pw').send_keys(npw)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
print "Login Completed"
#정규표현식 컴파일
#이미지 따올 첫번째 url
url = 'view-source:cafe.naver.com/ArticleList.nhn?search.clubid=24494762&search.menuid=7&search.boardtype=I&search.questionTab=A&search.totalCount=1351&search.page='


p = input("url page: ")
if p <= 0:
    print "page number error"
    exit();
n=1
NextPage(url,p,n)

#현재 디렉토리에 ./kanna 만들기 
if not os.path.isdir('./kanna'):
    print "현재 디렉토리에 /kanna를 생성합니다."
    os.mkdir('./kanna')
n=0
print os.getcwd()+"./kanna <-에 저장"
print "저장중 . . ."

for image in image_url:    
    urllib.urlretrieve(str(image_url[n]),"./kanna/kanna"+str(n+1)+str(image_ext[n]))
    n+=1
os.system("clear")
print "모든 이미지 파싱&저장이 끝났습니다."
driver.close()
