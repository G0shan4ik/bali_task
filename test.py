import json
from ast import literal_eval

import requests
from requests import request

dct = {
    'Name': 'RICK OWENS CHAIN BRACELET IN STERLING SILVER  (authentic)',
    'Price': 6.0,
    'URL': 'https://www.carousell.ph/p/1309928650',
    'Photo': 'https://media.karousell.com/media/photos/products/2024/6/21/rick_owens_chain_bracelet_in_s_1718943509_f87332e6.jpg'
}


def send_to_airtable(data: dict):
    AIRTABLE_TOKEN = 'patGlHaDBAM9XQBxg.96fcbaa9fdb4c971731ccf5dd9cefa7ccc3842a0c74435f3b053b7e26d97eef3'
    AIRTABLE_BASE_ID = 'appP155mkCHYI28rl'
    AIRTABLE_URL = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}"

    # del data['id']

    url = f"{AIRTABLE_URL}/carousell_table"
    headers = {
      'Authorization': f'Bearer {AIRTABLE_TOKEN}',
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=json.dumps(data))

    return response


new_data = {
    "records": [
        {
            "fields": {
                'Name': 'RICK OWENS CdsfgHAIN BRACELET IN STERLING SILVER  (authentic)',
                'Price': 6,
                'URL': 'https://www.carousell.ph/p/1309928650',
                'Photo': [
                    {
                        'url': 'https://media.karousell.com/media/photos/products/2024/6/21/rick_owens_chain_bracelet_in_s_1718943509_f87332e6.jpg'
                    }
                ]
            }
        },
        # {
        #     "fields": {
        #         'Name': 'RICK OWENS CdsfgHAIN BRACELET IN STERLING SILVER  (authentic)',
        #         'Price': 63.0,
        #         'URL': 'httdsfgps://www.carousell.ph/p/1309928650',
        #         'Photo': 'https://meddsfgia.karousell.com/media/photos/products/2024/6/21/rick_owens_chain_bracelet_in_s_1718943509_f87332e6.jpg'
        #     }
        # }
    ]
}

# for _ in range(3):
#     print(send_to_airtable(data={
#         "records": [
#             {
#                 "fields": {
#                     'Name': 'RICK OWENS CdsfgHAIN BRACELET IN STERLING SILVER  (authentic)',
#                     'Price': 6,
#                     'URL': 'https://www.carousell.ph/p/1309928650',
#                     'Photo': [
#                         {
#                             'url': 'https://media.karousell.com/media/photos/products/2024/6/21/rick_owens_chain_bracelet_in_s_1718943509_f87332e6.jpg'
#                         }
#                     ]
#                 }
#             },
#         ]
#     }))


# with open('index.html', 'w', encoding='utf-8') as f:
#     f.write(driver.page_html)
# driver.sleep(10)
from pyairtable import Table


def foo():
    AIRTABLE_TOKEN = 'patGlHaDBAM9XQBxg.96fcbaa9fdb4c971731ccf5dd9cefa7ccc3842a0c74435f3b053b7e26d97eef3'
    AIRTABLE_BASE_ID = 'appP155mkCHYI28rl'
    AIRTABLE_URL = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}"

    url = f"{AIRTABLE_URL}/carousell_table?maxRecords=300&offset"
    headers = {
        'Authorization': f'Bearer {AIRTABLE_TOKEN}',
        'Content-Type': 'application/json',
    }

    data = request("GET", url, headers=headers)
    request('DELETE', url, headers=headers)
    table = None
    table = Table(api_key=AIRTABLE_TOKEN, base_id=AIRTABLE_BASE_ID, table_name='carousell_table')
    records = table.all()

    # print(*[f"{item['fields']['URL']}" for item in records], sep='\n')

    return literal_eval(data.text)['records']


if __name__ == '__main__':
    from pprint import pprint
    # pprint(foo())
    # mass_id = [item['fields']['URL'] for item in foo()]
    # print(len(mass_id))
    # print(mass_id[1])
    # for item in foo():
    #     print(item['fields']['URL'])
    #     break
