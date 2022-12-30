import os
import telebot
import openai
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()
TELEGRAM_APIKEY = os.environ.get('TELEGRAM_APIKEY')
OPENAI_APIKEY = os.environ.get('OPENAI_APIKEY')

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}