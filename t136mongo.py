from pymongo import MongoClient
import pprint



myclient = MongoClient("mongodb+srv://user99:Lena8484@cluster0.4vhhh.mongodb.net/sample_restaurants?retryWrites=true&w=majority")
mydb = myclient.sample_restaurants
mycollection = mydb.restaurants
mycount=mycollection.count_documents({})
print(mycount)
for myrestaurant in mycollection.find({"address.zipcode":"10024"}):
    pprint.pprint(myrestaurant)