import sys
import os

# Adjust the path to include the directory above the current script's directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.retriever.LangchainRetriever import LangChainRetriever
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

def test_retriever_from_md_file(md_file_path):
    retriever = LangChainRetriever.create_retriever_from_file(md_file_path)
    template = "仅依赖下面的context回答用户的问题:\n{context}\n\nQuestion: {question}\n"
    prompt = ChatPromptTemplate.from_template(template)
    model = ChatOpenAI()
    output_parser = StrOutputParser()

    question_and_context = RunnableParallel(
        {"context": retriever,
         "question": RunnablePassthrough()} 
    )
    chain = question_and_context | prompt | model | output_parser

    question = "Who should I ask for sick leave from?"
    result = chain.invoke(question)
    assert "direct supervisor" in result
    print("✔ Assertion succeeded (MD File Retriever): 'direct supervisor' is in the result")
