from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path = 'books',
    glob = '*.pdf',
    loader_cls = PyPDFLoader
)

# docs = loader.load()

# print(len(docs))

# to see first pdfs first page

# print(docs[3].page_content)
# print(docs[0].metadata)



# print('--------------------------')


# for document in docs :
#    print(document.metadata)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)