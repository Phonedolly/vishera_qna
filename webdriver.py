import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

ITER_COUNT = 3


def webdriver_init() -> webdriver:
    # Chrome Web Driver 초기화
    print('Chrome Web Driver 초기화')
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def crawling(_driver: webdriver) -> None:
    viewer = []
    titles = []
    scroll_time_pause = 0.75
    count = 0

    _driver.get('https://m.cafe.naver.com/ca-fe/web/cafes/28173877/menus/23')
    last_height = _driver.execute_script("return document.body.scrollHeight")

    while True:

        # 바닥까지 스크롤
        _driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

        # 페이지 로딩까지 기다리기
        time.sleep(scroll_time_pause)
        _driver.execute_script('window.scrollTo(0, document.body.scrollHeight - 50)')
        time.sleep(scroll_time_pause)

        # 새 스크롤 weight를 계산하여 마지막 스코롤 weight와 비교
        new_height = _driver.execute_script('return document.body.scrollHeight')

        if new_height == last_height:
            try:
                more_button = _driver.find_element(By.CLASS_NAME, 'u_cbox_btn_more')
                if more_button and count < ITER_COUNT:
                    more_button.click()
                    scroll_time_pause = 0.1
                else:
                    break
            except NoSuchElementException:
                print("맨 아래에 도달")
                break

        last_height = new_height
        count += 1

    viewer += _driver.find_elements(By.CLASS_NAME, 'txt_area')

    for article in viewer:
        title = article.find_element(By.TAG_NAME, 'strong').text
        if title:
            titles += [title]

    with open('data.txt', 'w') as f:
        for title in titles:
            f.write(title + '\n')

    _driver.quit()
