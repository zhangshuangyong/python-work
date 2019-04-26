import requests
from multiprocessing import Pool
def temp(i):
	url="https://youku163.zuida-bofang.com/20181004/16232_27848638/800k/hls/6655c001960%03d.ts"%i

	headers={
	"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
	}
	r=requests.get(url,headers=headers)
	ret=r.content
	with open('D:/nmp4/{}'.format(url[-10:]),'wb') as f:
		f.write(ret)
		

if __name__ == '__main__':
	pool=Pool(10)
	for i in range(1600):
		pool.apply_async(temp, (i, ))
	pool.close()
	pool.join()
