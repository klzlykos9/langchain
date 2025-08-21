from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model1 = ChatGoogleGenerativeAI(
    model = 'gemini-1.5-flash'
)

llm = HuggingFacePipeline.from_model_id(
    model_id = 'TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    task = 'text-generation',
    pipeline_kwargs=dict(
        temperature = 0.5,
        max_new_tokens = 100
    )
)


model2 = ChatHuggingFace(llm = llm)

prompt1 = PromptTemplate(
    template = 'Generate short and simple notes from the following text \n {text}',
    input_variables = ['text']
)

prompt2 = PromptTemplate(
    template = 'Generate 5 short question answers from the following text \n {text}',
    input_variables = ['text']
)

prompt3 = PromptTemplate(
    template = 'Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables = ['notes', 'quiz']
)

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz' : prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
"""

result = chain.invoke({'text': text})
print(result)

chain.get_graph().print_ascii()