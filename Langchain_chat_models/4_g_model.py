from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence
from dotenv import load_dotenv

load_dotenv()
model = ChatGroq(
    model="deepseek-r1-distill-llama-70b",
    temperature=0,
    max_tokens=None,
    reasoning_format="parsed",  # If supported by the model
)

prompt = PromptTemplate(
    template = 'tell me 5 points on {topic}',
    input_variables = ['topic']
)

parser = StrOutputParser()

chain = RunnableSequence(prompt, model, parser)

print(chain.invoke({'topic':'AI'}))
# messages = [
#    ("system", "You are a helpful assistant that translates English to French."),
#    ("human", "I love programming."),
#  ]
# ai_msg = llm.invoke(messages)
# print(ai_msg.content)
