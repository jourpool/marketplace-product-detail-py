import requests

########################################################################
##                                                                    ##
## URL Example: https://www.sociolla.com/shampoo/26873-ikoo-infusions ##
## The numeric parameter (26873) in the URL is the itemId             ##
##                                                                    ##
########################################################################

#URL example
url = 'https://www.sociolla.com/accessories/11896-102-angled-contour-brush'

#Get itemId from url
param = url.split('/')
itemid = param[-1]

#Set API url for product information
url_api = 'https://catalog-api.sociolla.com/v3/products/' + itemid
headers = { 
    'soc-platform': 'sociolla-web-desktop'
}

#Get product information
response = requests.get(url_api, headers=headers).json()

#Populate data object
data = {}
data['platform'] = "Sociolla"
data['name'] = response['data']['meta_title'].replace(" | Sociolla", "")
data['brand'] = response['data']['brand']['name']
data['image'] = response['data']['images'][0]['url']
data['price_before'] = response['data']['max_price']
data['price'] = response['data']['min_price_after_discount']

#Return JSON object
print(data)