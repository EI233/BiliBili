import asyncio
import time

from bilibili_api import video, DanmakuClosedException, ResponseCodeException


async def main():
    for num in range(93, 188):
        k = 0
        with open(f"aid/第{num}周aid.txt", encoding="utf8") as f:
            aid = f.readlines()
            for i in aid:
                v = video.Video(aid=int(i))
                try:
                    time.sleep(0.5)
                    dms = await v.get_danmakus(0)
                    k += 1
                    with open(f"danmakus/第{num}周-第{k}视频.txt", "w", encoding="utf8") as f_new:
                        for j in dms:
                            f_new.write(j.text + "\n")
                except DanmakuClosedException:
                    dms = []
                except ResponseCodeException:
                    dms = []
                except KeyError:
                    dms = []
                except:
                    pass


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
