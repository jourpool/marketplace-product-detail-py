import requests, re, json

#URL example format 1
#url = 'https://www.lazada.co.id/products/kemeja-polos-pria-lengan-pendek-kemeja-pria-kemeja-polos-kemeja-distro-kemeja-casual-pria-bahan-oxsport-hitam-i2947356098-s5235832860.html'

#URL example format 2
url = 'https://s.lazada.co.id/s.cnC0l'

#Handle mobile URL
if 's.lazada.co.id' in url:
    mobileHeaders = { 
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'sec-fetch-mode': 'navigate', 'sec-fetch-dest': 'document', 'sec-fetch-site': 'none'
    }
    response = requests.get(url, headers=mobileHeaders).content
    url = re.search('<link rel="origin" href="(.*)"/>', response.decode('utf-8')).group(1)

#Set headers
headers = { 
    'Cache-Control': 'no-cache',
    'Host': 'www.lazada.co.id',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'origin': 'https://www.lazada.co.id',
    'referer': 'https://s.lazada.co.id/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
    'sec-fetch-mode': 'navigate', 'sec-fetch-dest': 'document', 'sec-fetch-site': 'same-site'
}

#Get content
response = requests.get(url, headers=headers).content

#Get product information
raw = re.search('app.run(.*);', response.decode('utf-8')).group(1)[1:-1]

#Convert to JSON
json_response = json.loads(raw)

#Populate data object
try:
    data = {}
    data['platform'] = 'Lazada'
    data['name'] = json_response['data']['root']['fields']['skuInfos']['0']['dataLayer']['pdt_name']
    data['brand'] = json_response['data']['root']['fields']['product']['brand']['name']
    data['image'] = json_response['data']['root']['fields']['skuGalleries']['0'][0]['src']
    data['price'] = json_response['data']['root']['fields']['skuInfos']['0']['price']['salePrice']['value']
    data['price_before'] = json_response['data']['root']['fields']['skuInfos']['0']['price']['originalPrice']['value']
except:
    pass

#Return JSON object
print(data)