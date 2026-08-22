from typing import TypedDict,Literal,Annotated 
from langchain_google_genai import ChatGoogleGenerativeAI 
from dotenv import load_dotenv 

load_dotenv() 

model = ChatGoogleGenerativeAI(model='gemini-3.7-flash') 

class reviews(TypedDict): 
    review: Annotated[str,'the overall review of the review not including the ratings and other stuff'] 
    rating: Annotated[int,'if rating not given assign a genral rating from yourslef between 1 to 5']
    sentiment:Annotated[str,'what ois the overall sentiment']
    name:Annotated[str,'if expilictly mentioned the name of the user']
    statuscode:Literal[200,404]
strutured_output = model.with_structured_output(reviews) 

result = strutured_output.invoke(
    'the Hardware os Great but the software is dog shit like what is the fuck is this ui i dont like this kid of ui will only rate 2 stars always shows 404 error by ansh ahuja'
) 

print(result)
print(type(result))
print(result['name'])
