from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path = 'Social_Network_Ads (1).csv')

data = loader.load()

print(data[0])

print(len(data))