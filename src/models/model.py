from typing import Optional
from pydantic import BaseModel,EmailStr

class TraineeModel(BaseModel):
  document: str
  firstName:str
  lastName:str
  email:EmailStr
  age:int
  programn:str
  record_number:int

class TraineeUpdateModel(BaseModel):
  firstName: Optional[str] = None
  lastName: Optional[str] = None
  email: Optional[EmailStr] = None
  age: Optional[int] = None
  program: Optional[str] = None
  record_number: Optional[int] = None

