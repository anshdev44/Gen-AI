from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

from langchain_core.runnables import (
    RunnableParallel,
    RunnableBranch,
    RunnableSequence,
    RunnablePassthrough,
    RunnableLambda,
)

load_dotenv()


def word_counter(text):
    return len(text.split())


llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")
parser=StrOutputParser()

prompt1 = PromptTemplate(
    template="Write a one liner joke on the topic {topic} which has dark humour",
    input_variables=["topic"],
)

chain = prompt1 | llm | parser

final_chain=chain | RunnableLambda(word_counter)
print(final_chain.invoke({"topic": "cricket"}))