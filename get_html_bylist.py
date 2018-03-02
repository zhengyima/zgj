#!/usr/bin/env python
# -*- coding:utf-8 -*-

import csv
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import requests
import os

from pyquery import PyQuery as pq


def get_a_page(url, headers):
    response = requests.request("GET", url, headers=headers)
    return response.text

def get_a_book(url,headers,filename):
    filename_blocks = filename.split('/')

    fname = ''
    for b in filename_blocks:
        fname = fname + b + '-'
    response = requests.request("GET", url, headers=headers)
    # fo = open("./"+filename+".html", "wb")
    fo = open("./" + fname + ".html", "wb")
    fo.write(response.text)
    fo.close()

    doc = pq(filename="./" + fname + ".html")

    if len(doc('.f14')) == 0:
        os.remove("./" + fname + ".html")
        return

    data_f14 = pq(doc('.f14')[0])

    a_label = data_f14('a').eq(0).attr('href')


list_url = "http://www.ajxxgk.jcy.cn/html/zjxflws/2.html"

list_headers = {
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
for i in (2, 2518):

    list_html = get_a_page(list_url, list_headers)
    fo = open("./list/" + str(i) + ".html", "wb")
    fo.write(list_html)
    fo.close()

    doc = pq(filename="./list/" + str(i) + ".html")
    data_page_0 = pq(doc('#page_0'))
    data_ctitles = pq(data_page_0('.ctitle'))

    cnt = 0
    for ctitle_block in data_ctitles:
        url = pq(ctitle_block)('a').eq(1).attr('href')
        #print url

        book_url =  "http://www.ajxxgk.jcy.cn" + url

        url_blocks = url.split('/')
        fname = url_blocks[2]+ '/' + url_blocks[3] + '/' + url_blocks[4].split('.')[0]

        get_a_book(book_url,list_headers,fname)

        cnt += 1
        print cnt





    list_url = "http://www.ajxxgk.jcy.cn/html/zjxflws/" + str(i + 1) + ".html"
    print "-------------------------"





