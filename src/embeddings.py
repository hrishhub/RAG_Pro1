from sentence_transformers import SentenceTransformer

class EmbeddingModel:
    def __init__(self , model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        
    def embed_text(self,text):
        return self.model.encode(text)
    
    def embed_documents(self,documents):
        return self.model.encode(documents)
    
    