from groq import Groq
from decouple import config
from .prompts import system_prompt

def analyze_content_with_llm(file_content):
    prompt = f'''
    Analyze the following code for:
    - Code style and formatting issues
    - Potential bugs or errors
    - Best Practices

    Content:{file_content}
    
 Return a detailed JSON Response with the following structure:
    {{
        'issues':[
        {{
        'type':"<style|bug|performace_issues|best_practices>",
        'line':'<line_number>',
        'description':'<description>',
        'suggestion':'<suggestion>'
        
        }}
        ]
        
    }}
    '''

    client = Groq(api_key=config("GROQ_KEY"))
    completion =client.chat.completions.create(model='llama3-8b-8192',messages=[
        {
            'role':'system','content':system_prompt
        },

        {
            'role':'user',
            'content':prompt,

        }

    ],temperature=1,top_p=1)
    return completion.choices[0].message.content
