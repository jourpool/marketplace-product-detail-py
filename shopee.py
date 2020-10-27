import requests, re

########################################################################
##                                                                    ##
## URL Example: https://shopee.co.id/vivo-i.30843261.2848762096       ##
## The last parameter (2848762096) is the itemId                      ##
## Second to last parameter (30843261) is the shopId                  ##
##                                                                    ##
########################################################################

#URL example format 1
#url = 'https://shopee.co.id/Celana-Pendek-Pria-Surfing-Distro-Premium-Renang-Pantai-Santai-Kolor-i.153402659.7646971923'

#URL example format 2
url = 'https://shopee.co.id/product/244026479/6531587103?smtt=0.232910045-1603341378.9'

#Get itemId and shopeId from url
if '/product/' in url:
    param = re.search('/product/(.*)[?]', url).group(1).split('/')
    itemId = param[1]
    shopId = param[0]
else:
    param = url.split('.')
    itemId = param[-1]
    shopId = param[-2]

#Set API url for product information
url_api = 'https://shopee.co.id/api/v2/item/get?itemid=' + itemId + '&shopid=' + shopId
headers = { 
    'Host': 'shopee.co.id',
    'User-agent': 'PostmanRuntime/7.26.5',
    'Referer': url
}

#Get product information
response = requests.get(url_api, headers=headers).json()

#Populate data object
data = {}
data['platform'] = "Shopee"
data['name'] = response['item']['name']
data['brand'] = response['item']['brand']
data['image'] = 'https://cf.shopee.co.id/file/' + response['item']['images'][0]
data['price_before'] = response['item']['price_before_discount']/100000
data['price'] = response['item']['price']/100000

if(data['price_before'] < data['price']):
    data['price_before'] = data['price']

# #Return JSON object
print(data)