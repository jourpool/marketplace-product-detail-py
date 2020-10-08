import requests

###########################################################################
##                                                                       ##
## URL Example: https://www.blibli.com/p/baby-pakcoy/ps--CAS-60072-00033 ##
## The last parameter (ps--CAS-60072-00033) is the itemId                ##
## Blibli uses 2 API endpoint to gather product info and prices          ##
## _summary for product information, _info for product prices            ##
##                                                                       ##
###########################################################################

#URL example
url = 'https://www.blibli.com/p/baby-pakcoy/ps--CAS-60072-00033'

#Get itemId from url
param = url.split('/')
itemid = param[-1].replace('?', '')

#Set API url for product information and product price
url_api = 'https://www.blibli.com/backend/product/products/' + itemid
url_data = url_api + '/_summary'
url_price = url_api + '/_info'
headers = { 
    'Host': 'www.blibli.com',
    'Connection': 'keep-alive',
    'User-Agent': 'PostmanRuntime/7.26.2'
}

print(url_data)

#Get product information
response = requests.get(url_data, headers=headers).json()

#Populate data object
data = {}
data['platform'] = "Blibli"
data['name'] = response['data']['name']
data['brand'] = response['data']['brand']['name']
data['image'] = response['data']['images'][0]['full']

#Get product price
response = requests.get(url_price, headers=headers).json()

#Update and populate data object with price information
data['price'] = response['data']['price']['offered']
data['price_before'] = response['data']['price']['listed']

#Return JSON object
print(data)