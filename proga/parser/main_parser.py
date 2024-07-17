import json

from botasaurus.browser import browser, Driver
from requests import request
from selenium.webdriver import ActionChains

from proga.database import Products
from bs4 import BeautifulSoup
import lxml

from time import sleep
from random import uniform


def send_to_airtable(data: dict):
    AIRTABLE_TOKEN = 'patGlHaDBAM9XQBxg.96fcbaa9fdb4c971731ccf5dd9cefa7ccc3842a0c74435f3b053b7e26d97eef3'
    AIRTABLE_BASE_ID = 'appP155mkCHYI28rl'
    AIRTABLE_URL = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}"

    url = f"{AIRTABLE_URL}/carousell_table"
    headers = {
        'Authorization': f'Bearer {AIRTABLE_TOKEN}',
        'Content-Type': 'application/json'
    }

    response = request("POST", url, headers=headers, data=json.dumps(data))

    return response


def check_match(dct: dict) -> bool:
    _select = Products.select().where(Products.unique_id == dct['unique_id'])
    if _select.exists():
        print(True)
        return True
    Products.create(**dct)
    print(False)
    return False


@browser(
    raise_exception=True,
    # profile='Carousell',
    # add_arguments=['--disable-dev-shm-usage', '--no-sandbox'],
    # headless=True,
    add_arguments=['--disable-extensions', '--disable-application-cache', '--disable-gpu', '--no-sandbox',
                   '--disable-setuid-sandbox', '--disable-dev-shm-usage']

)
def carousell_parser(driver: Driver, data: str) -> None:
    # driver.run_js('''
    #             delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
    #             delete window.cdc_adoQpoasnfa76pfcZLmcfl_JSON;
    #             delete window.cdc_adoQpoasnfa76pfcZLmcfl_Object;
    #             delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
    #             delete window.cdc_adoQpoasnfa76pfcZLmcfl_Proxy;
    #             delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;''')
    # driver.google_get(data)
    driver.get_via(data, 'https://www.carousell.ph')
    #  <-- Cloudflare -->

    # element = driver.select('h1')
    # action = ActionChains(driver)
    # action.move_to_element_with_offset(element, -20, -10).click().perform()

    driver.sleep(uniform(20, 30))

    # driver.save_screenshot('dddd.png')

    # print(driver.run_js("return Array.from(document.querySelectorAll('[data-testid]')).filter(el => el.getAttribute('data-testid').match(/listing-card-\d*$/g))"))

    # driver.run_js('window.scrollTo(0, 2500)')

    # soup = BeautifulSoup(driver.page_html, 'lxml')
    with open('test.js', 'r', encoding='utf-8') as f:
        code = f.read()
        result = driver.run_js(code)

    for dct in result:
        # print(dct)
        # data = card.select_one('img.D_jW.D_RJ')
        # __id = int(card.select_one('div.D_nS').get('data-testid').split('-')[-1])
        # dct = {
        #     'unique_id': __id,
        #     'name': card.select_one('img.D_lm.D_RG').get('title'),
        #     'price': int(card.select_one('p.D_jY.D_jZ.D_ke.D_kg.D_kk.D_kn.D_ku').text.replace('PHP ', '').replace(',', '')),
        #     'image': card.select_one('img.D_lm.D_RG').get('src').replace('_progressive_thumbnail', ''),
        #     'url': f"https://www.carousell.ph/p/{__id}" document.querySelector("#main > div.D_Gz > div > section.D_GL > div.D_GQ > div > div > div:nth-child(2) > div:nth-child(2) > div > div.D_nv > a:nth-child(2)")
        # }
        # dct = {
        #     'unique_id': __id,
        #     'name': card.select_one('img.D_lm.D_RG').get('title'),
        #     'price': int(card.select_one('p.D_jY.D_jZ.D_ke.D_kg.D_kk.D_kn.D_ku').text.replace('PHP ', '').replace(',', '')),
        #     'image': card.select_one('//*[@id="img-0"]'),
        #     'url': f"https://www.carousell.ph/p/{__id}"
        # }

        if not check_match(dct=dct):
            print(dct)
            send_to_airtable(data={
                    "records": [
                        {
                            "fields": {
                                "Name": dct['name'],
                                "Price": dct['price'],
                                "URL": dct['url'],
                                "Photo": [
                                    {
                                        "url": dct['image'],
                                    }
                                ]
                            }
                        }
                    ]
                }
            )


def schedule(all_links):
    cnt = 0
    print("\n\n\n\n\n<--- START --->\n\n\n\n\n")
    while True:
        for link in all_links:
            cnt += 1
            print(f"\n<-- Link: {link} -->\n")
            carousell_parser(link)

        print('\n\nsleep\n\n')

        break
