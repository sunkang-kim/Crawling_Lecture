#유튜브 댓글 크롤링 예제
from selenium import webdriver
import time
import requests
from bs4 import BeautifulSoup

driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.youtube.com/watch?v=8pSC6QgxFzI&t=593s")

driver.execute_script("window.scrollTo(0, 800)")
time.sleep(3)

last_height = driver.execute_script("return document.documentElement.scrollHeight")

#스크롤을 2번 내리는 구문
#while True: # 끝까지 내릴때
for i in range(0,2): # 2번만 내리겠다.
      #스크롤을 내리고
      driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
      #댓글이 다 뜰때까지 기다리기 위해 1.5초 기다림
      time.sleep(1.5)

      # 내린 상태의 높이를 new_height에 저장
      new_height = driver.execute_script("return document.documentElement.scrollHeight")
      # 스크롤이 마지막일때, new_height와 last_height는 같아지게 된다.
      # 그때 break문으로 빠져나가 loop를 돌지 않는다.
      if new_height == last_height: 
            break
      # 내린 상태의 높이 값을 last_height로 재정의
      last_height = new_height

#댓글이 렌더링 될때까지 기다림
time.sleep(10)
#=========================================================댓글 랜더링 부분

html_source = driver.page_source
soup = BeautifulSoup(html_source, 'html.parser')

#댓글의 id 찾기 => id가 autor-text인걸 찾고, span부분
id_list = soup.select("#author-text > span")
#댓글 찾기
content_list = soup.select("#content-text")

import pandas as pd
id_list_zip = []
content_list_zip = []

for i in range(0, len(id_list)) :
      id_list_zip.append(str(id_list[i].text).strip())
      content_list_zip.append(content_list[i].text)
      #print("작성자:",str(id_list[i].text).strip(),"댓글:",comment_list[i].text) #작성자: , 댓글: 방식으로 출력

sdict = {'작성자' : id_list_zip, '댓글': content_list_zip}
you_tube = pd.DataFrame(sdict)
you_tube.to_csv("youtube_result.csv")
#for i in comment_list :
#      print("======================================")
#      print(i.text)

#for i in id_list :
      #print(type(i))
#      print(str(i.text).strip())     #i는 bs4의 객체이기 때문에 text 내장 변수가 있다.
                        #yt-formatted-string 요소 중에 id가 content-text인것들 찾기
