#네이버 금융 크롤링
import requests
from bs4 import BeautifulSoup

# openpyxl은 파이썬에서 엑셀을 다루는 것을 쉽게 해주는 도구
from openpyxl import Workbook

# 네이버 파이낸셜 사이트
url = 'https://finance.naver.com/'

# url 요청
response = requests.get(url)

# 해당 url의 모든 정보를 텍스트 형태로 가져오기
html = response.text

# HTML의 요소 별로 파싱
soup = BeautifulSoup(html, 'html.parser')

# 인기 검색 종목의 테이블 안의 요소를 가져옴
# #container > div.aside > div > div.aside_area.aside_popular > table > tbody
tbody = soup.select_one('#container > div.aside > div > div.aside_area.aside_popular > table > tbody')
#print(tbody)

price_list = tbody.select('td')
slist = tbody.select('a')

count = 0
for i in range(0,len(price_list),2) :
    temp = slist[count]
    #종목코드 위치 가져오기
    #print(str(temp)[str(temp).find("code=")+5:(str(temp).find("code=")+5)+6]) 
    #print(i.text)
    print("종목이름:",temp.text, "종목코드:",str(temp)[str(temp).find("code=")+5:(str(temp).find("code=")+5)+6], \
          "현재가:",price_list[i].text,"전일대비:",price_list[i+1].text)
    count += 1