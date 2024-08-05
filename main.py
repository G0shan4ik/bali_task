from proga.parser.main_parser import schedule

from time import sleep
from random import randint


with open('links', 'r', encoding='utf8') as f:
    all_links: list[str] = list(map(lambda item: item.replace('\n', ''), f.readlines()))

def start_dev():
    while True:
        schedule(all_links=all_links)
        sleep(randint(900, 1900))