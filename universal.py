import opengraph, warnings, tldextract

#########################################################
##                                                     ##
## Known Supported Platform:                           ##
## fabelio, monotaro, mapemall, elevania, hijup, laku6 ##
## matahari, ralali, blanja                            ##
##                                                     ##
#########################################################

#URL example
#url = 'https://www.monotaro.id/corp_id/s003588772.html'
#url = 'https://fabelio.com/ip/karpet-modry-nilon-100x150'
#url = 'https://www.mapemall.com/item/19/0888-DUL10915-19-A032?isFromSIS=true'
#url = 'https://www.elevenia.co.id/prd-super-suki-value-voucher-50-000-28881836'
#url = 'https://www.hijup.com/id/square-hijab/64312-julie-gray?h_source_url=%2Fid'
#url = 'https://www.laku6.com/jual/express/samsung-galaxy-j7-prime-gold-32gb-bekas-1'
#url = 'https://www.matahari.com/bhatara-batik-sekar-fashion-wanita-putih-p4844767.html'
#url = 'https://www.ralali.com/v/arluxputramandiri/product/Beras-Pak-Boss-Setra-Ramos-Premium-25-KG'
url = 'https://www.blanja.com/katalog/p/fas/agrapana-baju-batik-pria-lengan-panjang-batik-premium-kemeja-batik-pria-lengan-panjang-samitra-18985017'

#Get platform name
host = tldextract.extract(url)
platform = host.domain.title()

#Get product information
warnings.filterwarnings("ignore")
og = opengraph.OpenGraph(url=url, useragent='Mozilla/5.0')

#Populate data object
data = {}
data['platform'] = platform
if hasattr(og, 'title'): data['name'] = og.title
if hasattr(og, 'image'): data['image'] = og.image

#Return JSON object
print(data)