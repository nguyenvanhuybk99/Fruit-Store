import requests

url = "http://0.0.0.0:8000/manager/product"

payload={'name': 'orange',
'quantity_in_stock': '3',
'price': '6'}
files=[

]
headers = {}

response = requests.request("GET", url, headers=headers, data=payload, files=files)

print(response.text)
