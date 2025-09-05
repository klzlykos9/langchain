from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
CORS(app)

# Model
model = GoogleGenerativeAI(model="gemini-2.5-flash")
parser = StrOutputParser()

# Prompts
page_prompt = PromptTemplate(
    template="You are KLZ, an AI that answers questions based on a webpage.\n\nQuestion: {question}\n\nWebpage text:\n{text}\n\nAnswer only from this webpage content.",
    input_variables=["question", "text"]
)

chat_prompt = PromptTemplate(
    template="You are KLZ, a helpful AI assistant. Answer conversationally:\n{question}",
    input_variables=["question"]
)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question", "").strip()
    url = data.get("url", "").strip()

    try:
        # If the user explicitly refers to "this page / product / site"
        if url and any(keyword in question.lower() for keyword in ["this", "page", "site", "product", "laptop"]):
            loader = WebBaseLoader(url)
            docs = loader.load()
            chain = page_prompt | model | parser
            answer = chain.invoke({"question": question, "text": docs[0].page_content})
        else:
            chain = chat_prompt | model | parser
            answer = chain.invoke({"question": question})

        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"answer": f"⚠️ Error: {str(e)}"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
