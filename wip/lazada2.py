import requests, re

#URL example
url = 'https://www.lazada.co.id/products/kulot-pendek-super-jumbo-90kg-random-i1035300310-s1568936681.html?spm=a2o4j.home.flashSale.3.41631559aBsdsW&search=1&mp=1&c=fs&clickTrackInfo=%7B%22rs%22%3A%220.10229821620459917%22%2C%22prior_score%22%3A%220%22%2C%22submission_discount%22%3A%2270%25%22%2C%22iss%22%3A%220.10229821620459917%22%2C%22type%22%3A%22entrance%22%2C%22prior_type%22%3A%22racing%22%2C%22userid%22%3A%22%22%2C%22sca%22%3A%222%22%2C%22hourtonow%22%3A%2213%22%2C%22abid%22%3A%22186176%22%2C%22itemid%22%3A%221035300310_1_racing_0.10229821620459917_0.10229821620459917%22%2C%22pvid%22%3A%2204b95aad-489b-43de-8821-940bf78687c8%22%2C%22pos%22%3A%221%22%2C%22rms%22%3A%220.0%22%2C%22c2i%22%3A%220.0%22%2C%22scm%22%3A%221007.17760.186176.%22%2C%22ss%22%3A%220.10229821620459917%22%2C%22i2i%22%3A%220.0%22%2C%22ms%22%3A%220.10229821620459917%22%2C%22itr%22%3A%220.18%22%2C%22mt%22%3A%22racing%22%2C%22its%22%3A%22300%22%2C%22promotion_price%22%3A%2221.000%22%2C%22anonid%22%3A%22f3a656a8-7914-4003-c8d5-84534c5f2870%22%2C%22FinalScore%22%3A%220.0950303003191948%22%2C%22isc%22%3A%2254%22%2C%22iss2%22%3A%220.540819533266665%22%2C%22data_type%22%3A%22flashsale%22%2C%22iss1%22%3A%220.03272727272727273%22%2C%22config%22%3A%22%22%2C%22HP_score%22%3A%220.0950303003191948%22%2C%22channel_id%22%3A%220000%22%7D&scm=1007.17760.186176.0'

#Get product information
response = requests.get(url).content

json = re.search('app.run(.*);', response.decode('utf-8')).group(1)[1:-1]

#data = {}
#data['platform'] = 'Lazada'
#data['name'] = response['data']['meta_title']
#data['brand'] = response['data']['brand']['name']
#data['image'] = response['data']['images'][0]['url']
#data['price_before'] = response['data']['max_price']
#data['price'] = response['data']['min_price_after_discount']

print(json)