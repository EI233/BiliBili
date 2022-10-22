import time

import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 "
                  "Safari/537.36 Edg/106.0.1370.52 ",
    "Referer": "https://www.bilibili.com",
}
for num in range(154, 170):
    time.sleep(1)
    with open(f"link/第{num}周link.txt", encoding="utf8") as f:
        k = 0
        link = f.readlines()
        for url in link:
            time.sleep(1)
            resp = requests.get(url.strip())
            dom = etree.HTML(resp.text)
            a = dom.xpath('//*[@id="v_tag"]/div/ul/li[@class="tag"]/div/a/text()')
            b = dom.xpath('//*[@id="v_tag"]/div/ul/li[@class="tag"]/a/text()')
            a_new = []
            b_new = []
            for i in a:
                a_new.append(i.strip())
            for i in b:
                b_new.append(i.strip())
            res = set(a_new + b_new)
            k += 1
            print(f"tag/第{num}周第{k}个tag.txt")
            with open(f"tag/第{num}周第{k}个tag.txt", "w") as f:
                for j in res:
                    f.write(j + "\n")
