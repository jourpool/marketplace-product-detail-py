import requests, re, json

#URL example
url = 'https://www.orami.co.id/sweety-silver-pants-boys-xxl-3x24.html'

#Get content
response = requests.get(url).content

#Get product information
raw = re.search('productDetail'r'\(''(.*), source', response.decode('utf-8')).group(1)

#Convert to JSON
json_response = json.loads(raw)

#Populate data object
try:
    data = {}
    data['platform'] = 'Orami'
    data['name'] = json_response['name']
    data['brand'] = json_response['brand']['name']
    data['price'] = json_response['price']['final']
    data['price_before'] = json_response['price']['original']
    data['image'] = json_response['image_default']['image']['base']
except:
    pass

#Return JSON object
print(data)