from fastapi import FastAPI
from pymongo import MongoClient

app = FastAPI()

CONNECTION_URI = "mongodb+srv://Bangie:1mirosavljev1@cluster0.zcy3e.mongodb.net/test"
client = MongoClient(CONNECTION_URI)
app.db = client.WebChatApp.Users
