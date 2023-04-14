from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver.exe")

url = "https://www.naver.com"

#네이버로 이동
driver.get(url)

#3초 정지
#통신이 좋지 않거나, 딜레이가 걸릴 것 같을때 타임을 사용할 수 있다.
time.sleep(3)

#2번째 페이지로 이동
url = "https://www.daum.net"
driver.get(url) #다음으로 이동

#스크래핑을 끝내고 웹 브라우저 종료시 사용
driver.quit()