# vishera_qna
# created by Phonedolly at 2022-08-01

import os
import platform
import json
import sys
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


def clear_screen():
    if platform.system() != 'Windows':
        os.system('clear')  # not windows
    else:
        os.system('cls')  # windows


def init() -> webdriver:
    ITER_COUNT = 3
    viewer = []
    titles = []
    scroll_time_pause = 0.75
    count = 0

    # Chrome Web Driver 초기화
    print('Chrome Web Driver 초기화')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # driver.get('https://cafe.naver.com/fx8300?iframe_url=/ArticleList.nhn%3Fsearch.clubid=28173877%26search.menuid=23%26search.boardtype=L')
    driver.get('https://m.cafe.naver.com/ca-fe/web/cafes/28173877/menus/23')
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:

        # 바닥까지 스크롤
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

        # 페이지 로딩까지 기다리기
        time.sleep(scroll_time_pause)
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight - 50)')
        time.sleep(scroll_time_pause)

        # 새 스크롤 weight를 계산하여 마지막 스코롤 weight와 비교
        new_height = driver.execute_script('return document.body.scrollHeight')

        if new_height == last_height:
            more_button = driver.find_element(By.CLASS_NAME, 'u_cbox_btn_more')
            if more_button and count < ITER_COUNT:
                more_button.click()
                scroll_time_pause = 0.1
            else:
                break

        last_height = new_height
        count += 1
        print(count)

    viewer += driver.find_elements(By.CLASS_NAME, 'txt_area')

    for article in viewer:
        try:
            title = article.find_element(By.TAG_NAME, 'strong').text
            if title:
                titles += [title]
        except NoSuchElementException:
            print('제목 없음')

    # driver.get('https://www.naver.com')
    # loginButton = driver.find_element(By.CLASS_NAME, 'link_login')
    # loginButton.click()
    #
    # idHolder = driver.find_element(By.ID, 'id_line').find_element(By.ID, 'id')
    # pwHolder = driver.find_element(By.ID, 'pw_line').find_element(By.ID, 'pw')
    # loginButtonInNid = driver.find_element(By.ID, 'log.login')
    #
    # print('네이버 ID: ')
    # idHolder.send_keys(input())
    # print('네이버 PW: ')
    # pwHolder.send_keys(input())
    # loginButtonInNid.click()
    # driver.

    return driver


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    clear_screen()
    init()
