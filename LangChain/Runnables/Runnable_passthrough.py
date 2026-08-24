from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser

from langchain_core.runnables import (
    RunnableParallel,
    RunnableBranch,
    RunnableSequence,
    RunnablePassthrough
)

load_dotenv()

parser = StrOutputParser()  # Converts LLM output into a normal string

llm = ChatGoogleGenerativeAI(
    model='gemini-3.5-flash-lite',
    temperature=0.8
)


prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

joke_gen_chain = RunnableSequence(prompt1, llm, parser)  # Generate the joke step-by-step

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),  # Keep the original joke unchanged
    'explanation': RunnableSequence(prompt2, llm, parser)  # Explain the same joke
})

final_chain = RunnableSequence(joke_gen_chain, parallel_chain)  # Generate joke, then process it in parallel

print(final_chain.invoke({'topic': 'cricket'}))  # Run the complete chain