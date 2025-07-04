import openai
from typing import Dict, Any, List
from config.settings import settings

class AIModelConfig:
    def __init__(self):
        openai.api_key = settings.openai_api_key
        self.default_model = "gpt-3.5-turbo"
        self.health_assessment_model = "gpt-4"
        
    def get_chat_completion(self, messages: List[Dict[str, str]], model: str = None) -> str:
        if not model:
            model = self.default_model
            
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=messages,
                max_tokens=500,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"
    
    def get_health_assessment_prompt(self) -> str:
        return """
        You are a health concierge assistant for a wellness clinic. 
        Your role is to:
        1. Conduct initial health assessments
        2. Qualify leads based on their needs
        3. Recommend appropriate treatments
        4. Schedule appointments
        
        Be professional, empathetic, and informative.
        Always ask relevant follow-up questions to better understand the client's needs.
        """
    
    def get_content_personalization_prompt(self, user_profile: Dict[str, Any]) -> str:
        return f"""
        Create personalized wellness content for a user with the following profile:
        - Age: {user_profile.get('age', 'Not specified')}
        - Health concerns: {user_profile.get('health_concerns', 'General wellness')}
        - Treatment interests: {user_profile.get('treatment_interests', 'Not specified')}
        - Language preference: {user_profile.get('language', 'English')}
        
        Provide relevant, actionable wellness advice.
        """

ai_config = AIModelConfig()