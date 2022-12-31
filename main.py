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
    response_text = get_gpt_response(request_text,OPENAI_APIKEY)
    if str(user_id) not in AUTHORIZED_USERS:
        print("Authorized users: "+str(AUTHORIZED_USERS))
        print("Unauthorized user: "+str(user_id))
        response_text = "Non sei autorizzato ad usare questo bot."
    #send message to telegram
    url = 'https://api.telegram.org/bot'+str(TELEGRAM_APIKEY)+'/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': response_text
    }
    r = requests.get(url, params=params)
    print(r.json())
    return {"message": "Message sent successfully!"}