import requests, html, re

###############################################################################################
##                                                                                           ##
## URL Example: https://www.bhinneka.com/total-screwdriver-set-6-pcs-tht250606-sku3334646407 ##
## The last parameter (3334646407) is the itemId                                             ##
## Bhinneka return html instead of data object                                               ##
##                                                                                           ##
###############################################################################################

#URL example
url = 'https://www.bhinneka.com/amazfit-online/amazfit-gtr-47mm-global-version-aluminium-alloy-sku3331451324'

#Get itemId from url
param = url.split('-')
itemid = param[-1].replace('sku', '')

#Set API url for product information
url_api = 'http://www.bhinneka.com/d/p/detail/' + itemid
headers = { 
    'Host': 'www.bhinneka.com',
    'X-Requested-With': 'XMLHttpRequest'
}

#Get product information in html format
response = requests.get(url_api, headers=headers).json()
html = re.sub("\n|\r|", "", response['html'])

#Populate data object
data = {}
data['platform'] = "Bhinneka"
data['name'] = re.search('<h1 class="bt-product-detail__title">(.*)</h1>', html).group(1)
data['image'] = re.search('(?P<url>https?://[^\\s]+)"', html).group(1)
data['price'] = re.search('data-price="(.*)" id="product-detail-pricestring"', html).group(1)

price_before = re.search('<del>Rp(.*)</del>', html)
if price_before: data['price_before'] = price_before.group(1).replace('.', '')
else: data['price_before'] = data['price']

#Return JSON object
print(data)