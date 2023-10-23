from database import *
from typing import Optional
import openai,os, datetime, json
from bson import ObjectId
from fastapi import HTTPException
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from gpt4models import *

app = FastAPI()

origins = [ 
           "https://localhost:5173",
           "hhtps://localhost:5174",
           "https://localhost:4173",
           "https://localhost:3000",
           ]

app.add_middleware( 
                   CORSMiddleware, 
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"ThespAIn": "/Welcome To DiamondAI Backend Code"}

# User registration endpoint
@app.post("/getstarted")
async def get_started(email):
    # Check if the email already exists in the database
    existing_user = db.users.find_one({"user_email": email})
    if existing_user:
        print("login successfully")
        # Email already exists, no need to insert it again
        return {"message": "User signed in successfully"}
    else:
        print("signed up successfully")
        # Email doesn't exist, so insert it as a new user
        db.users.insert_one({"user_email": email})
        return {"message": "User Registered successfully"}

@app.post("/thespain")
async def post_text(email, text):
    message = model(prompt=text, character=thespAIn)
    db.chat_history.insert_one({
        "email": email,
        "prompt": text,
        "completion": message,
    })
    print("result posted in database successfully")
    return message

@app.post("/medical")
async def post_text(email, text):
    message = model(prompt=text, character=medicAI)
    db.chat_history.insert_one({
        "email": email,
        "prompt": text,
        "completion": message,
    })
    print("result posted in database successfully")
    return message

@app.post("/finance")
async def post_text(email, text):
    message = model(prompt=text, character=financAI)
    db.chat_history.insert_one({
        "email": email,
        "prompt": text,
        "completion": message,
    })
    print("result posted in database successfully")
    return message

@app.post("/psychology")
async def post_text(email, text):
    message = model(prompt=text, character=PsychologyAI)
    db.chat_history.insert_one({
        "email": email,
        "prompt": text,
        "completion": message,
    })
    print("result posted in database successfully")
    return message

@app.post("/relationship")
async def post_text(email, text):
    message = model(prompt=text, character=RelationshipAI)
    db.chat_history.insert_one({
        "email": email,
        "prompt": text,
        "completion": message,
    })
    print("result posted in database successfully")
    return message

@app.post("/teacher")
async def post_text(email, text):
    message = model(prompt=text, character=TeacherAI)
    db.chat_history.insert_one({
        "email": email,
        "prompt": text,
        "completion": message,
    })
    print("result posted in database successfully")
    return message

# get speech
@app.post("/speech")
async def post_speech(email, file: UploadFile = File(...)):
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())
    audio_input = open(file.filename, "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_input)
    
    text_decoded = transcript["text"]
    
    if not text_decoded:
        raise HTTPException(status_code=400, detail="Failed to decode Audio")
    
    message = model(prompt=text_decoded)
    return message

@app.get("/history/")
async def get_chat_history(email: str):
    # Find chat history in MongoDB and convert ObjectId to strings
    chat_history = list(
        {
            "_id": str(item["_id"]),  # Convert ObjectId to string
            "email": item["email"],
            "prompt": item["prompt"],
            "completion": item["completion"],
        }
        for item in db.chat_history.find({"email": email})
    )
    # Check if chat history is empty and return an HTTPException if necessary
    if not chat_history:
        raise HTTPException(status_code=404, detail="Chat history not found")
    return {"chat_history": chat_history}

@app.delete("/conversation/{conversation_id}")
async def delete_conversation(conversation_id: str):
    # Attempt to find the conversation in the database and delete it
    result = db.chat_history.delete_one({"_id": ObjectId(conversation_id)})

    # Check if the conversation was found and deleted
    if result.deleted_count == 1:
        return {"message": "Conversation deleted successfully"}
    else:
        # If the conversation with the given _id was not found
        raise HTTPException(status_code=404, detail="Conversation not found")