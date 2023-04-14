#이미지 크롤링 연습 - 크림
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
from urllib.request import urlopen

# 크림 덩크 - 신발분류 
url = 'https://kream.co.kr/search?category_id=34&keyword=%EB%8D%A9%ED%81%AC&sort=popular&per_page=40'
driver = webdriver.Chrome('./chromedriver')
driver.get(url)

import time

# 스크롤 기다려주는 시간
SCROLL_PAUSE_TIME = 2

# 마지막 시점의 창 높이 저장
last_height = driver.execute_script("return document.body.scrollHeight")         

#while True:
for i in range(0,2):
    # 창 높이까지 스크롤                                          
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # 스크롤 후 창이 로딩될때까지 2초를 기다리겠다는 명령어. 로딩이 다되면 바로 넘어감
    time.sleep(SCROLL_PAUSE_TIME)

    #한 번에 맨 마지막까지 스크롤되면 아래 리스트가 뜨지 않아서,
    #  마지막을 찍고 조금 창을 올리는 방법으로 리스트가 로딩될 수 있게 함                           
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);")  

    #스크롤 후 창이 로딩될때까지 2초를 기다리겠다는 명령어. 로딩이 다되면 바로 넘어감
    time.sleep(SCROLL_PAUSE_TIME)

    # 스크롤이 된 후의 창 높이를 새로운 높이로 저장          
    new_height = driver.execute_script("return document.body.scrollHeight")

    # 새로운 높이가 이전 높이와 변하지 않았으면 스크롤 종료
    if new_height == last_height:                                                
        break
    last_height = new_height

# 스크롤 다 내렸으면 페이지 모든정보 긁어옴
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

'''
# 모든 가격 요소 불러오기
price = soup.find_all(class_='amount')

# 모든 가격 정보를 jor.txt로 저장
for i in price :
    with open("./jor.txt","a") as f:
        f.write(i.text+'\n')
'''

from urllib.request import urlopen

n=1   #사진 네이밍을 위해 사용하는 변수
# 모든 이미지 불러오기
img2 = soup.find_all(class_='picture product_img')

for i in img2 :
    #print(type(i))     # i의 타입 확인
    # 이미지 url 따오기
    imgUrl = i.find("img")["src"] # i가 bs4 객체이기 때문에 find()를 사용할 수 있음
    
    # 이미지 저장
    # urlopen(imgUrl)은 이미지 데이터
    with urlopen(imgUrl) as f:
        with open('./images/img' + str(n)+'.jpg','wb') as h: # w - write b - binary
            img = f.read()
            h.write(img)
    n += 1
    print(imgUrl)