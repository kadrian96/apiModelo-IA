from openai import OpenAI
from typing_extensions import override
from openai import AssistantEventHandler

client = OpenAI(
  organization='org-mZE8a7Qj1jjTBeTDLY1ecJ3C',
  project='proj_lsdxQWDy02Q24C1obcsrvUNA',
  api_key="sk-proj-hj8MJiZj9o0w30KmmjfxT3BlbkFJ8m79aosvJ7jqAnFWWNJ1"
)



my_assistants = client.beta.assistants.list(
    order="desc",
    limit="20",
)
assistant_id=my_assistants.data[0].id
    
thread = client.beta.threads.create()

def enviar_mensaje(mensaje):
    message = client.beta.threads.messages.create(
     thread_id=thread.id,
    role="user",
    content=mensaje
    )
    run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id=assistant_id,
  
    )
    if run.status == 'completed': 
        messages = client.beta.threads.messages.list(
        thread_id=thread.id
    )
        asistantResponse=messages.data[0].content[0].text.value
        
    else:
        asistantResponse=run.status
    return asistantResponse