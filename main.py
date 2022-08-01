# vishera_qna
# created by Phonedolly at 2022-08-01

import os
import platform
import json
import sys
import time

from webdriver import crawling, webdriver_init


def clear_screen():
    if platform.system() != 'Windows':
        os.system('clear')  # not windows
    else:
        os.system('cls')  # windows


if __name__ == '__main__':
    clear_screen()
    driver = webdriver_init()
    crawling(_driver=driver)
