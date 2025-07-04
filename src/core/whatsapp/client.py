import requests
from typing import Dict, Any, Optional
from config.whatsapp import whatsapp_config
from src.utils.exceptions import WhatsAppAPIError

class WhatsAppClient:
    def __init__(self):
        self.config = whatsapp_config
    
    async def send_text_message(self, to: str, message: str) -> Dict[str, Any]:
        """Send a text message