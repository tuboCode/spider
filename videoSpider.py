#-*- coding: utf-8 -*-

import requests
import os

# 爬取图片
# url = "http://image.nationalgeographic.com.cn/2017/0808/20170808103205868.jpg"
# 爬取视频
url = "http://150.138.145.101/254/23/52/bcloud/126677/ver_00_22-1112195569-avc-194172-aac-48000-52867-1698198-c5716d00a8d8caf15206c53f7a578858-1502158046456.mp4"
root = 'D://pic//'
path = root + url.split('/')[-1]

try:
    if not os.path.exists(root):
        os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(url)
            with open(path, 'wb') as f:
                f.write(r.content)
                f.close()
                print("文件保存成功")
    else:
        print("文件已存在")
except:
    print("爬取失败")