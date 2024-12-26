from pymongo import MongoClient

client = MongoClient("mongodb+srv://<username>:<password>@resumeranking.dswr0.mongodb.net/?retryWrites=true&w=majority&appName=ResumeRanking")

db = client.todo_db

collection_name = db['todo_collection']