#! python3
#lucky.py - Opens several Google search results.
#自动打开几个google搜索结果的程序
import requests, sys, webbrowser, bs4

#STEP1.获取命令行参数，并请求查找页面
print('Googling...')  #display text while downloading the Google page 
res = requests.get('http://google.com/search?q=' + ' ' .join(sys.argv[1:]))
res.raise_for_status()

#STEP2.找到所有的结果
#Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text)

#STEP3.针对每个结果打开WEB浏览器
#Open a browser tab for each result.
linkElems = soup.select('.r a')
numOpen = min(5, len(linkElems))
for i in range(numOpen):
	webbrowser.open('http://google.com' + linkElems[i].get('href'))
	