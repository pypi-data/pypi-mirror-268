# tuapp/__init__.py

# Importar funciones específicas de los módulos para hacerlas disponibles en el nivel del paquete
from main import main_menu
from file_extractor import extract_text
from chatbot import chat_with_gpt, setup_api_key

# Puedes optar por exponer solo ciertas funciones o todas, dependiendo de cómo desees que se use tu módulo.
__all__ = ['main_menu', 'extract_text', 'chat_with_gpt', 'setup_api_key']
