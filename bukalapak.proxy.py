import requests

##########################################################################################
##                                                                                      ##
## URL Example: https://bukalapak.com/p/handphone/headset-earphone/39ghf7n-jual-headset ##
## The itemId is the id between the last slash and the first dash (39ghf7n)             ##
## Bukalapak requires token first from /westeros_auth_proxies                           ##
##                                                                                      ##
##########################################################################################

#URL example
url = 'https://www.bukalapak.com/p/fashion-wanita/baju-muslim-perlengkapan-sholat-2555/busana-muslim-wanita/1lxw25g-jual-gamis-maxi-aulia-free-pashmina?from=homepage&source=fvt&panel=1&type=recommendation'

#Set proxy
proxies = { 
    'http'  : "http://orangeapp.xyz:8888", 
    'https' : "https://orangeapp.xyz:8888"
}

#Get itemId from url
param = url.split('/')
itemid = param[-1].split('-')[0]

#Set API url for token and product information
url_token = 'https://www.bukalapak.com/westeros_auth_proxies'
url_data = 'https://api.bukalapak.com/products/'
headers = { 
    'Content-Length': '0',
    'Content-Type': 'application/json',
    'User-Agent': 'PostmanRuntime/7.26.2'
}

#Get token
response = requests.post(url_token, headers=headers).json()

#Update API url for product information
url_data += itemid + '?access_token=' + response['access_token']

#Get product information
response = requests.get(url_data, headers=headers, proxies=proxies).json()

#Populate data object
data = {}
data['platform'] = "Bukalapak"
data['name'] = response['data']['name']
data['brand'] = response['data']['specs']['brand']
data['image'] = response['data']['images']['large_urls'][0]
data['price'] = response['data']['deal']['discount_price']
data['price_before'] = response['data']['deal']['original_price']

#Return JSON object
print(data)