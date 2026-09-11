from ..LLMInterface import LLMInterface
from ..LLMEnums import CoHereEnum, DocumentTypeEnum
import cohere
import logging


class CoHereProvider(LLMInterface):
    def __init__(self, api_key: str,        
                default_input_max_characters: int=1000,
                default_generation_max_output_tokens: int=1000,
                default_generation_temperature: float=0.1):
        
        self.api_key = api_key
        
        self.default_input_max_characters = default_input_max_characters
        self.default_generation_max_output_tokens = default_generation_max_output_tokens
        self.default_generation_temperature = default_generation_temperature
        
        self.generation_model_id = None
        
        self.embedding_model_id = None
        self.embedding_size = None
        
        
        self.client = cohere.Client(api_key = self.api_key)
        
        self.logger = logging.getLogger(__name__)
        
        
    def set_generation_model(self, model_id: str):  # we made this func instead of add it to __init__ so if the application in the runtime and we need to change generation model
            self.generation_model_id = model_id
            
            
    def set_embedding_model(self, model_id: str, embedding_size: int):
            self.embedding_model_id = model_id
            self.embedding_size = embedding_size
            
    def process_text(self, text: str):     # Didn't add to the interface since some provider could use it while others not, it is a helper method used by the other functions 
        return text[:self.default_input_max_characters].strip()
    
    
    def generate_text(self, promote: str, chat_history: list=[] , max_output_tokens: int=None , temperature: float = None):
        
        if not self.client:
            self.logger.error("CoHere client was not set") 
            return None   
        
        if not self.generation_model_id:
            self.logger.error("Generation model for CoHere was not set")
            return None
        
        response = self.client.chat(
            model = self.generation_model_id,
            chat_history = chat_history,
            message = self.process_text(promote), 
            temperature = temperature,
            max_tokens = max_output_tokens,       
        )
        
        if not response or not response.text:
            self.logger.error("Error while generating text with CoHere")
            return None
        
        return response.text
    
    
    def construct_promote(self, prompt: str, role: str):
        return {
            "role": role,
            "text": self.process_text(prompt),
        }


    def embed_text(self, text: str, document_type: str = None): 
        if not self.client:
            self.logger.error("CoHere client was not set") 
            return None   
        
        if not self.generation_model_id:
            self.logger.error("Embeddig model for CoHere was not set")
            return None   
        
        input_type = CoHereEnum.DOCUMENT
        if document_type == DocumentTypeEnum.QUERY:
            input_type = CoHereEnum.QUERY
            
        response = self.client.embed(
            model = self.embedding_model_id,
            texts = [text],
            input_type = input_type,
            embedding_types = ["float"],
        )
        
        
        if not response or response.embeddings or not response.embeddings.float  :
            self.logger.error("Error while embedding text with CoHere")
            return None
        
        return response.embeddings.float[0]
    