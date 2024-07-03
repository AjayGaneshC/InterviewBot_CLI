import os
from langchain.llms import Ollama
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = Ollama(base_url="https://e16fe50d656f1.notebooksg.jarvislabs.net/",model="llama2")  # or any other model you have in Ollama

questions = [
    "Can you tell me about your background in software development and any significant projects you've worked on?",
    "What programming languages are you most proficient in, and how have you applied them in your work?",
    "Describe a challenging technical problem you've faced and how you solved it.",
    "How do you stay updated with the latest trends and technologies in software development?",
    "Can you explain your experience with version control systems and your preferred workflow?"
]

interviewer_template = PromptTemplate(
    input_variables=["question", "answer"],
    template="""
    You are an experienced HR professional conducting a job interview for a software developer position.
    The candidate has just answered the following question:

    Question: {question}
    Candidate's Answer: {answer}

    Please provide a brief evaluation of the candidate's response (2-3 sentences) and ask the next relevant question.
    If this was the last question, provide a summary of the candidate's overall performance, including strengths and areas for improvement.

    Your response:
    """
)

interviewer_chain = LLMChain(llm=llm, prompt=interviewer_template)

def conduct_interview():
    print("Welcome to the software developer job interview. Please answer the following questions:")
    
    for i, question in enumerate(questions):
        print(f"\nQuestion {i+1}: {question}")
        answer = input("Your answer: ")
        
        if i < len(questions) - 1:
            response = interviewer_chain.run(question=question, answer=answer)
            print(f"\nInterviewer: {response}")
        else:
            response = interviewer_chain.run(question=question, answer=answer)
            print(f"\nInterview Summary:\n{response}")

if __name__ == "__main__":
    conduct_interview()
