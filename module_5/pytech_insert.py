




import pymongo
from pymongo import MongoClient

url = "mongodb://admin:admin@cluster0-shard-00-00.rg689.mongodb.net:27017,cluster0-shard-00-01.rg689.mongodb.net:27017,cluster0-shard-00-02.rg689.mongodb.net:27017/pytech?ssl=true&replicaSet=atlas-pahvqn-shard-0&authSource=admin&retryWrites=true&w=majority"

client = pymongo.MongoClient(url)
db = client.pytech
collection = db.students

#Davy Jones document
davy= {
    "student_id": "1007",
    "first_name": "Davy",
    "last_name": "Jones",

    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "3.5",
            "start_date": "January 04, 2021",
            "end_date": "May 05, 2021",
            "courses": [
                {
                    "course_id": "NAU421",
                    "description": "Sailing the High Seas",
                    "instructor": "Professor Blackbeard",
                    "grade": "A"
                },
                {
                    "course_id": "NAU430",
                    "description": "Nautical Nuances",
                    "instructor": "Ferdinand Magellan",
                    "grade": "B"
                }
            ]
        }
    ]
 
}

        
    
# Francis Drake document 
francis = {
    "student_id": "1008",
    "first_name": "Francis",
    "last_name": "Drake",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "3.7",
            "start_date": "January 04, 2021",
            "end_date": "May 05, 2021",
            "courses": [
                {
                    "course_id": "NAU 430",
                    "description": "Nautical Nuances",
                    "instructor": "Ferdinand Magellan",
                    "grade": "C"
                },
                {
                    "course_id": "SCD620",
                    "description": "Knot the Navy",
                    "instructor": "Professor Hawkins",
                    "grade": "A"
                }
            ]
        }
    ]
}
#Anne Bonny document
anne = {
    "student_id": "1009",
    "first_name": "Anne",
    "last_name": "Bonny",
    "enrollments": [
        {
            "term": "Session 2",
            "gpa": "2.7",
            "start_date": "January 04, 2021",
            "end_date": "May 05, 2021",
            "courses": [
                {
                    "course_id": "EXP310",
                    "description": "Mastheads and Figureheads",
                    "instructor": "Professor Mary Read",
                    "grade": "C"
                },
                {
                    "course_id": "SCD 620",
                    "description": "Knot the Navy",
                    "instructor": "Professor Hawkins",
                    "grade": "B"
                }
            ]
        }
    ]
}

students = db.students

print("--INSERT STATEMENTS--")
davy_student_id = students.insert_one(davy).inserted_id
print("Inserted student record Davy Jones into the students collection with document_id " + str(davy_student_id))

francis_student_id = students.insert_one(francis).inserted_id
print("Inserted student record Francis Drake into the students collection with document_id " + str(francis_student_id))

anne_student_id = students.insert_one(anne).inserted_id
print("  Inserted student record Anne Bonny into the students collection with document_id " + str(anne_student_id))