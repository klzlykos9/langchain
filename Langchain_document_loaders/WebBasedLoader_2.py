from langchain_community.document_loaders import WebBaseLoader
import os
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = GoogleGenerativeAI(
    model = 'gemini-2.5-flash'
)

prompt = PromptTemplate(
    template = 'Answer the following question \n {question} from the following text -\n {text}',
    input_variables = ['question', 'text']
)

parser = StrOutputParser()
url = 'https://www.nbphe.org/certified-in-public-health/cph-eligibility-requirements/'
loader = WebBaseLoader(url)


docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({'question': 'get me all job posts available on this website ?', 'text':docs[0].page_content}))