from langchain_community.document_loaders import TextLoader

loader = TextLoader('/teamspace/studios/this_studio/Langchain_document_loaders/cricket.txt', encoding = 'utf-8')

docs = loader.load()

print(docs)


print(len(docs))

print(type(docs[0])) 

print(docs[0].page_content)

print(docs[0].metadata)

print('--------------------------------')

print(docs[0])


