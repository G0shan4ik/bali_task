# import requests
# from bs4 import BeautifulSoup
# import lxml
# from pprint import pprint
#
#
# def update_dict(dct: dict) -> dict:
#     # response = requests.get(
#     #     url='https://app.scrapingbee.com/api/v1/',
#     #     params={
#     #         'api_key': 'KB7FUUC6C41UNZK19DIHNAICI6X9EGVOZ2VO0LCSF2RHLQL5IJLH92G66UK02OCABQASD16MUW0PKE3D',
#     #         'url': 'https://www.carousell.ph/p/nike-acg-1320201724/?t-id=0n54uSdKTa_1723817799840&t-referrer_browse_type=categories&t-referrer_category_id=5130&t-referrer_page_type=category_browse&t-referrer_request_id=oUP3nO8FQqi7autO&t-referrer_sort_by=popular&t-tap_index=0',
#     #         'premium_proxy': 'true',
#     #         'country_code': 'sg',
#     #         'wait': '1000'
#     #     },
#     #
#     # )
#
#     # with open('card.html', "w", encoding="utf-8") as f:
#     #     f.write(response.text)
#
#     with open('card.html', "r", encoding="utf-8") as f:
#         content = f.read()
#
#     soup = BeautifulSoup(content, 'lxml')
#
#     images = soup.select_one('div#FieldSetGroup-Container-photo_group').select('img')
#     brand_size = soup.select_one('div#FieldSetField-Container-field_description_info').select('span')
#     descr = soup.select_one('div#FieldSetField-Container-field_description').text.replace('\n', ' ').strip()
#
#     cramps = [item.text for item in soup.select_one('ul[data-testid="new-listing-details-page-desktop-breadcrumbs"]').select('a')]
#     gender, category, subcategory = '-', '-', '-'
#     try:
#         gender, category, subcategory = cramps
#     except:
#         try:
#             gender, category = cramps
#         except:
#             try:
#                 gender = cramps[0]
#             except:
#                 ...
#
#     dct["Gender"] = gender
#     dct["Category"] = category
#     dct["Subcategory"] = subcategory
#     dct["Images"] = " ".join([item.get('src') for item in images])
#     dct["Condition"] = f"{soup.select_one('div#FieldSetField-Container-field_condition_with_action').text}"
#     dct["Location"] = f"{soup.select_one('div#FieldSetField-Container-field_sticky_info').select('p')[-1].text}"
#     dct["Brand"] = f"{brand_size[-2].text}"
#     dct["Size"] = f"{brand_size[-1].text}"
#     dct["Description"] = descr
#
#     return dct
#
#
# pprint(update_dict({}))
from pprint import pprint


mass = ['https://media.karousell.com/media/photos/products/2024/8/7/rick_owens_tractor_chunky_sand_1723026390_f54e15ca_progressive.jpg', 'https://media.karousell.com/media/photos/products/2024/8/7/rick_owens_tractor_chunky_sand_1723026390_99bd315c_progressive.jpg', 'https://media.karousell.com/media/photos/products/2024/8/7/rick_owens_tractor_chunky_sand_1723026390_efea4084_progressive.jpg', 'https://media.karousell.com/media/photos/products/2024/8/7/rick_owens_tractor_chunky_sand_1723026390_c773143e_progressive.jpg', 'https://media.karousell.com/media/photos/products/2024/8/7/rick_owens_tractor_chunky_sand_1723026390_ea6bfddd_progressive.jpg', 'https://media.karousell.com/media/photos/products/2024/8/7/rick_owens_tractor_chunky_sand_1723026390_addcd6f3_progressive.jpg']

print([{"url": item} for item in mass])