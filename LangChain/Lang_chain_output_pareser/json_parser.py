from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser

load_dotenv()

chat_model = GoogleGenerativeAI(
    model="gemini-3-flash-preview"
)

parser = JsonOutputParser()

template = PromptTemplate(
    template='Give me the name, age and city of a fictional person.\n{format_instructions}',
    input_variables=[],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

prompt=template.format()
res=chat_model.invoke(prompt)
print(res.content)