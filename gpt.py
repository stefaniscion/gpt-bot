import openai

def get_gpt_response(prompt,api_key):
    temperature = 0.5
    openai.api_key = api_key
    gpt_response = openai.Completion.create(model="text-davinci-003", prompt=prompt, temperature=temperature, max_tokens=4097-28, top_p=1, frequency_penalty=0, presence_penalty=0)
    response = ""
    for row in gpt_response["choices"]:
        response = response + str(row["text"])
    return response