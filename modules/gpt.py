import os
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_APIKEY = os.environ.get('OPENAI_APIKEY')

def get_gpt_response(prompt,memory):
    openai.api_key = OPENAI_APIKEY
    gpt_response = openai.Completion.create(
        model="text-davinci-003", 
        prompt=prompt, 
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7
    )
    response_text = gpt_response["choices"][0]["text"]
    response_token = gpt_response["choices"][0]
    return response_text,response_token