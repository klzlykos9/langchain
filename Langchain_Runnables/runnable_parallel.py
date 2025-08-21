from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain.schema.runnable import RunnableSequence, RunnableParallel
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

load_dotenv()

prompt1 = PromptTemplate(
    template = 'Generate a tweet about {topic}',
    input_variables = ['topic']
)


prompt2 = PromptTemplate(
    template = 'Generatea Linkedin post about {topic}',
    input_variables = ['topic']
)

model1 = GoogleGenerativeAI(
    model = 'gemini-2.5-flash'
)

llm = HuggingFacePipeline.from_model_id(
    model_id = 'TinyLlama/TinyLlama-1.1B-Chat-V1.0',
    task = 'text-generation',
    pipeline_kwargs = dict(
        temperature = 0.5,
        max_new_tokens = None
    )
)

model2 = ChatHuggingFace(llm = llm)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model1, parser),
    'linkedin': RunnableSequence(prompt2, model2, parser)
})

# it ll give me a dictionary

result = parallel_chain.invoke({'topic':'AI'})

# print(result)
print(result['tweet'])

print('----------------------------------/n')

print(result['linkedin'])