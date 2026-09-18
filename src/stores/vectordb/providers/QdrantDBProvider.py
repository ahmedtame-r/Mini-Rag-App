from qdrant_client import QdrantClient, models
from ..VectorDBInterface import VectorDBInterface
from ..VectorDBEnums import DistanceMethodEnums
import logging
from typing import List


class QdrantDB(VectorDBInterface):
    def __init__(self, db_path: str, distance_method: str):
        self.client = None
        self.db_path = db_path
        self.distance_method = None
        
        if distance_method == DistanceMethodEnums.COSINE.value:
            self.distance_method = models.Distance.COSINE
        
        elif distance_method == DistanceMethodEnums.DOT.value:
            self.distance_method = models.Distance.DOT
            
        self.logger = logging.getLogger(__name__)
        
    def connect(self):
        self.client = QdrantClient(path = self.db_path)
        
    
    def disconnect(self):
        self.client = None
        
    
    def is_collection_existed(self, collection_name):
        return self.client.collection_exists(collection_name="{collection_name}")
    
    
    def list_all_collections(self) -> List:
        return self.client.get_collections()
    
    
    def get_collection_info(self, collection_nam):
        return self.client.get_collection(collection_nam=collection_nam)


    def delete_collection(self, collection_name):
        if self.is_collection_existed(collection_name=collection_name):
            return self.client.delete_collectio()
        
    def create_collection(self, collection_name, embedding_size, do_reset = False):
        if do_reset:
            _ = self.delete_collection(collection_name=collection_name)
            
        if not self.is_collection_existed(collection_name=collection_name):
            self.client.create_collection(
                collection_name=collection_name,
                vectors_config = models.VectorParams(
                    size=embedding_size,
                    distance=self.distance_method,
                )
            )
            
    
    def insert_one(
        self,
        collection_name: str,
        text: str, 
        vector: list,
        metadata: dict = None,
        record_id: list = None,
    ):
        if not self.is_collection_existed(collection_name=collection_name):
            self.logger.error(f"Can't insert new record to non-existed collection: {collection_name}")
            return False
        try:
            _ = self.client.upload_record(
                collection_name = collection_name,
                records = [
                    models.Record(
                        vector = vector,
                        payload = {
                            "text" : text, "metadata": metadata
                        }
                    )
                ]
            )
        except Exception as e:
            self.logger.error(f"error while inserting batch: {e}")
            return False
        
        return True
    
    
    def insert_many(self, collection_name, texts, vectors, metadata = None, record_ids = None, batch_size = 50):
        if metadata is None:
            metadata = [None] * len(texts)
            
        if record_ids is None:
            record_ids = [None] * len(texts)
            
        for i in range(0, len(texts), batch_size):
            batch_end = i + batch_size
            
            batch_texts = texts[i:batch_end]
            batch_vectors = vectors[i:batch_end]
            batch_metadata = vectors[i:batch_end]
            
            batch_records = [
                models.Record(
                    vector = batch_vectors,
                    payload = {
                        "text" : batch_texts, "metadata": batch_metadata,
                    }
                )
                
                for x in range(len(batch_texts))
            ]
            
        try:
            _ = self.client.upload_records(
                collection_name = collection_name,
                records = batch_records
            )
        
        except Exception as e:
            self.logger.error(f"Error while insert batch: {e}")
            return False
        
        return True
    
    
    def search_by_vector(self, collection_name, vector, limit):
        return self.clients.search(
            collection_name = collection_name,
            query_vector = vector,
            limit = limit,
        )