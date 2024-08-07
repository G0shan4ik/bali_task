import json

import requests
from botasaurus.browser import browser, Driver
from bs4 import BeautifulSoup
from requests import request

from pyairtable import Table

from random import randint


AIRTABLE_TOKEN = 'patGlHaDBAM9XQBxg.96fcbaa9fdb4c971731ccf5dd9cefa7ccc3842a0c74435f3b053b7e26d97eef3'
AIRTABLE_BASE_ID = 'appP155mkCHYI28rl'
AIRTABLE_URL = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}"

url = f"{AIRTABLE_URL}/carousell_table?maxRecords=300&offset"
headers = {
    'Authorization': f'Bearer {AIRTABLE_TOKEN}',
    'Content-Type': 'application/json',
}


def send_to_airtable(data: dict):
    response = request("POST", url, headers=headers, data=json.dumps(data))
    request('DELETE', url, headers=headers)

    return response


def get_all_table_urls() -> list[str]:
    table = Table(api_key=AIRTABLE_TOKEN, base_id=AIRTABLE_BASE_ID, table_name='carousell_table')
    records = table.all()

    return [f"{item['fields']['URL']}" for item in records]


# @browser(
#     add_arguments=['--disable-extensions', '--disable-application-cache', '--disable-gpu', '--no-sandbox',  '--disable-setuid-sandbox', '--disable-dev-shm-usage'],
#     close_on_crash=True,
#     profile='Carousell'
# )
# def carousell_parser(driver: Driver, data: str) -> None:
#     driver.get_via(data, 'https://www.carousell.ph')
#     #  <-- Cloudflare -->
#     driver.sleep(randint(25, 30))
#
#     with open('test.js', 'r', encoding='utf-8') as f:
#         code = f.read()
#         result = driver.run_js(code)
#
#     data_ = get_all_table_urls()
#     for dct in result:
#         print(dct['url'] not in data_)
#         if dct['url'] not in data_:
#             print(dct)
#             send_to_airtable(data={
#                     "records": [
#                         {
#                             "fields": {
#                                 "Name": dct['name'],
#                                 "Price": dct['price'],
#                                 "URL": dct['url'],
#                                 "Photo": [
#                                     {
#                                         "url": dct['image'],
#                                     }
#                                 ]
#                             }
#                         }
#                     ]
#                 }
#             )
#     return

def carousell_parser(data: str):
    response = requests.get(
        url='https://app.scrapingbee.com/api/v1/',
        params={
            'api_key': 'KB7FUUC6C41UNZK19DIHNAICI6X9EGVOZ2VO0LCSF2RHLQL5IJLH92G66UK02OCABQASD16MUW0PKE3D',
            'url': 'https://www.carousell.ph/search/rick%20owens',
            'premium_proxy': 'true',
            'country_code': 'sg'
        },

    )
    result: list[dict] = []

    soup = BeautifulSoup(response.text, 'lxml')
    for item in soup.select('div[data-testid*=listing-card]'):
        __id = int(item.select('a')[-1].get('href').split('/')[2].split('-')[-1])
        result.append({
            "unique_id": __id,
            "image": item.select('img')[-1].get('src'),
            "name": item.select('p')[2].text,
            "price": int(item.select('p')[3].text.replace('PHP ', '').replace(',', '')),
            "url": f"https://www.carousell.ph/p/{__id}",
        })
        continue

    data_ = get_all_table_urls()
    for dct in result:
        print(dct['url'] not in data_)
        if dct['url'] not in data_:
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
        else:
            break
    return


def schedule(all_links):
    cnt = 0
    print("\n\n\n\n\n<--- START --->\n\n\n\n\n")
    while True:
        for link in all_links:
            cnt += 1
            print(f"\n<-- Link: {link} - Num: {all_links.index(link) + 1}-->\n")
            carousell_parser(link)

        print('\n\nsleep\n\n')

        break
