from src.retriever.LangchainRetriever import LangChainRetriever
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

def test_runnable_from_md_file(md_file_path):
    question_and_context = LangChainRetriever.create_runnable_from_file(md_file_path)
    prompt = ChatPromptTemplate.from_template("仅依赖下面的context回答用户的问题:\n{context}\n\nQuestion: {question}\n")
    model = ChatOpenAI()
    output_parser = StrOutputParser()

    chain = question_and_context | prompt | model | output_parser

    question = "Who should I ask for sick leave from?"
    result = chain.invoke(question)
    assert "direct supervisor" in result
    print("✔ Assertion succeeded (MD File Runnable): 'direct supervisor' is in the result")
