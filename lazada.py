import requests, re, json

#URL example
url = 'https://www.lazada.co.id/products/mie-kremez-shorr-24-pcs-i3014298844-s5361348173.html?spm=a2o4j.home.flashSale.3.3e9c1559Q5pjfE&search=1&mp=1&c=fs&clickTrackInfo=%7B%22rs%22%3A%220.005365079153474421%22%2C%22prior_score%22%3A%220%22%2C%22submission_discount%22%3A%2223%25%22%2C%22iss%22%3A%220.005365079153474421%22%2C%22type%22%3A%22entrance%22%2C%22prior_type%22%3A%22racing%22%2C%22userid%22%3A%22%22%2C%22sca%22%3A%221%22%2C%22hourtonow%22%3A%2213%22%2C%22abid%22%3A%22178638%22%2C%22itemid%22%3A%223014298844_1_racing_0.005365079153474421_0.005365079153474421%22%2C%22pvid%22%3A%22705ae7ab-683a-4d99-b588-0bc236fff496%22%2C%22pos%22%3A%221%22%2C%22rms%22%3A%220.0%22%2C%22c2i%22%3A%220.0%22%2C%22scm%22%3A%221007.17760.178638.%22%2C%22ss%22%3A%220.005365079153474421%22%2C%22i2i%22%3A%220.0%22%2C%22ms%22%3A%220.005365079153474421%22%2C%22itr%22%3A%220.01%22%2C%22mt%22%3A%22racing%22%2C%22its%22%3A%22400%22%2C%22promotion_price%22%3A%2210.000%22%2C%22anonid%22%3A%22f3a656a8-7914-4003-c8d5-84534c5f2870%22%2C%22FinalScore%22%3A%220.10352600365877151%22%2C%22isc%22%3A%224%22%2C%22iss2%22%3A%220.19262837001884967%22%2C%22data_type%22%3A%22flashsale%22%2C%22iss1%22%3A%229.411764705882353E-4%22%2C%22config%22%3A%22%22%2C%22HP_score%22%3A%220.10352600365877151%22%2C%22channel_id%22%3A%220000%22%7D&scm=1007.17760.178638.0'

#Get content
response = requests.get(url).content

#Get product information
raw = re.search('app.run(.*);', response.decode('utf-8')).group(1)[1:-1]

#Convert to JSON
json_response = json.loads(raw)

#Populate data object
data = {}
data['platform'] = 'Lazada'
data['name'] = json_response['data']['root']['fields']['skuInfos']['0']['dataLayer']['pdt_name']
data['brand'] = json_response['data']['root']['fields']['product']['brand']['name']
data['image'] = json_response["data"]["root"]["fields"]["skuGalleries"]["0"][0]['src']
data['price'] = json_response['data']['root']['fields']['skuInfos']['0']['price']['salePrice']['value']
data['price_before'] = json_response['data']['root']['fields']['skuInfos']['0']['price']['originalPrice']['value']

#Return JSON object
print(data)