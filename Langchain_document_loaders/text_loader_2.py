from langchain_community.document_loaders import TextLoader
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableLambda

load_dotenv()

model = GoogleGenerativeAI(
    model= 'gemini-2.5-flash'
)

prompt = PromptTemplate(
    template = 'Write a summary for the following poem - \n {poem}',
    input_variables = ['poem']
)

parser = StrOutputParser()

loader = TextLoader('cricket.txt', encoding = 'utf-8')

docs = loader.load()
docs1 =  RunnableLambda(lambda x:{docs[0].page_content})
chain = docs1 | prompt | model | parser

# print(chain.invoke({'poem': docs[0].page_content}))

print(chain.invoke({}))