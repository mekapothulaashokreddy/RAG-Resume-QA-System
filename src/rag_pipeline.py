from retriever import search_resume
from llm import ask_llm


def get_answer(question):

    results = search_resume(question)

    documents = results["documents"][0]

    context = "\n\n".join(documents)

    answer = ask_llm(question, context)

    return answer


if __name__ == "__main__":

    while True:

        question = input("\nAsk your question (type 'exit' to quit): ")

        if question.lower() == "exit":
            break

        answer = get_answer(question)

        print("\nAnswer:\n")
        print(answer)