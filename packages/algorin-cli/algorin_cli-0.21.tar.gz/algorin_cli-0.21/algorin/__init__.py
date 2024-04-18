# algorin/__init__.py

# Importar funciones específicas de los módulos para hacerlas disponibles en el nivel del paquete
from .main import main_menu, execute_transcript
from .chatbot import setup_api_key, chat_with_gpt, chat_without_context
from .file_extractor import extract_text

# Puedes optar por exponer solo ciertas funciones o todas, dependiendo de cómo desees que se use tu módulo.
__all__ = ['main_menu', 'execute_transcript', 'setup_api_key', 'chat_with_gpt', 'chat_without_context', 'extract_text']
