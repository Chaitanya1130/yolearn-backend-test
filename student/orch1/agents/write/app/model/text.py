
from pydantic import BaseModel
from typing import List

class TextInput(BaseModel):
    text:str
class TextOutput(BaseModel):
    id:str=None
    reviewedtext:str
    storedtext:str