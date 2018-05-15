#！ python3
#downloadXkcd.py - Downloads every single XKCD comic.
#抓取所有XKCD漫画
#技能包：requests模块(下载页面)，BeautifulSoup(找到页面中漫画的URL），
#	iter_content(下载漫画并保存到硬盘)
import requests, os, bs4

url = 'http://xkcd.com'					#starting url
os.makedirs('xkcd', exist_ok = True)	#store comics in ./xkcd
while not url.endswith('#'):
	#STEP.1 下载网页
	#Download the page.
	print('Downloading page %s...' % url)
	res = requests.get(url)
	res.raise_for_status()
	
	soup = bs4.BeautifulSoup(res.text)
	
	#STEP.2 寻找和下载漫画图像
	#Find the URL of the comic image.
	comicElem = soup.select('#comic img')
	if comicElem == []:
		print ('Could not find comic image.')
	else:
		comicUrl = 'http:' + comicElem[0].get('src')

		#Download the image.
		print ('Downloading image %s...' %(comicUrl))
		res = requests.get(comicUrl)
		res.raise_for_status()
		
		#STEP.3 保存图像到硬盘，找到前一张漫画
		#Save the image to ./xkcd.
		imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()
		
	#Get the Prev button's url.
	prevLink = soup.select('a[rel="prev"]')[0]
	url = 'http://xkcd.com' + prevLink.get('href')
print ('Done.')

