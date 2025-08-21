from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os


load_dotenv()
google_api_key = os.getenv('GOOGLE_API_KEY')
prompt = PromptTemplate(
    template = 'Generate 5 interesting facts about {topic}',
    input_variables = ['topic']
)

model = ChatGoogleGenerativeAI(
    model = "gemini-1.5-flash",
    google_api_key = google_api_key
)

parser = StrOutputParser()

chain = prompt | model | parser

Result = chain.invoke({'topic':'how earth is been made'})

print(Result)

chain.get_graph().print_ascii()
