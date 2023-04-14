import requests
from bs4 import BeautifulSoup
url = 'https://kin.naver.com/search/list.naver?query=파이썬'
response = requests.get(url)

# 200(성공) : 서버가 요청을 제대로 처리했다는 뜻
# 네이버 지식인에 파이썬을 검색한 url. 응답 코드가 200 일때, html을 받아와 soup 객체로 변환
if response.status_code == 200 :
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # ul 태그 중 basic1 클래스를 뽑아오는 선택자
    ul = soup.select_one('ul.basic1')
    #print(ul)

    # ul 자식 태그에는 li 태그가 10개
    # 각 li 태그 안에는 dl -> dt -> a 태그 안에 제목이 들어 있다
    # li > dl > dt > a 는 자식 선택자를 이용한 것
    titles = ul.select('li > dl > dt > a')
    print(titles)

    for title in titles : #titles의 리스트 내부를 반복
        print(title.get_text()) #titles에서 제목만 텍스트로 추출

else :
    print(response.status_code)