from bs4 import BeautifulSoup
from urllib import request
import urllib.request
from lxml import etree
import requests
import re

URL_tar = 'http://www.yinpin.com/'
def getCommentUrl(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    req = request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req).read()
    return response

def lxm_Html(url):
	response= getCommentUrl(url)
	html = etree.HTML(response)
	return html


#获取主页面下标题地址
html1 = lxm_Html(URL_tar)
results = html1.xpath('/html/body/div/div[3]/div[2]/div[5]/dl/dd/a/@href')

for m in  results:
#获取一个大类下的文件地址
	url2 = str(m.encode("gb2312")).replace(r"\x","%").replace(r"b'","")
	erro_num = 0
##########################################################
	#获取一页的音频文件页数
	mp3Comment = getCommentUrl(url2[0:-1])
	htmln = BeautifulSoup(mp3Comment,'html.parser')
	page_Num = htmln.find(valign="middle")
	page_Num= re.findall(".*nt>/(.*)</td.*",str(page_Num))			
##########################################################

	for i  in range(1,int(page_Num[0])+1):
		#获取一类当前页面所有音频索引地址
		html2 =lxm_Html(url2[0:-1]+"&page=%d"%i)		
		results = html2.xpath('/html/body/div/div[3]/div[2]/table/tr/td[4]/a/@href')

		for x in results:
		#获取单个音频文件下载地址以及文件名字
			html3 = lxm_Html("http://www.yinpin.com/"+x)
			mp3_url =html3.xpath("/html/body/div[1]/div[3]/div[2]/div/div/table/tr/td[1]/table/tr[2]/td[2]/a/@href")
			mp3_name =html3.xpath("/html/body/div/div[3]/div[2]/div/div/table/tr/td[1]/table/tr[1]/td[2]/span/text()")
			#下载文件
			try:
				print("下载："+mp3_name[0]+".mp3.......")
				m4a = requests.get(mp3_url[0])
				with open("./mp3/"+mp3_name[0]+".mp3",'wb') as f:
				   f.write(m4a.content)
			except:
				erro_num+=1
				print(erro_num)
