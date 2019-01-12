from bs4 import BeautifulSoup
from urllib import request
import urllib.request
url = "http://www.qushuba.com/shu23117/"

def getCommentUrl(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
    req = request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req).read()
    soupArticle=BeautifulSoup(response,'html.parser')
    return soupArticle

soupArticle = getCommentUrl(url)
newChapter = soupArticle.find(id="info")
newChapterUrl=newChapter.find_all('a')[-1].get("href")
commentSoup=getCommentUrl('http://www.qushuba.com/'+newChapterUrl)
artical = commentSoup.find(attrs="bookname").find("h1").get_text()
comment = commentSoup.find(id="content").get_text("\n")
print("\t"*5+artical+"\n",comment)
