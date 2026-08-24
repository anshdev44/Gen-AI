from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

# 1. Initialize models
model1 = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.7)
model2 = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=0.7)

# 2. Define the initial prompts
Prompt1 = PromptTemplate(
    template="Write Notes on the topic {Topic}", input_variables=["Topic"]
)

Prompt2 = PromptTemplate(
    template="Write 5 question and answers on the {Topic}", input_variables=["Topic"]
)

# 3. New Prompt: Changed {Q/A} to {qa} to fix the formatting error
Prompt3 = PromptTemplate(
    template="""
    Here are study notes on a topic:
    {notes}
    
    Here are quiz questions on that same topic:
    {qa}
    
    Please combine these into a beautifully formatted study guide with an executive summary at the top.
    """,
    input_variables=["notes", "qa"]
)

parser = StrOutputParser()

# 4. Create the parallel step using 'qa' instead of 'Q/A'
parallel_chain = RunnableParallel({
    'notes': Prompt1 | model1 | parser,
    'qa': Prompt2 | model2 | parser
})

# 5. Combine everything into one single, clean pipeline
final_chain = parallel_chain | Prompt3 | model1 | parser

# 6. Run the chain
result = final_chain.invoke({'Topic': 'Black Holes'})

print(result)
