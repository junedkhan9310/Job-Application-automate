import re
import json
import openai
import os


from config import Config
from utils.print_exception import print_exception_details

client = openai.OpenAI(api_key=Config.gpt_API_kye)



def clean_markdown_json(md_string):
    # Remove Markdown fences like ```json ... ```
    cleaned = re.sub(r'^```json\n|```$', '', md_string.strip(), flags=re.MULTILINE)
    return json.loads(cleaned)

def mock_chatgpt_chat_withID(data):

    if "years" in data or "many" in data or "experience" in data:
        return 5
    else:
        return "This is a mock response for the question: "

def mock_chatgpt_chat_withID_for_drop_down(select_from):
    options = select_from.split("|")
    # return any random option
    return options[0] if options else ""


    
def new_chatgpt_chat_withID(q,limit):
    try:
        
        data = f'{{"question": "{q}", "limit": "{limit}"}}'
        response =  mock_chatgpt_chat_withID(data)
        # response = client.responses.create(
        # prompt={
        #     "id":Config.gpt_Prompt_id,
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
        response =  mock_chatgpt_chat_withID_for_drop_down(select_from)

        # response = client.responses.create(
        # prompt={
        #     "id":Config.gpt_Prompt_id,
        #     "version": "3",
        #     "variables": {
        #     "input_data": f"{data}"
        #     }
        # }
        # )
        # parsed_data = clean_markdown_json(response.output_text)

        return response 

    except Exception as e:
        print_exception_details(e)

