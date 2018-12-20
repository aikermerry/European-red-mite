from lxml import etree
import requests

url = "http://www.qushuba.com/shu23117/"

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}

response = requests.get(url=url, headers=headers).text

html = etree.HTML(response)
results = html.xpath('//*[@id="info"]/p[4]/a/@href')

response1 = requests.get('http://www.qushuba.com' + results[0], headers=headers).text
html1 = etree.HTML(response1)

text = ''
for i in html1.xpath('//*[@id="content"]/text()'):
    text += i.replace('\xa0', '')
    text += '\n'

print(text)

