import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

ITER_COUNT = 900


def crawling_routine(url: str, iter_count: int) -> list:
    webdriver_init()
    return crawling(_url=url, _iter_count=iter_count)


def webdriver_init() -> webdriver:
    # Chrome Web Driver 초기화
    print('Chrome Web Driver 초기화')
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()))


def crawling(_url: str, _iter_count: int, _driver: webdriver) -> list:
    viewer = []
    titles = []
    scroll_time_pause = 2
    count = 0

    _driver.get(_url)
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
                if more_button and count < iter_count:
                    more_button.click()
                    scroll_time_pause = 0.3  # 로딩이 완료되었으므로 더 빠르게 진행 가능
                else:
                    break
            except NoSuchElementException:
                print("맨 아래에 도달")
                break

        last_height = new_height
        print(count)
        count += 1

    viewer += _driver.find_elements(By.CLASS_NAME, 'txt_area')

    for article in viewer:
        title = article.find_element(By.TAG_NAME, 'strong').text
        if title:
            titles += [title]

    with open('data.txt', 'w', encoding='utf-8') as f:
        for title in titles:
            f.write(title + '\n')

    _driver.quit()

    return titles
