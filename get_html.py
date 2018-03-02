#!/usr/bin/env python
# -*- coding:utf-8 -*-

import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests

from pyquery import PyQuery as pq

url = "http://www.ajxxgk.jcy.cn/html/20180225/2/7827700.html"

headers = {
    'upgrade-insecure-requests': "1",
    'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
    'x-devtools-emulate-network-conditions-client-id': "(ED36D896727475E63F96694479CF2756)",
    'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'referer': "http://www.ajxxgk.jcy.cn/html/20180301/2/7848211.html",
    'accept-encoding': "gzip, deflate",
    'accept-language': "zh-CN,zh;q=0.9",
    'cookie': "__jsluid=5703c81927cadffb6590ee32752b049d; Hm_lvt_2e64cf4f6ff9f8ccbe097650c83d719e=1519996257; PHPSESSID=a4545u146rv7brq0ummmel6e67; sYQDUGqqzHpid=page_0; sYQDUGqqzHtid=tab_0; Hm_lpvt_2e64cf4f6ff9f8ccbe097650c83d719e=1519996280",
    'cache-control': "no-cache",
    'postman-token': "e1632309-81d3-2580-3cc4-76133c387d26"
}

filename = "20180225/2/7827700"

for i in range(1,1000):

    filename_blocks = filename.split('/')

    fname = ''
    for b in filename_blocks:
        fname = fname + b + '-'
    response = requests.request("GET", url, headers=headers)
    #fo = open("./"+filename+".html", "wb")
    fo = open("./"+fname+".html", "wb")
    fo.write(response.text)
    fo.close()

    doc = pq(filename="./"+fname+".html")
    data_f14 = pq(doc('.f14')[0])

    a_label = data_f14('a').eq(0).attr('href')

    #print a_label
    url = "http://www.ajxxgk.jcy.cn" + a_label

    a_label_es = a_label.split('/')
    filename = a_label_es[2] + '/' + a_label_es[3] + '/' + a_label_es[4].split('.')[0]

    #print filename
    print i



#print(response.text)