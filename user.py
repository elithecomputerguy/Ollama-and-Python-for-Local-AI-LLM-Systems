import ollama

import os

def ask(query):
    query = f'{query} - answer in 25 or fewer words'
    response = ollama.chat(model='llama2:7b', messages=[
    {
        'role': 'user',
        'content': query,
    },
    ])
    response = response['message']['content']

    return response

os.system('clear')
while True:
    query = input('how can i help you?  ')
    os.system('clear')
    answer = ask(query)
    print(f'Question: {query}')
    print(answer)