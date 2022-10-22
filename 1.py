import google.protobuf.text_format as text_format
import requests

import dm_pb2 as Danamku

url = "http://api.bilibili.com/x/v2/dm/web/seg.so"
k = 0
for num in range(1, 188):
    k = 0
    with open(f"cid/第{num}周cid.txt", encoding="utf8") as f:
        aid = f.readlines()
        for i in aid:
            k += 1
            for j in range(1, 20):
                params = {
                    "type": 1,
                    "oid": int(i),
                    "segment_index": j
                }
                resp = requests.get(url, params)
                if resp.status_code != 200:
                    break
                data = resp.content
                with open(f"res/第{num}周第{k}个视频.so", "ab+") as f_new:
                    f_new.write(data)

# danmaku_seg = Danamku.DmSegMobileReply()
# danmaku_seg.ParseFromString(data)
# for i in range(len(danmaku_seg.elems)):
#     danmaku = text_format.MessageToString(danmaku_seg.elems[i], as_utf8=True)
#     # print(danmaku.split("\n")[6])
#     num += 1
# print(num)
