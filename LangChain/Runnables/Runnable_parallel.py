from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.runnables import (
    RunnableParallel,
    RunnableBranch,
    RunnableSequence,
    RunnableParallel,
)

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.7)

prompt1 = PromptTemplate(
    template="Genrate a reddit Post on {topic}", input_variables=["topic"]
)

promtp2 = PromptTemplate(
    template="Genrate a Instagram Post on {topic}", input_variables=["topic"]
)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {
        "reddit": RunnableSequence(prompt1, llm, parser),
        "instagram": RunnableSequence(promtp2, llm, parser),
    }
)

result=parallel_chain.invoke({'topic':'Ai'})

print(result['reddit'])
print(result['instagram'])

