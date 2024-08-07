#  Install the Python Requests library:
# pip install requests
import requests
from bs4 import BeautifulSoup
import lxml
from pprint import pprint


def send_request():
    # response = requests.get(
    #     url='https://app.scrapingbee.com/api/v1/',
    #     params={
    #         'api_key': 'KB7FUUC6C41UNZK19DIHNAICI6X9EGVOZ2VO0LCSF2RHLQL5IJLH92G66UK02OCABQASD16MUW0PKE3D',
    #         'url': 'https://www.carousell.ph/search/rick%20owens',
    #         'premium_proxy': 'true',
    #         'country_code': 'sg'
    #     },
    #
    # )
    # with open('index.html', 'w', encoding='utf-8') as f:
    #     f.write(response.text)

    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'lxml')
    mass = []
    cnt = 0
    for item in soup.select('div[data-testid*=listing-card]'):
        cnt += 1
        print(cnt)
        __id = int(item.select('a')[-1].get('href').split('/')[2].split('-')[-1])
        print(__id)
        mass.append({
            "unique_id": __id,
            "image": item.select('img')[-1].get('src'),
            "name": item.select('p')[2].text,
            "price": int(item.select('p')[3].text.replace('PHP ', '').replace(',', '')),
            "url": f"https://www.carousell.ph/p/{__id}",
        })
        continue
    pprint(mass)
    print(len(mass))
    # print('Response HTTP Status Code: ', response.status_code)
    # print('Response HTTP Response Body: ', response.content)


send_request()