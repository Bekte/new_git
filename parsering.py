import requests
import AdvancedHTMLParser
import json

url = 'https://mobile.pinduoduo.com/index.html?refer_page_name=personal&refer_page_id=10001_1735268631765_anmq5scbq2&refer_page_sn=10001'
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text

    parser = AdvancedHTMLParser.AdvancedHTMLParser()
    parser.parseStr(html_content)


    script_tag = parser.getElementById("__PDD_RAWDATA__")


    if script_tag:
        script_content = script_tag.innerHTML.strip()
        try:
            json_data = json.loads(script_content)
            goods_data = [
                {
                    'id': i['data']['goods_id'],
                    'goods_name': i['data']['goods_name'],
                    'short_name': i['data']['short_name'],
                    'market_price': i['data']['market_price']
                }
                for i in json_data['store']['mainListProps']['goodsList']]

            for data in goods_data:
                print(data)




        except json.JSONDecodeError:
            print("NONE")
    else:
        print("Тег <script> с id='jsonData' не найден.")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")