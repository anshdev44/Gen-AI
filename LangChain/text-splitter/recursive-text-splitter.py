from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

text = """
LangChain is a framework designed to help developers build applications powered by large language models. It provides several useful components such as prompt templates, output parsers, document loaders, text splitters, embeddings, retrievers, and vector stores. These components can be connected together to create powerful applications such as question-answering systems and retrieval augmented generation applications. In a RAG system, documents are first loaded and divided into smaller chunks. These chunks are then converted into numerical representations called embeddings and stored in a vector database. When a user asks a question, the system searches the vector database for chunks that are semantically similar to the question. The retrieved chunks are then provided to the language model as context so that it can generate a more accurate and relevant answer.
"""

# loader=PyPDFLoader(
#     file_path='./file.pdf'
# )

splitter=RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=0
)

# dock=loader.load()

chunks=splitter.split_text(text)

for i,chunk in enumerate(chunks):
    print("chunk number->",i)
    print(chunk)