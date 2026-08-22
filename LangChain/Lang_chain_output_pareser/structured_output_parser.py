from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()


# Define the Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=0
)


# Define the output structure
class Facts(BaseModel):
    fact_1: str = Field(description="Fact 1 about the topic")
    fact_2: str = Field(description="Fact 2 about the topic")
    fact_3: str = Field(description="Fact 3 about the topic")


# Tell Gemini to return output according to the Pydantic schema
structured_model = model.with_structured_output(Facts)


# Invoke the model
result = structured_model.invoke(
    "Give 3 facts about black holes."
)

print(result)