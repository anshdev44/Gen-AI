from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

# Fixed typo: 'temparature' -> 'temperature'
model = ChatGoogleGenerativeAI(model="gemini-3.7-flash", temperature=0.7)

# Fixed typos in Literal values ("Postive"/"Nagative" -> "Positive"/"Negative")
class Feedback(BaseModel):
    sentiment: Literal["Positive", "Negative"] = Field(
        description="Based on the Input classify the following text into a positive or a negative Review"
    )

parser1 = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Feedback)

# Fixed syntax: Changed square brackets [] to curly braces {} for the partial_variables dictionary
prompt1 = PromptTemplate(
    template="Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={"format_instruction": parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template='Write a response to the following positive feedback given by the user in under 3 lines:\n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write a response to the following negative feedback given by the user in under 3 lines:\n {feedback}',
    input_variables=['feedback']
)

# Fixed string matching: Lambda now checks for exact capitalization ("Positive" and "Negative")
# Note: RunnableBranch passes the dictionary input down, so we wrap prompt2/prompt3 
# in a lambda or a dictionary mapper to match their expected input key '{feedback}'
branch_chain = RunnableBranch(
    (lambda x: x.sentiment == 'Positive', lambda x: {'feedback': text_input} | prompt2 | model | parser1),
    (lambda x: x.sentiment == 'Negative', lambda x: {'feedback': text_input} | prompt3 | model | parser1),
    RunnableLambda(lambda x: "could not find sentiment")
)

# We store the raw text in a variable so the branching steps can reference it safely
text_input = (
    "The interface redesign is an absolute masterpiece of modern art, provided you enjoy wandering through a "
    "labyrinth just to find the log-out button. I really want to commend the engineering team for making the "
    "app so secure that even I, the account holder, cannot log in half the time. On the bright side, when the "
    "app isn't crashing every five minutes, the dark mode looks quite slick. It's truly impressive how a company "
    "can hire such incredibly polite and friendly support staff who are simultaneously completely incapable of "
    "resolving a single technical issue. I wouldn't say I hate it, but I certainly wouldn't recommend it to anyone "
    "I actually like."
)

final_chain = classifier_chain | branch_chain

# Fixed input key: Changed 'text' to 'feedback' to match prompt1
result = final_chain.invoke({'feedback': text_input})
print(result)
