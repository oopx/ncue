import urllib.request as request 
src="https://www.ntu.edu.tw/"
with request.urlopen(src) as response:
	data=response.read().decode("utf-8")
print(data)
