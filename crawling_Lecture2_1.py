#%%
import requests
from bs4 import BeautifulSoup
import pandas as pd

page_list = []
#전체 총 400페이지
for i in range(1,3992,10) : 
    page_list.append(str(i))
#print(page_list)

#한페이지
#raw = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=딥러닝')

#페이지의 규칙성을 확인하고, 여러 페이지의 뉴스를 저장하기
title_list = []     #제목을 담을 빈 리스트
content_list = []   #내용을 담을 빈 리스트

for page in page_list :
    raw = requests.get(f'https://search.naver.com/search.naver?where=news&sm=tab_pge&query=%EB%94%A5%EB%9F%AC%EB%8B%9D&sort=0&photo=0&field=0&pd=0&ds=&de=&cluster_rank=32&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so:r,p:all,a:all&start={page}')
    html = BeautifulSoup(raw.text, "html.parser")
    #==================================================

    articles = html.select("ul.list_news > li") #뉴스 기사 요소 덩어리

    #뉴스 제목과 내용을 추출하여 csv 파일로 저장하기
    for i in range(len(articles)) :
        #뉴스 제목 추출
        title = articles[i].select_one('a.news_tit').text  # list_news > li 에서 a.new_tit의 text 추출
        title_list.append(title)    #제목 리스트에 추가

        #뉴스 내용 추출
        content = articles[i].select_one('div.dsc_wrap').text # 뉴스 overview 내용 가져오기
        content_list.append(content)    #내용 리스트에 추가

#딕셔너리 생성
sdict = {'제목': title_list,        #제목 list를 제목 컬럼의 값으로 넣기 
         '내용': content_list}      #내용 list를 내용 컬럼의 값으로 넣기

title_content = pd.DataFrame(sdict) #sdict 딕셔너리를 title_content 데이터 프레임으로 변환
title_content.to_csv("./naver_news_crawling_result.csv", index=False)   #title_content 데이터 프레임을 csv 파일로 저장
