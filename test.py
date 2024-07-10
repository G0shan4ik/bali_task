import json

import requests

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

for _ in range(3):
    print(send_to_airtable(data={
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
        ]
    }))


# with open('index.html', 'w', encoding='utf-8') as f:
#     f.write(driver.page_html)
# driver.sleep(10)