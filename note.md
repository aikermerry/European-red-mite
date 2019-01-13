# Xpath 匹配为空

问题0：在chorme的F12开发者模式中直接获取的xpath 为chorme优化过的，可能会导致你在应用到selector时出现空匹配。例如：

content = selector.xpath('/html/body/table/tr/td[2]/a[1]')

这个在chorme中，就会优化为/html/body/table/**tbody**/tr/td[2]/a[1]，这样就无法匹配

解决办法：所以需要删除掉tbody。


原文：https://blog.csdn.net/tjuyanming/article/details/71194546 

问题1：获取两个字符中间的字符

```python
import re
>>> a ='<td valign="middle">共99个,每页20个,页次：<font color="b50000">1</font>/5</td>'
>>> re.findall(".*nt>/(.*)</td.*",a)
['5']
```

问题2：保存mp3文件

```python
m4a = requests.get(mp3_url[0])
    with open("./mp3/"+mp3_name[0]+".mp3",'wb') as f:
         f.write(m4a.content)
		
```

问题3：lxml库使用：

```python
from lxml import etree
def getCommentUrl(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    req = request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req).read()
    return response


response= getCommentUrl(url)
html = etree.HTML(response)
#获取指定路径的内容，获取连接再后面加/@href ，文本加/text()
results = html.xpath('/html/body/div/div[3]/div[2]/div[5]/dl/dd/a/@href')
```

