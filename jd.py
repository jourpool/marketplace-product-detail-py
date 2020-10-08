import requests, time

#################################################################################
##                                                                             ##
## URL Example: https://jd.id/product/huawei-nova-5t-0_54040123/510158883.html ##
## The last parameter before .html (510158883) is the itemId                   ##
## JD.ID requires two keys: appoloId and apolloSecret                          ##
## At the time of this code written, the keys are a week old and still working ##
##                                                                             ##
#################################################################################

#URL example
url = 'https://www.jd.id/product/noa-everyday-yuri-crop-top-mint-free-size_617876312/617876313.html'

##Set JD.ID Key
apolloId = 'bb381338c65943b5b264bde3020d06a4'
apolloSecret = '03ae97ca5b684fa185700291bb6d0143'

#Get itemId from url
param = url.split('/')
itemid = param[-1].replace(".html", "")

#Set API payload
payload = {}
payload['apolloId'] = apolloId
payload['apolloSecret'] = apolloSecret
payload['skuId'] = itemid
timestamp = str(int(time.time()))

#Set API url for product information
url_api = 'https://color.jd.id/soa_h5/id_wareBusiness.style/1.0?body=' + str(payload)
print(url_api)
headers = { 
    'origin': 'https://www.jd.id',
    'x-api-timestamp': timestamp
}

#Get product information
response = requests.get(url_api, headers=headers).json()

#Populate data object
data = {}
data['platform'] = "JD.ID"
data['name'] = response['others']['wareBaseInfo']['productName']
data['brand'] = response['others']['wareBaseInfo']['brandName']

#Get product image and prices
for i in response['floors']:
    if 'image' not in data:
        try: data['image'] = 'https://id.360buyimg.com/Indonesia/s880x0_/' + i['data']['imageList'][0]
        except KeyError: pass
    if 'price' not in data:
        try: data['price'] = i['data']['salePrice']
        except KeyError: pass
    if 'price_before' not in data: 
        try: data['price_before'] = i['data']['originalPrice']
        except KeyError: pass

#Return JSON object
print(data)