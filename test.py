import requests
import json

url = "https://api.bilibili.com/x/web-interface/popular/series/one?number="
for i in range(1, 188):
    res = requests.request(url=url + f"{i}", method="Get")
    data = json.loads(res.text)
    # with open(f"data/第{i}周.json", "w", encoding="utf8") as f:
    #     f.write(res.text)
    # with open(f"aid/第{i}周aid.txt", "w", encoding="utf8") as f:
    #     for i in data["data"]["list"]:
    #         f.write(str(i["aid"]) + "\n")
    # with open(f"tag/第{i}周.json", "w", encoding="utf8") as f:
    #     new_data = {}
    #     for j in data["data"]["list"]:
    #         if j["tname"] not in new_data.keys():
    #             new_data.update({j["tname"]: 1})
    #         else:
    #             new_data[j["tname"]] += 1
    #     json.dump(new_data, f, ensure_ascii=False)
    # with open(f"cid/第{i}周cid.txt", "w", encoding="utf8") as f:
    #     for i in data["data"]["list"]:
    #         f.write(str(i["cid"]) + "\n")
    with open(f"link/第{i}周link.txt", "w", encoding="utf8") as f:
        for i in data["data"]["list"]:
            f.write(str(i["short_link"]) + "\n")
