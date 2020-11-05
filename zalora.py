import requests

#URL example
url = 'https://www.zalora.co.id/lois-jeans-long-pant-denim-black-2335013.html'

#Get itemId from url
param = url.split('/')
itemid = param[-1]

#Set API url for product information
url_api = 'https://www.zalora.co.id/data?method=getProductDetail&productUrl=' + itemid
headers = { 
    'Host': 'www.zalora.co.id',
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
}

#Get product information
response = requests.get(url_api, headers=headers).json()

#Populate data object
try:
    data = {}
    data['platform'] = "Zalora"
    data['name'] = response['data']['product_name']
    data['brand'] = response['data']['brand_name']
    data['image'] = response['data']['product_images'][0]['product_image']
    data['price_before'] = response['data']['unformatted_price'].replace(".00", "")
    data['price'] = response['data']['unformatted_special_price'].replace(".00", "")
except:
    pass

#Return JSON object
print(data)