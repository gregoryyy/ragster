from sentence_transformers import SentenceTransformer
from config import get_config

model = SentenceTransformer(get_config().embed.st_model)

def embed(texts):
    return model.encode(texts)