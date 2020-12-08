import pymongo

client = pymongo.MongoClient(
    'mongodb+srv://Agnieszka:Fryderyk2012@cluster0.qgcux.mongodb.net/users?retryWrites=true&w=majority')
# from mongo Atlas choose connect and connect your application

# the protocol, ip address and port by default - but if you have mongo locally

# create a database

mydb = client['users']
# information = mydb.employeeinformation  # create a collection if is not created

# record = [{
#     "firstname": "Agnes",
#     "second_name": "Gruszecka",
#     "department": "Statistics"},
# {
#     "firstname": "Frycek",
#     "second_name": "Gruszecki",
#     "department": "Student"},
# {
#     "firstname": "Marcin",
#     "second_name": "Gruszecki",
#     "department": "Statistics"},
# ]
# information.insert_many(record)
# print(information.find_one({'firstname':'Agnes'}))

# for record in information.find():
#     print(record)

# ######### Query the JSON documents based on equality conditions
# for record in information.find({'firstname':'Agnes'}):
#     print(record)

# ###### query operators

# information.insert_many([{"firstanme": "Krish", "second_name": "Naik", "department": {"morning": 1, "afternoon": 2}}])


# ###### aggregation

# agg_result = information.aggregate(
#     [{"$group": {"_id": "$firstname", "Total firstnames": {"$sum": 1}}}]
# )
# for i in agg_result:
#     print(i)

# #### datetime
import datetime

# mydb = client['users']
# information = mydb.data_with_data  # create a collection if is not created

# data = [{"_id": 6, "item": "abc", "price": 10, "quantity": 2, "date": datetime.datetime.utcnow()},
#         {"_id": 7, "item": "def", "price": 20, "quantity": 1, "date": datetime.datetime.utcnow()},
#         {"_id": 8, "item": "abc", "price": 5, "quantity": 5, "date": datetime.datetime.utcnow()},
#         {"_id": 9, "item": "def", "price": 10, "quantity": 12, "date": datetime.datetime.utcnow()},
#         {"_id": 10, "item": "def", "price": 5, "quantity": 22, "date": datetime.datetime.utcnow()},
#
#         ]
# information.insert_many(data)

# ##### calculate average quantity and average price

# agg_result = information.aggregate([
#     {"$group": {"_id": "$item", "avgAmount": {"$avg": {"$multiply": ["$price", "$quantity"]}},
#                 "avgQuantity": {"$avg": "$quantity"}}}])
#
# for i in agg_result:
#     print(i)

# books = [
#     {
#         "_id": 1,
#         'title': "abc123",
#         'isbn': "0001122223334",
#         'author': {'last': "zzz", 'first': "aaa"},
#         'copies': 5,
#         'lastModified': "2016-07-28"
#     },
#     {
#         "_id": 2,
#         'title': "Baked Goods",
#         'isbn': "9999999999999",
#         'author': {'last': "xyz", 'first': "abc", 'middle': ""},
#         'copies': 2,
#         'lastModified': "2017-07-21"
#     },
#     {
#         "_id": 3,
#         'title': "Ice Cream Cakes",
#         'isbn': "8888888888888",
#         'author': {'last': "xyz", 'first': "abc", 'middle': "mmm"},
#         'copies': 5,
#         'lastModified': "2017-07-22"
#     }
# ]
#
# collection = mydb['Books']  # create a collection if is not created
# # collection.insert_many(books)
#
# for i in collection.aggregate([{'$project': {"title": 1}}]):
#     print(i)
