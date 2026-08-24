from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv

from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import (
    StrOutputParser,
    JsonOutputParser,
    PydanticOutputParser,
)

from langchain_core.runnables import (
    RunnableParallel,
    RunnableBranch,
    RunnableSequence,
    RunnablePassthrough,
    RunnableLambda,
)

from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)


class Feedback(BaseModel):
    sentiment: Literal["Pos", "Neg"] = Field(
        description="Based on the user feedback, classify it as positive or negative"
    )


# Converts LLM output into a Feedback Pydantic object
parser = PydanticOutputParser(pydantic_object=Feedback)

# Used to get normal text from the final LLM response
parser2 = StrOutputParser()


prompt1 = PromptTemplate(
    template="""
Classify the following feedback as positive or negative.

Feedback: {feedback}

{format_instructions}
""",
    input_variables=["feedback"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)


prompt2 = PromptTemplate(
    template="""
The user gave positive feedback.

Write a short and friendly response to this feedback:

{feedback}
""",
    input_variables=["feedback"]
)


prompt3 = PromptTemplate(
    template="""
The user gave negative feedback.

Write a short and polite response acknowledging their concern:

{feedback}
""",
    input_variables=["feedback"]
)


# Decide which chain to execute based on sentiment
branch_chain = RunnableBranch(
    (
        lambda x: x.sentiment == "Pos",
        RunnableSequence(prompt2, llm, parser2)
    ),
    (
        lambda x: x.sentiment == "Neg",
        RunnableSequence(prompt3, llm, parser2)
    ),
    RunnablePassthrough()
)


# First classify the feedback, then send it to the appropriate branch
complete_chain = RunnableSequence(
    prompt1,
    llm,
    parser,
    branch_chain
)


print(
    complete_chain.invoke(
        {
            "feedback": "I really loved the product. It is very easy to use!"
        }
    )
)