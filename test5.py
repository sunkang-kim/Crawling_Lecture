import requests
from bs4 import BeautifulSoup

url = "https://www.naver.com"

result = requests.get(url) # <Response [200]> 반환
print(result)

html = result.text  # html 전체 내용 반환
#print(html)

soup = BeautifulSoup(html, "html.parser") #정해진 규격으로 html을 변환

print(soup)