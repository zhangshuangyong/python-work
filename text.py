#coding=gbk
import requests
import re
url='https://www.douyu.com/g_LOL'


headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'

}
reponse=requests.get(url,headers=headers).content.decode()
#with open('1.html','wb',encoding='utf8') as f:
    #f.write(reponse.content)
#print(type(reponse))
pattern=r'<div class="DyListCover-info"><span class="DyListCover-hot is-template"><svg><use xlink:href="#icon-hot_635f5ef"></use></svg>(.*?)</span><h2 class="DyListCover-user is-template"><svg><use xlink:href="#icon-user_05fb112"></use></svg>(.*?)</h2></div>'
match=re.findall(pattern,reponse,re.M)
#print(match)
for title_redu in match:
    title=title_redu[-1]
    redu=title_redu[0]
    print(title,redu)

