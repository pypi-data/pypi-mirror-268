# algorin/__init__.py

# Importar funciones específicas de los módulos para hacerlas disponibles en el nivel del paquete
from .file_extractor import extract_text
from .chatbot import setup_api_key, chat_with_gpt, chat_without_context
from .main import main_menu

# Puedes optar por exponer solo ciertas funciones o todas, dependiendo de cómo desees que se use tu módulo.
__all__ = ['main_menu', 'extract_text', 'setup_api_key', 'chat_with_gpt', 'chat_without_context']
