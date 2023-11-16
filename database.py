import certifi, pprint, os
from pymongo import MongoClient

'''MONGODB DATABASE - to store user emails, conversations of users'''

# password = os.getenv("mongopassword")

password = "gbogO2020$"

mongo_uri = f"mongodb+srv://richardogundele:{password}@cluster0.jfqn1lj.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(mongo_uri, tlsCAFile=certifi.where())

#Get or create database with name 'chatapp' to store the whole conversation and emails
db = client.get_database("diamond")
thdb = client.get_database("thespian")
mdb = client.get_database("medical")
fdb = client.get_database("finance")
pdb = client.get_database("psychology")
rdb = client.get_database("relationship")
tedb = client.get_database("teacher")
