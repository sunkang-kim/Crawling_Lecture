import requests
from bs4 import BeautifulSoup
url = 'https://kin.naver.com/search/list.naver?query=파이썬'
response = requests.get(url)

# 200(성공) : 서버가 요청을 제대로 처리했다는 뜻
# 네이버 지식인에 파이썬을 검색한 url. 응답 코드가 200 일때, html을 받아와 soup 객체로 변환
if response.status_code == 200 :
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    #print(soup) #parsing 된 html의 전체 내용 출력

    #select_one은 하나의 html 요소를 찾는 함수
    title = soup.select_one('#s_content > div.section > ul > li:nth-child(1) > dl > dt > a') #검색 후 첫번째 제목
    print(title)    #첫번째 제목에 해당하는 html 코드 출력

    #텍스트만 뽑아오고 싶다면 get_text() 함수를 이용
    print(title.get_text())

else :
    print(response.status_code)