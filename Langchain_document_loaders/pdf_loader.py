from langchain_community.document_loaders import PyPDFLoader   # need to install PyPDF


loader = PyPDFLoader('dl-curriculum.pdf')

docs = loader.load()

print(docs)

print(len(docs))

print('-------------------------')
print(docs[0].page_content)

print('-----------------------')

print(docs[0].metadata)