from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

chat_model = GoogleGenerativeAI(model="gemini-3-flash-preview")

template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

parser = StrOutputParser()


# Create a sequential pipeline where the output of each component is automatically passed as input to the next component
chain = template1 | chat_model | parser | template2 | chat_model | parser

result = chain.invoke({'topic':'black hole'})

print(result)

