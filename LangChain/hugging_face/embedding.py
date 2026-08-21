import numpy as np
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpointEmbeddings
import os
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()
token = os.getenv("HF_TOKEN")

embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2", 
    huggingfacehub_api_token=token,
)
documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France",
]
query='which is the capital of india'
vector = embeddings.embed_documents(documents)
query_vector=embeddings.embed_query(query)

similarity =cosine_similarity(vector,[query_vector])
print(similarity)


# print(vector)

