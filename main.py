import pymongo
import requests

client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')
mydb = client['Employee']
empinfo = mydb.employeeinformation

## Simple way of querying
print(empinfo.find_one())

## Select * from employeeinformation
for record in empinfo.find():
    print(record)

## Query the json documents based on equality conditions
## Select * from employeeinformation where firstname = Jairaj
print("WHERE CLAUSE")

for record in empinfo.find({'fname': 'Jairaj'}):
    print(record)

print('Query Operators ($in,$lt,$gt)')
## Query Operators ($in,$lt,$gt)
for record in empinfo.find({'qualification': {'$in': ['phd', 'master']}}):
    print(record)

print("And and Query Operators")
## And and Query Operators
for record in empinfo.find({'qualification': 'master', 'age': {'$lt': 35}}):
    print(record)

## OR operators
print("OR operators")
for record in empinfo.find({'$or': [{'first_name': 'Modesto'}, {'qualification': 'master'}]}):
    print(record)

## AND operators
print("AND operators")
for record in empinfo.find({'$and': [{'first_name': 'Modesto'}, {'qualification': 'master'}]}):
    print(record)

inventory = mydb.inventory
# inventory.insert_many(
#     [
#         {'item': "journal", 'qty': 25, 'size': {'h': 14, 'w': 21, 'uom': "cm"}, 'status': "A"},
#         {'item': "notebook", 'qty': 50, 'size': {'h': 8.5, 'w': 11, 'uom': "in"}, 'status': "A"},
#         {'item': "paper", 'qty': 100, 'size': {'h': 8.5, 'w': 11, 'uom': "in"}, 'status': "D"},
#         {'item': "planner", 'qty': 75, 'size': {'h': 22.85, 'w': 30, 'uom': "cm"}, 'status': "D"},
#         {'item': "postcard", 'qty': 45, 'size': {'h': 10, 'w': 15.25, 'uom': "cm"}, 'status': "A"}
#     ]
# );

for records in inventory.find({'size': { 'h': 14, 'w': 21,'uom': "cm" }}):
    print(records)
