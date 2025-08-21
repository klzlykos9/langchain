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
url = 'https://www.amazon.in/HP-Laptop-15-6-inch-Graphics-fc0154AU/dp/B0D3HG5CMG/ref=sr_1_3?adgrpid=94221362531&ext_vrnc=hi&hvadid=590450674960&hvdev=c&hvlocphy=9300861&hvnetw=g&hvqmt=e&hvrand=7784002373648542449&hvtargid=kwd-353766051967&hydadcr=16601_2163995&mcid=1c11e2187bb238fb8c38026e68aa3fa6&sr=8-3'

loader = WebBaseLoader(url)


docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({'question': 'no os usb 2.0 ports ?', 'text':docs[0].page_content}))