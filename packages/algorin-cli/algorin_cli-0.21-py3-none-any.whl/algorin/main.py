#!/usr/bin/env python3
import os
from .file_extractor import extract_text
from .chatbot import setup_api_key, chat_with_gpt, chat_without_context

def execute_transcript(path):
    if not os.path.exists(path):
        print("La ruta especificada no existe.")
        return ""
    
    # Verifica si el path es un directorio o un archivo directamente
    if os.path.isdir(path):
        files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith(('.txt', '.pdf', '.docx', '.pptx'))]
    elif os.path.isfile(path) and path.endswith(('.txt', '.pdf', '.docx', '.pptx')):
        files = [path]  # Trata el archivo directamente como un elemento de lista
    else:
        print("El path proporcionado no es un directorio ni un archivo soportado.")
        return ""
    
    texts = []
    for file_path in files:
        try:
            text = extract_text(file_path)
            texts.append(text)
        except Exception as e:
            print(f"No se pudo procesar el archivo {os.path.basename(file_path)} debido a un error: {e}")
    
    combined_text = "\n\n".join(texts)
    return combined_text

def main_menu():
    print("Bienvenido al CLI de Documentos y ChatGPT")
    api_key = input("Por favor, ingrese su API key de OpenAI: ")
    setup_api_key(api_key)
    
    while True:
        print("\nMenú:")
        print("1. Extraer texto y chat con contexto")
        print("2. Chat directo sin contexto")
        print("3. Salir")
        choice = input("Ingrese su elección (1-3): ")
        
        if choice == '1':
            path = input("Por favor, ingrese la ruta donde están los archivos: ")
            context = execute_transcript(path)
            if context:
                print("Iniciando chat con contexto...")
                chat_with_gpt(context)
            else:
                print("No se encontró texto válido para usar como contexto.")
        elif choice == '2':
            print("Iniciando chat directo sin contexto...")
            chat_without_context()
        elif choice == '3':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main_menu()
