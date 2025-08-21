from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain.schema.runnable import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatGoogleGenerativeAI(
    model = 'gemini-2.5-flash'
)

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive','negative'] = Field(description = 'Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object= Feedback)

prompt1 = PromptTemplate(
    template = 'Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}',
    input_variables = ['feedback'],
    partial_variables = {'format_instruction':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

# till this i ll get a feedback positive/negative
# 2nd part branch chain using Runnablebranch as it could do if condition


# result = classifier_chain.invoke({'feedback':'This is a wonderful smartphone'}).sentiment

# print(result)

prompt2 = PromptTemplate(
    template = 'Write an appropriate response to this positive feedback in 3 sentence \n {feedback}',
    input_variables = ['feedback']
)

prompt3 = PromptTemplate(
    template = 'Write an appropriate response to this negative feedback in 3 sentence \n{feedback}',
    input_variables = ['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser), # (condition1, chain1),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser), #(condition2, chain2),
    RunnableLambda(lambda x: 'could not find sentiment')     # default
)

# runnblelambda converts lambda to runnable functions 

chain = classifier_chain | branch_chain

Feed = 'This is a worst phone'
print(classifier_chain.invoke({'feedback':Feed }).sentiment)

print(chain.invoke({'feedback': Feed}))

chain.get_graph().print_ascii()