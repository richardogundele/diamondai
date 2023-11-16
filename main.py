from database import *
import openai,os, datetime, json
from fastapi import Path
import pymongo
from bson import ObjectId
from fastapi import HTTPException
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from gpt4models import *

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

# origins = [
#            "https://richard-9hla.onrender.com/",
#            "https://diamond-et14.onrender.com/",
#            "https://localhost:4000",
#            ]

app.add_middleware( 
                   CORSMiddleware, 
                   allow_origins=["*"],
                   allow_credentials=False,
                   allow_methods=["*"],
                   allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"ThespAIn": "/Welcome To DiamondAI Backend Code"}

# User registration endpoint
@app.post("/start")
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
    
'''  Thespian App'''

@app.post("/thespian")
async def post_text(email, text):
    message = model(prompt=text, character=thespAIn)
    thdb.chat_history.insert_one({
        "email": email,
        "prompt": text,
        "completion": message,
    })
    print("result posted in database successfully")
    return message

@app.get("/thespianhistory")
async def get_chat_history(email: str):
    # Find chat history in MongoDB and convert ObjectId to strings
    chat_history = list(
        {
            "_id": str(item["_id"]),  # Convert ObjectId to string
            "email": item["email"],
            "prompt": item["prompt"],
            "completion": item["completion"],
        }
        for item in thdb.chat_history.find({"email": email})
    )
    # Check if chat history is empty and return an HTTPException if necessary
    if not chat_history:
        raise HTTPException(status_code=404, detail="Chat history not found")
    return {"chat_history": chat_history}

@app.delete("/thespianconversation")
async def delete_conversation(email):
    collection = thdb["chat_history"]
    # Delete all documents with the specified email address
    result = collection.delete_many({"email": email})
    # Check how many documents were deleted
    return(f"{result.deleted_count} documents with email {email} deleted successfully")

''' Medical App'''
@app.post("/medical")
async def post_text(email, text):
    message = model(prompt=text, character=medicAI)
    mdb.chat_history.insert_one({
        "email": email,
        "prompt": text,
        "completion": message,
    })
    print("result posted in database successfully")
    return message

@app.get("/medicalhistory")
async def get_chat_history(email: str):
    # Find chat history in MongoDB and convert ObjectId to strings
    chat_history = list(
        {
            "_id": str(item["_id"]),  # Convert ObjectId to string
            "email": item["email"],
            "prompt": item["prompt"],
            "completion": item["completion"],
        }
        for item in mdb.chat_history.find({"email": email})
    )
    # Check if chat history is empty and return an HTTPException if necessary
    if not chat_history:
        raise HTTPException(status_code=404, detail="Chat history not found")
    return {"chat_history": chat_history}

@app.delete("/medicalconversation")
async def delete_conversation(email):
    collection = mdb["chat_history"]
    # Delete all documents with the specified email address
    result = collection.delete_many({"email": email})
    # Check how many documents were deleted
    return(f"{result.deleted_count} documents with email {email} deleted successfully")

''' Finance App '''
@app.post("/finance")
async def post_text(email, text):
    message = model(prompt=text, character=financAI)
    fdb.chat_history.insert_one({
        "email": email,
        "prompt": text,
        "completion": message,
    })
    print("result posted in database successfully")
    return message

@app.get("/financehistory")
async def get_chat_history(email: str):
    # Find chat history in MongoDB and convert ObjectId to strings
    chat_history = list(
        {
            "_id": str(item["_id"]),  # Convert ObjectId to string
            "email": item["email"],
            "prompt": item["prompt"],
            "completion": item["completion"],
        }
        for item in fdb.chat_history.find({"email": email})
    )
    # Check if chat history is empty and return an HTTPException if necessary
    if not chat_history:
        raise HTTPException(status_code=404, detail="Chat history not found")
    return {"chat_history": chat_history}

@app.delete("/financeconversation")
async def delete_conversation(email):
    collection = fdb["chat_history"]
    # Delete all documents with the specified email address
    result = collection.delete_many({"email": email})
    # Check how many documents were deleted
    return(f"{result.deleted_count} documents with email {email} deleted successfully")

''' Psychology App '''
@app.post("/psychology")
async def post_text(email, text):
    message = model(prompt=text, character=PsychologyAI)
    pdb.chat_history.insert_one({
        "email": email,
        "prompt": text,
        "completion": message,
    })
    print("result posted in database successfully")
    return message

@app.get("/psychologyhistory")
async def get_chat_history(email: str):
    # Find chat history in MongoDB and convert ObjectId to strings
    chat_history = list(
        {
            "_id": str(item["_id"]),  # Convert ObjectId to string
            "email": item["email"],
            "prompt": item["prompt"],
            "completion": item["completion"],
        }
        for item in fdb.chat_history.find({"email": email})
    )
    # Check if chat history is empty and return an HTTPException if necessary
    if not chat_history:
        raise HTTPException(status_code=404, detail="Chat history not found")
    return {"chat_history": chat_history}

@app.delete("/psychologyconversation")
async def delete_conversation(email):
    collection = pdb["chat_history"]
    # Delete all documents with the specified email address
    result = collection.delete_many({"email": email})
    # Check how many documents were deleted
    return(f"{result.deleted_count} documents with email {email} deleted successfully")

''' Relationship App'''
@app.post("/relationship")
async def post_text(email, text):
    message = model(prompt=text, character=RelationshipAI)
    rdb.chat_history.insert_one({
        "email": email,
        "prompt": text,
        "completion": message,
    })
    print("result posted in database successfully")
    return message

@app.get("/relationshiphistory")
async def get_chat_history(email: str):
    # Find chat history in MongoDB and convert ObjectId to strings
    chat_history = list(
        {
            "_id": str(item["_id"]),  # Convert ObjectId to string
            "email": item["email"],
            "prompt": item["prompt"],
            "completion": item["completion"],
        }
        for item in rdb.chat_history.find({"email": email})
    )
    # Check if chat history is empty and return an HTTPException if necessary
    if not chat_history:
        raise HTTPException(status_code=404, detail="Chat history not found")
    return {"chat_history": chat_history}

@app.delete("/relationshipconversation")
async def delete_conversation(email):
    collection = rdb["chat_history"]
    # Delete all documents with the specified email address
    result = collection.delete_many({"email": email})
    # Check how many documents were deleted
    return(f"{result.deleted_count} documents with email {email} deleted successfully")

''' Teacher App'''
@app.post("/teacher")
async def post_text(email, text):
    message = model(prompt=text, character=TeacherAI)
    tedb.chat_history.insert_one({
        "email": email,
        "prompt": text,
        "completion": message,
    })
    print("result posted in database successfully")
    return message

@app.get("/teacherhistory")
async def get_chat_history(email: str):
    # Find chat history in MongoDB and convert ObjectId to strings
    chat_history = list(
        {
            "_id": str(item["_id"]),  # Convert ObjectId to string
            "email": item["email"],
            "prompt": item["prompt"],
            "completion": item["completion"],
        }
        for item in tedb.chat_history.find({"email": email})
    )
    # Check if chat history is empty and return an HTTPException if necessary
    if not chat_history:
        raise HTTPException(status_code=404, detail="Chat history not found")
    return {"chat_history": chat_history}

@app.delete("/teacherconversation")
async def delete_conversation(email):
    collection = tedb["chat_history"]
    # Delete all documents with the specified email address
    result = collection.delete_many({"email": email})
    # Check how many documents were deleted
    return(f"{result.deleted_count} documents with email {email} deleted successfully")

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

