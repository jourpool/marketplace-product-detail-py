# Indonesia Marketplace Product Detail with Python
Pull product information detail from major Indonesia marketplace with Python.

## Supported Marketplace
* JD.ID
* Orami
* Blibli
* Shopee
* Lazada
* Zalora
* Sociolla
* Bhinneka
* Bukalapak

## Marketplace That Require Proxies
* Blibli
* Lazada
* Bukalapak  
<br />

Add proxy to the code:
```python
proxy = { 
    'http'  : "http://YourProxyIP:80", 
    'https' : "https://YourProxyIP:80"
}
```

Include it on every request:
```python
response = requests.post(url_token, headers=headers, proxies=proxy).json()
```