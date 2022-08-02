# vishera_qna
# created by Phonedolly at 2022-08-01

import os
import platform
import json
import sys
import time

from analyze import analyze
from webdriver import crawling, webdriver_init, crawling_routine

TOTAL_URL = 'https://m.cafe.naver.com/ca-fe/fx8300'
QNA_URL = 'https://m.cafe.naver.com/ca-fe/web/cafes/28173877/menus/23'

TOTAL_ITER_COUNT = 500
QNA_ITER_COUNT = 300


def clear_screen():
    if platform.system() != 'Windows':
        os.system('clear')  # not windows
    else:
        os.system('cls')  # windows


if __name__ == '__main__':
    # print('input mode. full(F), total(FREE), qna(QNA), from recent data(FRD): ', end='')
    print('input mode. total(FREE), qna(QNA), from recent data(FRD): ', end='')
    mode = input().upper()
    # if mode == 'F':
    #     analyze(crawling_routine(TOTAL_URL, TOTAL_ITER_COUNT))
    #     analyze(crawling_routine(QNA_URL, QNA_ITER_COUNT))
    if mode == 'FREE':
        analyze(crawling_routine(TOTAL_URL, TOTAL_ITER_COUNT))
    elif mode == 'QNA':
        analyze(crawling_routine(QNA_URL, QNA_ITER_COUNT))
    elif mode == 'FRD':
        f = open('data.txt', encoding='utf-8')
        data = []
        while True:
            file_line = f.readline()
            if not file_line:
                break
            else:
                data += [file_line[:-1]]
        f.close()
        analyze(data)
