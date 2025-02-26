# import requests
# from bs4 import BeautifulSoup
#
#
# cookies = {
#     'api_uid': 'rBUqjWdpOs+wkhWjZO4+Ag==',
#     'jrpl': 'EuNf0CjZEh1AlzrFtaB4R6G4LPfYGvMI',
#     'njrpl': 'EuNf0CjZEh1AlzrFtaB4R6G4LPfYGvMI',
#     'dilx': 'XcxgyjbDenqKG5nqmpptU',
#     '_nano_fp': 'Xpmqnp9yXqTjnpTynC_amUld1~sQ6CqeFOj1DSKk',
#     'webp': '1',
#     'quick_entrance_click_record': '20241224%2C473%2C257%2C129',
#     'tubetoken': 'UhRDXBMKi2RSgbpJUUGdA5dITVL%252FWUP7lFfqG3bTVa5SwFAddx0w90ez4Wu0YAvDGcho%252F8pPAZ0RjvaB2eoly%252FCKry5D2yaYA6byQG6EPkASzTMBLOlBaGLCLvMqwdKSeuFI91qSuXiJLcevTVfmJqTBpek0eviq3yn0ni4NUAsEySJEDZ0c7xh7viA%252FLrVUFFCvuAaIC7nBIy0qILi0r6bplghQi38GAXzBwkM%252Bca4%253D',
#     'plp_uid': '16e3e38963594c9d8f4d185d629f518d',
#     'request_id': '9e928d93cf894e4e9c799ad7bb476f62',
#     'rec_list_chat_list_rec_list': 'rec_list_chat_list_rec_list_lhzj3i',
#     'PDDAccessToken': 'K4SV2UOXKTRR3QSKQHINDY2TESCOZS4C2B7X5MKRXXXB3O3VIKLQ122df2b',
#     'pdd_user_id': '7190558516959',
#     'pdd_user_uin': 'S2VP3F6MM4ZL2QCDXFBCZIPO4E_GEXDA',
#     'pdd_vds': 'gaepucureZyDIvIumCnTmusqbClTGqlduYGdLrbfuTmfIqxqLBNdnCbdNeuc',
# }
#
# headers = {
#     'accept': 'application/json',  # Change this to accept JSON
#     'accept-language': 'en-US,en;q=0.9,ky-KG;q=0.8,ky;q=0.7,ru-KG;q=0.6,ru;q=0.5',
#     'cache-control': 'max-age=0',
#     'referer': 'https://mobile.pinduoduo.com/index.html?refer_page_name=personal&refer_page_id=10001_1735268631765_anmq5scbq2&refer_page_sn=10001&page_id=10002_1735268632719_mgfge0dun8&bsch_is_search_mall=&bsch_show_active_page=&item_index=5&count=8&sp=1448&mlist_id=wa3b4t1tfj&last_goods_id=50713146129&is_back=1&list_id=nvmjzmc77m',
#     'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
# }
#
# params = {
#     'goods_id': '50713146129',
#     '_oak_rcto': 'YWJOPgNPdtmEWgJDK5SlLuRnrbb1ULss4EY',
#     '_oc_trace_mark': '199',
#     '_oc_adinfo': 'eyJwYWdlX3NuIjoxMDAwMiwic2NlbmVfaWQiOjUwNn0=',
#     '_oak_gallery_token': '5930ecdeff8888dca50e1aa9ee27a4c9',
#     '_oak_gallery': 'https://img.pddpic.com/goods_mms/2024-03-17/b3a21927-eb90-4d10-a37c-bfd695fa9a8e.jpeg',
#     '_oc_refer_ad': '1',
#     'page_from': '35',
#     'thumb_url': 'https://img.pddpic.com/goods_mms/2024-03-17/b3a21927-eb90-4d10-a37c-bfd695fa9a8e.jpeg?imageMogr2/thumbnail/400x%7CimageView2/2/w/400/q/80/format/webp',
#     'refer_page_name': 'index',
#     'refer_page_id': '10002_1735268632719_mgfge0dun8',
#     'refer_page_sn': '10002',
#     'uin': 'S2VP3F6MM4ZL2QCDXFBCZIPO4E_GEXDA',
# }
#
# # response = requests.get('https://mobile.pinduoduo.com/goods.html', params=params, cookies=cookies, headers=headers)
# # import requests
#
# response = requests.get('https://mobile.pinduoduo.com/goods.html', params=params, cookies=cookies, headers=headers)
#
# # Check if the response is valid
# if response.status_code == 200:
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     # Example: Extract the title of the product (assuming it's in a <title> tag)
#     title = soup.find('title')
#     if title:
#         print("Product Title:", title.get_text())
#
#     # Example: Extract the product price (assuming it's in a specific class or ID)
#     price = soup.find('span', {'class': 'product-price'})
#     if price:
#         print("Product Price:", price.get_text())
#
#     # You can extract other data similarly by identifying the HTML tags and attributes
# else:
#     print(f"Failed to retrieve data. Status code: {response.status_code}")


import requests
import AdvancedHTMLParser
import json

cookies = {
    'api_uid': 'rBUqjWdpOs+wkhWjZO4+Ag==',
    'jrpl': 'EuNf0CjZEh1AlzrFtaB4R6G4LPfYGvMI',
    'njrpl': 'EuNf0CjZEh1AlzrFtaB4R6G4LPfYGvMI',
    'dilx': 'XcxgyjbDenqKG5nqmpptU',
    '_nano_fp': 'Xpmqnp9yXqTjnpTynC_amUld1~sQ6CqeFOj1DSKk',
    'webp': '1',
    'quick_entrance_click_record': '20241224%2C473%2C257%2C129',
    'tubetoken': 'UhRDXBMKi2RSgbpJUUGdA5dITVL%252FWUP7lFfqG3bTVa5SwFAddx0w90ez4Wu0YAvDGcho%252F8pPAZ0RjvaB2eoly%252FCKry5D2yaYA6byQG6EPkASzTMBLOlBaGLCLvMqwdKSeuFI91qSuXiJLcevTVfmJqTBpek0eviq3yn0ni4NUAsEySJEDZ0c7xh7viA%252FLrVUFFCvuAaIC7nBIy0qILi0r6bplghQi38GAXzBwkM%252Bca4%253D',
    'plp_uid': '16e3e38963594c9d8f4d185d629f518d',
    'request_id': '9e928d93cf894e4e9c799ad7bb476f62',
    'rec_list_chat_list_rec_list': 'rec_list_chat_list_rec_list_lhzj3i',
    'PDDAccessToken': 'K4SV2UOXKTRR3QSKQHINDY2TESCOZS4C2B7X5MKRXXXB3O3VIKLQ122df2b',
    'pdd_user_id': '7190558516959',
    'pdd_user_uin': 'S2VP3F6MM4ZL2QCDXFBCZIPO4E_GEXDA',
    'pdd_vds': 'gaepucureZyDIvIumCnTmusqbClTGqlduYGdLrbfuTmfIqxqLBNdnCbdNeuc',
}

headers = {
    'accept': 'application/json',  # Change this to accept JSON
    'accept-language': 'en-US,en;q=0.9,ky-KG;q=0.8,ky;q=0.7,ru-KG;q=0.6,ru;q=0.5',
    'cache-control': 'max-age=0',
    'referer': 'https://mobile.pinduoduo.com/index.html?refer_page_name=personal&refer_page_id=10001_1735268631765_anmq5scbq2&refer_page_sn=10001&page_id=10002_1735268632719_mgfge0dun8&bsch_is_search_mall=&bsch_show_active_page=&item_index=5&count=8&sp=1448&mlist_id=wa3b4t1tfj&last_goods_id=50713146129&is_back=1&list_id=nvmjzmc77m',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

params = {
    'goods_id': '50713146129',
    '_oak_rcto': 'YWJOPgNPdtmEWgJDK5SlLuRnrbb1ULss4EY',
    '_oc_trace_mark': '199',
    '_oc_adinfo': 'eyJwYWdlX3NuIjoxMDAwMiwic2NlbmVfaWQiOjUwNn0=',
    '_oak_gallery_token': '5930ecdeff8888dca50e1aa9ee27a4c9',
    '_oak_gallery': 'https://img.pddpic.com/goods_mms/2024-03-17/b3a21927-eb90-4d10-a37c-bfd695fa9a8e.jpeg',
    '_oc_refer_ad': '1',
    'page_from': '35',
    'thumb_url': 'https://img.pddpic.com/goods_mms/2024-03-17/b3a21927-eb90-4d10-a37c-bfd695fa9a8e.jpeg?imageMogr2/thumbnail/400x%7CimageView2/2/w/400/q/80/format/webp',
    'refer_page_name': 'index',
    'refer_page_id': '10002_1735268632719_mgfge0dun8',
    'refer_page_sn': '10002',
    'uin': 'S2VP3F6MM4ZL2QCDXFBCZIPO4E_GEXDA',
}


# response = requests.get('https://mobile.pinduoduo.com/goods.html', params=params, cookies=cookies, headers=headers)
#
# if response.status_code == 200:
#     html_content = response.text
#
#     parser = AdvancedHTMLParser.AdvancedHTMLParser()
#     parser.parseStr(html_content)
#     script_tag = parser.getElementById("main")
#     print(script_tag)
#     if script_tag:
#         try:
#             json_data = json.loads(script_tag)
#             # goods_data = [
#             #     {
#             #         'id': i['data']['goods_id'],
#             #         'goods_name': i['data']['goods_name'],
#             #         'short_name': i['data']['short_name'],
#             #         'market_price': i['data']['market_price']
#             #     }
#             #     for i in json_data['store']['mainListProps']['goodsList']]
#             #
#             # for data in goods_data:
#             #     print(data)
#             print(json_data)
#
#
#
#
#         except json.JSONDecodeError:
#             print("NONE")
#     else:
#         print("Тег <script> с id='jsonData' не найден.")
#
# else:
#     print(f"Failed to retrieve the page. Status code: {response.status_code}")

#
# import requests
# import json
# from bs4 import BeautifulSoup  # Используем BeautifulSoup для парсинга HTML
#
# cookies = {
#     'api_uid': 'rBUqjWdpOs+wkhWjZO4+Ag==',
#     'jrpl': 'EuNf0CjZEh1AlzrFtaB4R6G4LPfYGvMI',
#     'njrpl': 'EuNf0CjZEh1AlzrFtaB4R6G4LPfYGvMI',
#     'dilx': 'XcxgyjbDenqKG5nqmpptU',
#     '_nano_fp': 'Xpmqnp9yXqTjnpTynC_amUld1~sQ6CqeFOj1DSKk',
#     'webp': '1',
#     'quick_entrance_click_record': '20241224%2C473%2C257%2C129',
#     'tubetoken': 'UhRDXBMKi2RSgbpJUUGdA5dITVL%252FWUP7lFfqG3bTVa5SwFAddx0w90ez4Wu0YAvDGcho%252F8pPAZ0RjvaB2eoly%252FCKry5D2yaYA6byQG6EPkASzTMBLOlBaGLCLvMqwdKSeuFI91qSuXiJLcevTVfmJqTBpek0eviq3yn0ni4NUAsEySJEDZ0c7xh7viA%252FLrVUFFCvuAaIC7nBIy0qILi0r6bplghQi38GAXzBwkM%252Bca4%253D',
#     'plp_uid': '16e3e38963594c9d8f4d185d629f518d',
#     'request_id': '9e928d93cf894e4e9c799ad7bb476f62',
#     'rec_list_chat_list_rec_list': 'rec_list_chat_list_rec_list_lhzj3i',
#     'PDDAccessToken': 'K4SV2UOXKTRR3QSKQHINDY2TESCOZS4C2B7X5MKRXXXB3O3VIKLQ122df2b',
#     'pdd_user_id': '7190558516959',
#     'pdd_user_uin': 'S2VP3F6MM4ZL2QCDXFBCZIPO4E_GEXDA',
#     'pdd_vds': 'gaepucureZyDIvIumCnTmusqbClTGqlduYGdLrbfuTmfIqxqLBNdnCbdNeuc',
# }
#
# headers = {
#     'accept': 'application/json',  # Change this to accept JSON
#     'accept-language': 'en-US,en;q=0.9,ky-KG;q=0.8,ky;q=0.7,ru-KG;q=0.6,ru;q=0.5',
#     'cache-control': 'max-age=0',
#     'referer': 'https://mobile.pinduoduo.com/index.html?refer_page_name=personal&refer_page_id=10001_1735268631765_anmq5scbq2&refer_page_sn=10001&page_id=10002_1735268632719_mgfge0dun8&bsch_is_search_mall=&bsch_show_active_page=&item_index=5&count=8&sp=1448&mlist_id=wa3b4t1tfj&last_goods_id=50713146129&is_back=1&list_id=nvmjzmc77m',
#     'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
# }
#
# params = {
#     'goods_id': '50713146129',
#     '_oak_rcto': 'YWJOPgNPdtmEWgJDK5SlLuRnrbb1ULss4EY',
#     '_oc_trace_mark': '199',
#     '_oc_adinfo': 'eyJwYWdlX3NuIjoxMDAwMiwic2NlbmVfaWQiOjUwNn0=',
#     '_oak_gallery_token': '5930ecdeff8888dca50e1aa9ee27a4c9',
#     '_oak_gallery': 'https://img.pddpic.com/goods_mms/2024-03-17/b3a21927-eb90-4d10-a37c-bfd695fa9a8e.jpeg',
#     '_oc_refer_ad': '1',
#     'page_from': '35',
#     'thumb_url': 'https://img.pddpic.com/goods_mms/2024-03-17/b3a21927-eb90-4d10-a37c-bfd695fa9a8e.jpeg?imageMogr2/thumbnail/400x%7CimageView2/2/w/400/q/80/format/webp',
#     'refer_page_name': 'index',
#     'refer_page_id': '10002_1735268632719_mgfge0dun8',
#     'refer_page_sn': '10002',
#     'uin': 'S2VP3F6MM4ZL2QCDXFBCZIPO4E_GEXDA',
# }
#
# response = requests.get('https://mobile.pinduoduo.com/goods.html', params=params, cookies=cookies, headers=headers)
#
# if response.status_code == 200:
#     html_content = response.text
#
#     soup = BeautifulSoup(html_content, 'html.parser')
#
#     script_tag = soup.find('div', id='main')
#     if script_tag:
#         try:
#             json_str = script_tag.string.strip()
#
#             json_data = json.loads(json_str)
#
#             goods_data = [
#                 {
#                     'id': i['data']['goods_id'],
#                     'goods_name': i['data']['goods_name'],
#                     'short_name': i['data']['short_name'],
#                     'market_price': i['data']['market_price']
#                 }
#                 for i in json_data['params']
#             ]
#
#             for data in goods_data:
#                 print(data)
#         except json.JSONDecodeError:
#             print("Не удалось распарсить JSON.")
#     else:
#         print("Тег <script> с id='main' не найден.")
# else:
#     print(f"Ошибка при получении страницы. Статусный код: {response.status_code}")


import requests
import json
from bs4 import BeautifulSoup  # Используем BeautifulSoup для парсинга HTML

cookies = {
    'api_uid': 'rBUqjWdpOs+wkhWjZO4+Ag==',
    'jrpl': 'EuNf0CjZEh1AlzrFtaB4R6G4LPfYGvMI',
    'njrpl': 'EuNf0CjZEh1AlzrFtaB4R6G4LPfYGvMI',
    'dilx': 'XcxgyjbDenqKG5nqmpptU',
    '_nano_fp': 'Xpmqnp9yXqTjnpTynC_amUld1~sQ6CqeFOj1DSKk',
    'webp': '1',
    'quick_entrance_click_record': '20241224%2C473%2C257%2C129',
    'tubetoken': 'UhRDXBMKi2RSgbpJUUGdA5dITVL%252FWUP7lFfqG3bTVa5SwFAddx0w90ez4Wu0YAvDGcho%252F8pPAZ0RjvaB2eoly%252FCKry5D2yaYA6byQG6EPkASzTMBLOlBaGLCLvMqwdKSeuFI91qSuXiJLcevTVfmJqTBpek0eviq3yn0ni4NUAsEySJEDZ0c7xh7viA%252FLrVUFFCvuAaIC7nBIy0qILi0r6bplghQi38GAXzBwkM%252Bca4%253D',
    'plp_uid': '16e3e38963594c9d8f4d185d629f518d',
    'request_id': '9e928d93cf894e4e9c799ad7bb476f62',
    'rec_list_chat_list_rec_list': 'rec_list_chat_list_rec_list_lhzj3i',
    'PDDAccessToken': 'K4SV2UOXKTRR3QSKQHINDY2TESCOZS4C2B7X5MKRXXXB3O3VIKLQ122df2b',
    'pdd_user_id': '7190558516959',
    'pdd_user_uin': 'S2VP3F6MM4ZL2QCDXFBCZIPO4E_GEXDA',
    'pdd_vds': 'gaepucureZyDIvIumCnTmusqbClTGqlduYGdLrbfuTmfIqxqLBNdnCbdNeuc',
}

headers = {
    'accept': 'application/json',  # Change this to accept JSON
    'accept-language': 'en-US,en;q=0.9,ky-KG;q=0.8,ky;q=0.7,ru-KG;q=0.6,ru;q=0.5',
    'cache-control': 'max-age=0',
    'referer': 'https://mobile.pinduoduo.com/index.html?refer_page_name=personal&refer_page_id=10001_1735268631765_anmq5scbq2&refer_page_sn=10001&page_id=10002_1735268632719_mgfge0dun8&bsch_is_search_mall=&bsch_show_active_page=&item_index=5&count=8&sp=1448&mlist_id=wa3b4t1tfj&last_goods_id=50713146129&is_back=1&list_id=nvmjzmc77m',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
}

params = {
    'goods_id': '50713146129',
    '_oak_rcto': 'YWJOPgNPdtmEWgJDK5SlLuRnrbb1ULss4EY',
    '_oc_trace_mark': '199',
    '_oc_adinfo': 'eyJwYWdlX3NuIjoxMDAwMiwic2NlbmVfaWQiOjUwNn0=',
    '_oak_gallery_token': '5930ecdeff8888dca50e1aa9ee27a4c9',
    '_oak_gallery': 'https://img.pddpic.com/goods_mms/2024-03-17/b3a21927-eb90-4d10-a37c-bfd695fa9a8e.jpeg',
    '_oc_refer_ad': '1',
    'page_from': '35',
    'thumb_url': 'https://img.pddpic.com/goods_mms/2024-03-17/b3a21927-eb90-4d10-a37c-bfd695fa9a8e.jpeg?imageMogr2/thumbnail/400x%7CimageView2/2/w/400/q/80/format/webp',
    'refer_page_name': 'index',
    'refer_page_id': '10002_1735268632719_mgfge0dun8',
    'refer_page_sn': '10002',
    'uin': 'S2VP3F6MM4ZL2QCDXFBCZIPO4E_GEXDA',
}

response = requests.get('https://mobile.pinduoduo.com/goods.html', params=params, cookies=cookies, headers=headers)

# Check if the response is valid
if response.status_code == 200:
    html_content = response.text

    # Используем BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Ищем тег <script> с нужным ID, который может содержать JSON
    script_tag = soup.find('params', id='goods_id')  # Проверьте правильность ID скрипта
    if script_tag:
        try:
            # Извлекаем текст из тега <script>
            json_str = script_tag.string.strip()

            # Пробуем распарсить JSON
            json_data = json.loads(json_str)

            goods_data = [
                {
                    'id': i['data']['goods_id'],
                    'goods_name': i['data']['goods_name'],
                    'short_name': i['data']['short_name'],
                    'market_price': i['data']['market_price']
                }
                for i in json_data['store']['mainListProps']['goodsList']
            ]

            # Выводим данные
            for data in goods_data:
                print(data)
        except json.JSONDecodeError:
            print("Не удалось распарсить JSON.")
    else:
        print("Тег <script> с id='main' не найден.")
else:
    print(f"Ошибка при получении страницы. Статусный код: {response.status_code}")
