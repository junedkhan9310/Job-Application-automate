
import re
import json
import global_var
import openai


client = openai.OpenAI(api_key=global_var.gpt_API_kye)

def clean_markdown_json(md_string):
    # Remove Markdown fences like ```json ... ```
    cleaned = re.sub(r'^```json\n|```$', '', md_string.strip(), flags=re.MULTILINE)
    return json.loads(cleaned)

    
def new_chatgpt_chat_withID(q,limit):
    try:
        
        data = f'{{"question": "{q}", "limit": "{limit}"}}'
        response = client.responses.create(
        prompt={
            "id": "pmpt_68b059XXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
            "version": "3",
            "variables": {
            "input_data": f"{data}"
            }
        }
        )
        parsed_data = clean_markdown_json(response.output_text)

        return parsed_data 

    except Exception as e:
        print(e)

def new_chatgpt_chat_withID_for_drop_down(q,select_from):
    try:
        
        data = f'{{"question": "{q}", "options": "{select_from}"}}'
        response = client.responses.create(
        prompt={
            "id": "pmpt_68b059XXXXXXXXXXXXXXXXXXXXXXXXXXXXXx",
            "version": "3",
            "variables": {
            "input_data": f"{data}"
            }
        }
        )
        parsed_data = clean_markdown_json(response.output_text)

        return parsed_data 

    except Exception as e:
        print(e)

