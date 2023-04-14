#키보드 입력 구현
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome("chromedriver.exe")

url = "https://www.google.com"

driver.get(url)

#검색창 id는 APjFqb로 확인
elem = driver.find_element(By.CSS_SELECTOR, '#APjFqb')

elem.send_keys("코로나") #코로나 검색어 입력
elem.send_keys(Keys.RETURN) #엔터키 입력

#20초 정지
#통신이 좋지 않거나, 딜레이가 걸릴 것 같을때 타임을 사용할 수 있다.
time.sleep(20)