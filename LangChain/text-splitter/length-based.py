from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

print("1. Program started")

loader = PyPDFLoader("./file.pdf")

print("2. Loader created")

docs = loader.load()

print("3. PDF loaded")
print("Number of documents:", len(docs))

text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=100,
    chunk_overlap=0
)

print("4. Splitter created")

chunks = text_splitter.split_documents(docs)

print("5. Documents split")
print("Number of chunks:", len(chunks))

for chunk in chunks:
    print("Length:", len(chunk.page_content))
    print("Text:", chunk.page_content)
    print("-" * 50)