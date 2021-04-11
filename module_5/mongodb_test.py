#Tanisha Matthews
#April 9, 2021
#Module 5.2


from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.rg689.mongodb.net/pytech?retryWrites=true&w=majority"

client = MongoClient(url)

db = client.pytech

print(db.list_collection_names())

print("--Pytech Collection List--")
print("['students']")

print("End of program press any key to exit")
