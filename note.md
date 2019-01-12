# Xpath 匹配为空

问题：在chorme的F12开发者模式中直接获取的xpath 为chorme优化过的，可能会导致你在应用到selector时出现空匹配。例如：

content = selector.xpath('/html/body/table/tr/td[2]/a[1]')

这个在chorme中，就会优化为/html/body/table/**tbody**/tr/td[2]/a[1]，这样就无法匹配

解决办法：所以需要删除掉tbody。


原文：https://blog.csdn.net/tjuyanming/article/details/71194546 

问题1：获取两个字符中间的字符

```
>>> a ='<td valign="middle">共99个,每页20个,页次：<font color="b50000">1</font>/5</td>'
>>> re.findall(".*nt>/(.*)</td.*",a)
['5']
```

