
import re
import json
import openai
import os
from main import print_exception_details


from config import Config

client = openai.OpenAI(api_key=Config.gpt_API_kye)



def clean_markdown_json(md_string):
    # Remove Markdown fences like ```json ... ```
    cleaned = re.sub(r'^```json\n|```$', '', md_string.strip(), flags=re.MULTILINE)
    return json.loads(cleaned)

def mock_chatgpt_chat_withID(data):
    return {"this is how gpt will answer me like this yes"}

    
def new_chatgpt_chat_withID(q,limit):
    try:
        
        data = f'{{"question": "{q}", "limit": "{limit}"}}'
        response =  mock_chatgpt_chat_withID(data)
        # response = client.responses.create(
        # prompt={
        #     "id": os.getenv("gpt_API_kye"),
        #     "version": "3",
        #     "variables": {
        #     "input_data": f"{data}"
        #     }
        # }
        # )
        # parsed_data = clean_markdown_json(response)

        return response 

    except Exception as e:
        print_exception_details(e)

def new_chatgpt_chat_withID_for_drop_down(q,select_from):
    try:
        
        data = f'{{"question": "{q}", "options": "{select_from}"}}'
        response = client.responses.create(
        prompt={
            "id": os.getenv("gpt_API_kye"),
            "version": "3",
            "variables": {
            "input_data": f"{data}"
            }
        }
        )
        parsed_data = clean_markdown_json(response.output_text)

        return parsed_data 

    except Exception as e:
        print_exception_details(e)

