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

response= getCommentUrl(URL_tar)
html1 = etree.HTML(response)
results = html1.xpath('/html/body/div/div[3]/div[2]/div[5]/dl/dd/a/@href')


for m in  results:
#获取一个大类下的文件地址
	url2 = str(m.encode("gb2312")).replace(r"\x","%").replace(r"b'","")
	
	mp3Comment = getCommentUrl(url2[0:-1])
	#获取一页的音频文件地址以及总的页数
	htmln = BeautifulSoup(mp3Comment,'html.parser')
	page_Num = htmln.find(valign="middle")
	page_Num= re.findall(".*nt>/(.*)</td.*",str(page_Num))			
	print(int(page_Num[0]))

	for i  in range(1,int(page_Num[0])+1):
		response2= getCommentUrl(url2[0:-1]+"&page=%d"%i)
		html2 = etree.HTML(response2)
		#获取每一页的音频文件地址

		results = html2.xpath('/html/body/div/div[3]/div[2]/table/tr/td[4]/a/@href')
		print(results)
	
		for x in results:
			getMp3 =  getCommentUrl("http://www.yinpin.com/"+x)
			html3 = etree.HTML(getMp3)
			mp3_url =html3.xpath("/html/body/div[1]/div[3]/div[2]/div/div/table/tr/td[1]/table/tr[2]/td[2]/a/@href")
			mp3_name =html3.xpath("/html/body/div/div[3]/div[2]/div/div/table/tr/td[1]/table/tr[1]/td[2]/span/text()")
			try:
				print(mp3_name[0]+".mp3")
				m4a = requests.get(mp3_url[0])
				print(m4a ==None)
				#取音频最后4位数，即就是.mp3作为后缀名
				#with open("./mp3/"+mp3_name[0]+".mp3",'wb') as f:
				 #   f.write(m4a.content)
			except:
				pass