import ollama

response = ollama.chat(model='llama2', messages=[
  {
    'role': 'user',
    'content': 'are birds real?',
  },
])
print(response['message']['content'])