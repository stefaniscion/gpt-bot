import os
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

def parse_message(message):
    print("message-->",message)
    chat_id = message['message']['chat']['id']
    txt = message['message']['text']
    print("chat_id-->", chat_id)
    print("txt-->", txt)
    return chat_id,txt

def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': text
    }
    r = requests.post(url,json=payload)
    return r