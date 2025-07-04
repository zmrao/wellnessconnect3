import requests
from typing import Dict, Any
from config.settings import settings

class WhatsAppConfig:
    def __init__(self):
        self.access_token = settings.whatsapp_access_token
        self.phone_number_id = settings.whatsapp_phone_number_id
        self.verify_token = settings.whatsapp_webhook_verify_token
        self.base_url = f"https://graph.facebook.com/v18.0/{self.phone_number_id}"
        
    def get_headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
    
    def send_message(self, to: str, message: str) -> Dict[str, Any]:
        url = f"{self.base_url}/messages"
        payload = {
            "messaging_product": "whatsapp",
            "to": to,
            "type": "text",
            "text": {"body": message}
        }
        
        response = requests.post(url, json=payload, headers=self.get_headers())
        return response.json()
    
    def send_template_message(self, to: str, template_name: str, language: str = "en") -> Dict[str, Any]:
        url = f"{self.base_url}/messages"
        payload = {
            "messaging_product": "whatsapp",
            "to": to,
            "type": "template",
            "template": {
                "name": template_name,
                "language": {"code": language}
            }
        }
        
        response = requests.post(url, json=payload, headers=self.get_headers())
        return response.json()

whatsapp_config = WhatsAppConfig()