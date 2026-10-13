from bson import ObjectId
from src.models.database import collection
from src.models.models import traineeModel,traineeUpdateModel

def helper_trainee(trainee)-> dict:
  return {
    "id": str(trainee["_id"]),
    "document": trainee["document"],
    "firstName": trainee["firstName"],
    "lastName": trainee["lastName"],
    "email": trainee["email"],
    "age": trainee["age"],
    "programn": trainee["programn"],
    "record_number": trainee["record_number"]
  }


