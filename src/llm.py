import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

llm = ChatOpenAI(
    model="tencent/hy3:free",
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    temperature=0
)

def ask_llm(question, context):
    prompt = f"""
You are an AI Resume Assistant.

Use ONLY the resume information below.

Resume:
{context}

Question:
{question}

If the answer is not present in the resume, say:
"I couldn't find that information in the provided resumes."

Answer:
"""

    response = llm.invoke(prompt)
    return response.content