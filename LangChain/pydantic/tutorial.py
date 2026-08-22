from pydantic import BaseModel, EmailStr, Field
from typing import Optional, Literal

class Person(BaseModel):
    name: str = "Ansh"
    age: Optional[int] = None
    job: Literal["yes", "no"]
    email: EmailStr
    # 1. Changed "Cgpa" to lowercase "cgpa" to follow Python standards
    cgpa: float = Field(gt=0, lt=10,description='given cgpa in indian standards')

# 2. The dictionary key "cgpa" now matches the class field exactly
data = {
    "age": "20", 
    "job": "no", 
    "email": "abs@gmail.com",
    "cgpa": 7
}

# 3. Unpack and create the object
ansh = Person(**data)

print(ansh)
