import json

import requests
from bs4 import BeautifulSoup
from requests import request
import lxml

from pyairtable import Table

from time import sleep


API_KEY = ""
AIRTABLE_TOKEN = ''
AIRTABLE_BASE_ID = ''
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


def update_dict(dct: dict) -> dict:
    response = requests.get(
        url='https://app.scrapingbee.com/api/v1/',
        params={
            'api_key': API_KEY,
            'url': dct['true_url'],
            'premium_proxy': 'true',
            'country_code': 'sg',
            'wait': '1000'
        },

    )

    soup = BeautifulSoup(response.text, 'lxml')

    images = soup.select_one('div#FieldSetGroup-Container-photo_group').select('img')
    brand_size = soup.select_one('div#FieldSetField-Container-field_description_info').select('span')
    descr = soup.select_one('div#FieldSetField-Container-field_description').text.replace('\n', ' ').strip()

    cramps = [item.text for item in soup.select_one('ul[data-testid="new-listing-details-page-desktop-breadcrumbs"]').select('a')]
    gender, category, subcategory = '-', '-', '-'
    try:
        gender, category, subcategory = cramps
    except:
        try:
            gender, category = cramps
        except:
            try:
                gender = cramps[0]
            except:
                ...

    dct["Gender"] = gender
    dct["Category"] = category
    dct["Subcategory"] = subcategory
    dct["Images"] = [item.get('src') for item in images]
    dct["Condition"] = f"{soup.select_one('div#FieldSetField-Container-field_condition_with_action').text}"
    dct["Location"] = f"{soup.select_one('div#FieldSetField-Container-field_sticky_info').select('p')[-1].text}"
    dct["Brand"] = f"{brand_size[-2].text}"
    dct["Size"] = f"{brand_size[-1].text}"
    dct["Description"] = descr

    return dct


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
            'api_key': API_KEY,
            'url': data,
            'premium_proxy': 'true',
            'country_code': 'sg'
        },

    )
    # with open("index.html", "r", encoding='utf-8') as f:
    #     content = f.read()
    result: list[dict] = []

    soup = BeautifulSoup(response.text, 'lxml')
    # soup = BeautifulSoup(content, 'lxml')

    for item in soup.select('div[data-testid*=listing-card]'):
        __id = int(item.select('a')[-1].get('href').split('/')[2].split('-')[-1])

        result.append({
            "true_url": f"https://www.carousell.ph{item.select('a')[1].get('href')}",
            "unique_id": __id,
            "name": item.select('p')[2].text,
            "price": int(item.select('p')[3].text.replace('PHP ', '').replace(',', '')),
            "url": f"https://www.carousell.ph/p/{__id}",
            "Seller": f'''@{item.select_one('p[data-testid="listing-card-text-seller-name"]').text}'''
        })
        continue

    data_ = get_all_table_urls()
    for dct in result:
        print(dct['url'] not in data_)
        if dct['url'] not in data_:

            dct = update_dict(dct)  # new func

            # print(dct)

            send_to_airtable(data={
                    "records": [
                        {
                            "fields": {
                                "Name": dct['name'],
                                "Price": dct['price'],
                                "URL": dct['url'],
                                "Photo": [{"url": item} for item in dct["Images"]],
                                "Gender": dct["Gender"],
                                "Category": dct["Category"],
                                "Subcategory": dct["Subcategory"],
                                "Condition": dct["Condition"],
                                "Location": dct["Location"],
                                "Brand": dct["Brand"],
                                "Size": dct["Size"],
                                "Description": dct["Description"],
                                "Seller": dct["Seller"],
                            }
                        }
                    ]
                }
            )
            sleep(1000)
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
