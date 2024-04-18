from openai import OpenAI

client = None

def setup_api_key(key):
    global client
    # Inicializa el cliente de OpenAI una vez que la API key está configurada
    client = OpenAI(api_key=key)

def chat_with_gpt(initial_context):
    global client
    if client is None:
        print("Cliente de OpenAI no inicializado. Por favor, ejecute setup_api_key primero.")
        return

    chat_log = [{"role": "system", "content": "You are a helpful assistant."}]
    if initial_context:
        chat_log.append({"role": "user", "content": initial_context})

    while True:
        user_input = input("Tú: ")
        if user_input.lower() == "exit":
            print("Terminando chat...")
            break

        chat_log.append({"role": "user", "content": user_input})

        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=chat_log
            )
            bot_response = response.choices[0].message.content
            print("ChatGPT: ", bot_response)

            chat_log.append({"role": "assistant", "content": bot_response})
        except Exception as e:
            print(f"Error al generar la respuesta del chat: {e}")
            break

def chat_without_context():
    chat_with_gpt(None)
