from llm import ask_llm

context = """
Ashok Reddy

Skills:
Python
SQL
Machine Learning
TensorFlow
Pandas

Projects:
Stroke Risk Prediction
Taxi Fare Prediction
"""

question = "What are Ashok Reddy's skills?"

answer = ask_llm(question, context)

print(answer)