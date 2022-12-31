import os
import requests
from dotenv import load_dotenv
from fastapi import FastAPI,Request
from gpt import get_gpt_response

# Load environment variables
load_dotenv()
TELEGRAM_APIKEY = os.environ.get('TELEGRAM_APIKEY')
OPENAI_APIKEY = os.environ.get('OPENAI_APIKEY')
AUTHORIZED_USERS = os.environ.get('AUTHORIZED_USERS').split(",")

app = FastAPI()

# Test route
@app.get("/")
async def root():
    return {"message": "Hello World!"}
    
# Telegram route
@app.post("/telegram/")
async def root(request: Request):
    request = await request.json()
    user_id = request['message']['from']['id']
    chat_id = request['message']['chat']['id']
    request_text =  request['message']['text']
    if request_text == "/start":
        response_text = "Ciao, sono un bot che usa GPT-3 per rispondere ai messaggi. Scrivi qualcosa e vediamo cosa succede!"
    elif str(user_id) not in AUTHORIZED_USERS:
        response_text = "Non sei autorizzato ad usare questo bot. (User ID: "+str(user_id)+")"
    else:
        response_text = get_gpt_response(request_text,OPENAI_APIKEY)
    #send message to telegram
    url = 'https://api.telegram.org/bot'+str(TELEGRAM_APIKEY)+'/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': response_text,
        'parse_mode': 'MarkdownV2'
    }
    r = requests.get(url, params=params)
    print(r.json())
    return {"message": "Message sent successfully!"}