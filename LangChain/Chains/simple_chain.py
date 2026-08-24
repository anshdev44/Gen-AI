from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


# Define the Gemini model
model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", temperature=1.5)

template = PromptTemplate(
    template="Write 5 lines about a handsome and young boy named {Name}",
    input_variables=["Name"],
)

parser = StrOutputParser()

#geives you a overall thing of the chaon like a simple graph on it
chain = template | model | parser
result = chain.invoke({"Name": "Ansh Ahuja"})
chain.get_graph().print_ascii()
print(result)