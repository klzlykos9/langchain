from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('/teamspace/studios/this_studio/dl-curriculum.pdf')

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size = 100,
    chunk_overlap = 0,
    separator = ''
)

result = splitter.split_documents(docs)   # to split document objects

print(result)

print('-------------')

print(result[0])    # to see the first chunks

print('----------------')

print(result[0].page_content)