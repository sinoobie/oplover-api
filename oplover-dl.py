import requests, os

print("""
	[ OPLOVERZ DOWNLOADER ]
	      - noobie -
""")

BASE="https://nuubi.herokuapp.com"
query=input("Search: ")
req=requests.get(BASE+"/api/oplover/search?q="+query).json()
data=req['data']['match']

n=1
print("[Hasil Pencarian]")
for x in data:
	print(f"{n}. {x['title']}")
	n+=1
pil=int(input("Pilih: "))

url=data[pil-1]['url']
req2=requests.get(BASE+"/api/oplover/get_episode?url="+url).json()
data2=req2['data']
print(f"""
[DETAIL]: {data[pil-1]['title']}
{data2['detail']}""")

m=1
print("[Pilih Episode]")
for i in data2['episode']:
	print(f"{m}. {i['name']}")
	m+=1
lih=int(input("Pilih: "))
url2=data2['episode'][lih-1]['url']

req3=requests.get(BASE+"/api/oplover/get_urldl?url="+url2).json()
data3=req3['data']['listdl'][0]
#print(req3)

o=1
print("\n"+data3['title'])
for x in data3['ulist']:
	print(f"{o}. {list(x.keys())[0]}")
	o+=1
pilih=int(input("Pilih: "))
print("Membuka URL")
os.system(f"xdg-open {list(data3['ulist'][pilih-1].values())[0]}")
