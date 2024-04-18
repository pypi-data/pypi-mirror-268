import openai

api_key = None

def setup_api_key(key):
    global api_key
    api_key = key

def chat_with_gpt(initial_context):
    if not api_key:
        print("API key no configurada.")
        return
    
    openai.api_key = api_key
    chat_log = [{"role": "system", "content": "You are a helpful assistant."}]
    if initial_context:
        chat_log.append({"role": "user", "content": initial_context})
    
    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "exit":
            print("Terminando chat...")
            break
        
        chat_log.append({"role": "user", "content": user_input})
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_log
        )
        
        bot_response = response.choices[0].message['content']
        print("ChatGPT: ", bot_response)
        
        chat_log.append({"role": "assistant", "content": bot_response})

def chat_without_context():
    chat_with_gpt(None)
