#Tanisha Matthews
#Database Development and Use
#April 17, 2021



import pymongo
from pymongo import MongoClient

url = "mongodb://admin:admin@cluster0-shard-00-00.rg689.mongodb.net:27017,cluster0-shard-00-01.rg689.mongodb.net:27017,cluster0-shard-00-02.rg689.mongodb.net:27017/pytech?ssl=true&replicaSet=atlas-pahvqn-shard-0&authSource=admin&retryWrites=true&w=majority"

client = pymongo.MongoClient(url)
db = client.pytech
collection = db.students

students = db.students

student_list = students.find({})

# display message 
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

# loop over the collection and output the results 
for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# update student_id 1007
result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Crockett"}})

# find the updated student document 
davy = students.find_one({"student_id": "1007"})

# display message
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")

# output the updated document to the terminal window
print("  Student ID: " + davy["student_id"] + "\n  First Name: " + davy["first_name"] + "\n  Last Name: " + davy["last_name"] + "\n")
