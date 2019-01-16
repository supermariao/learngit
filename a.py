# encoding = utf-8
import requests
import os
import socket
import sqlite3
import re
search_string = input('输入要查询的电影名称:')
search_string = '千与千寻'
r = requests.post(r'http://www.zuixinzy.com/index.php?m=vod-search',data={'m':'vod-search','wd':search_string,'submit':'search'})
temp = re.findall('<a href="/\?m=vod-detail-id-[0-9]+\.html" target="_blank">.+?</a></span>',r.text)
print(temp)
name_list = []
url_list = []
for str in temp:
	url = 'http://www.zuixinzy.com' + str.split('"')[1]
	name = str.split('>')[1][:-3]
	print(name)
	r = requests.get(url)
	url = re.findall('https://.+?index\.m3u8',r.text)
	print(url)
	j = len(url)/2
	i = 0
	while i<j:
		print(url[i])
		i += 1
	name_list.append(name)
	url_list.append(url)
print(name_list)