from abc import ABC, abstractmethod


# this interface used to write the design of class without any implementation / logic
class LLMInterface(ABC):
    
    @abstractmethod  # used to define the func as a must implemented func
    def set_generation_model(self, model_id: str):
        pass
    
    @abstractmethod
    def set_embedding_model(self, model_id: str, embedding_size: int):
        pass
    
    @abstractmethod
    def generate_text(self, promote: str, chat_history: list=[] , max_output_tokens: int=None , temperature: float = None):
        pass
    
    @abstractmethod
    def embed_text(self, text: str, document_type: str = None): 
        pass
    
    @abstractmethod
    def construct_promote(self, prompt: str, role: str):
        pass
    
    
        
