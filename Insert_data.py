import pymongo
import requests


def clean(d: dict) -> dict:
    filters = ['id', 'uid', 'avatar', 'subscription', 'address']
    for i in filters:
        d.pop(i)

    return d


URL = "https://random-data-api.com/api/users/random_user?size=50"

response = requests.get(url=URL)

data = response.json()

data = list(filter(lambda x: clean(x), data))
[print(i) for i in data]
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb = client['Employee']
empinfo = mydb.employeeinformation

empinfo.insert_many(data)
