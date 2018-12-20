import re
from bs4 import BeautifulSoup
import requests
from urllib import request
import urllib.request
url = "https://www.qu.la/book/3137/"

def getCommentUrl(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0'}

    req = request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req).read()
    soupArticle=BeautifulSoup(response,'lxml')
    return soupArticle
soupArticle = getCommentUrl(url)
newChapter = soupArticle.find(id="info")
newChapterUrl=newChapter.find_all('a')[-1].get("href")
chapterNew=url+newChapterUrl
commentSoup=getCommentUrl(chapterNew)
artical = commentSoup.find(attrs="bookname").find("h1").get_text()
comment = commentSoup.find(id="content").get_text("\n")
print("\t"*5+artical,comment.replace('chaptererror();','').replace("小说网..org，最快更新元尊最新章节！",""))

