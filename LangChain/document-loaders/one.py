from langchain_community.document_loaders import PyPDFLoader


loader=PyPDFLoader(
    file_path='./file.pdf'
    
)

docs=loader.load()

for i in range(len(docs)):
    print('Metadata: ',docs[i].metadata,'\n')
    print('Page content',docs[i].page_content,'\n')