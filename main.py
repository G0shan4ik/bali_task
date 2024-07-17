from proga.database import init
from proga.parser.main_parser import schedule
from proga.parser.main_parser import carousell_parser

from time import sleep


with open('links', 'r', encoding='utf8') as f:
    all_links: list[str] = list(map(lambda item: item.replace('\n', ''), f.readlines()))

def start_dev():
    init()
    # carousell_parser('https://www.carousell.ph/search/rick%20owens?sort_by=3')
    while True:
        schedule(all_links=all_links)
        sleep(400)

