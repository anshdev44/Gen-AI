from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,JsonOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch,RunnableSequence

load_dotenv()

llm=ChatGoogleGenerativeAI(
    model='gemini-3-flash-preview',
    temperature=0.7
)

prompt1=PromptTemplate(
    template='genrate a complicate humored joke i english can be really dark around the topic-> {topic} under 3 lines',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template='explain the joke ->{joke} and return joke and explaination in a good format and return in Json format and also the explain in apra not more than 5 lines',
    input_variables=['joke']
)

parser=StrOutputParser()
parser1=JsonOutputParser()

chain=RunnableSequence(prompt1,llm,parser,prompt2,llm,parser1)

result=(chain.invoke({'topic':'sex'}))

print(result['joke'])

