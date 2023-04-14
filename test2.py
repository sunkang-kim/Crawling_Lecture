#클릭으로 다음 페이지 이동
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome("chromedriver.exe")

url = "https://www.naver.com"

#네이버로 이동
driver.get(url)

#웹툰 버튼 클릭
driver.find_element(By.CSS_SELECTOR,'#NM_FAVORITE > div.group_nav > ul.list_nav.NM_FAVORITE_LIST > li:nth-child(8) > a').click()

time.sleep(5) #5초 대기 후 이동

#베스트 도전 버튼 클릭
driver.find_element(By.CSS_SELECTOR,'#menu > li:nth-child(3) > a').click()

#200초 정지
#통신이 좋지 않거나, 딜레이가 걸릴 것 같을때 타임을 사용할 수 있다.
time.sleep(200)