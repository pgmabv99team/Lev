from pymongo import MongoClient
import pprint


myclient = MongoClient(
    "mongodb+srv://user99:Lena8484@cluster0.4vhhh.mongodb.net/sample_restaurants?retryWrites=true&w=majority")
mydb = myclient.sample_restaurants
mycollection = mydb.restaurants
mycount = mycollection.count_documents({"cuisine": "Thai"})
print(mycount)

# for myrestaurant in mycollection.find({"address.zipcode":"10024"}):
# for myrestaurant in mycollection.find({"address.zipcode":"10024","cuisine":"Thai"}):
# for myrestaurant in mycollection.find({"$and":
#                                        [
#                                            {"address.zipcode": "10024"},
#                                         #    {"cuisine": "Thai"},
#                                            {"address.building":"450"}

#                                        ]
#                                        },
#                                       {"cuisine": 1, "name": 1, "address.street": 1, "_id": 0, "address.building": 1}):

#     pprint.pprint(myrestaurant)

for xx in mycollection.aggregate([
    {"$group" : {"_id":"$cuisine", "count":{"$sum":1}}}]):
     pprint.pprint(xx)



# db.restaurants.find( {$and: [
#  {"cuisine" : "Bakery"} ,
#  {"borough" : "Brooklyn"}
#  ]
# })
