import requests
import time
import json

valute = input()
def val():
    a = requests.get("https://blockchain.info/ru/ticker").text
    k = json.dumps(a)
    return json.loads(k)


dict = json.loads(val())
print(dict[valute]['buy'])
