'''
- 為「PCHome線上購物」建立一個離線版的商品搜尋程式。
- 網址： https://shopping.pchome.com.tw/
'''

import requests
import os
import json
import prettytable

def search_product(product_name, page_num):
    rr = requests.get(
        "https://ecshweb.pchome.com.tw/search/v3.3/all/results",
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36 OPR/67.0.3575.115",
            "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        },
        params = {
            "q" : prodcut_name,
            "page" : str(page_num),
            "sort" : "sale/dc"
        }
    )

    data_json = json.loads(rr.text)
    return data_json["prods"]
    # for d in data_json["prods"]:
    #     print(d["name"], d["price"])

def show_product(product_list):
    os.system("cls")
    t = prettytable.PrettyTable(["名稱","價格"],encoding="utf-8")
    t.align["名稱"] = "l"
    t.align["價格"] = "r"
    for d in product_list:
        # print(d["name"], d["price"])
        t.add_row([d["name"], d["price"]])
    print(t)

os.system("cls")
prodcut_name = input("產品關鍵字： ")
page_num = 1

while page_num != 0:
    product_list = search_product(prodcut_name, page_num)
    show_product(product_list)
    print(f"現在頁碼：{page_num}")
    try:
        page_num = int(input("前往頁碼(輸入 0 結束): "))
    except:
        pass



