import requests
from pprint import pprint

url='http://arch-ps-2:8087/rest'
headers={'X-Api-Key':'85a39ae85a156b2ab184ce0a709e964e','X-Api-User':'admin'}
rslt = requests.get(f'{url}/login',headers=headers)
#rslt = requests.get(f'{url}/user',headers=headers)
rslt = requests.get(f'{url}',headers=headers)
pprint (rslt.text)
pass
