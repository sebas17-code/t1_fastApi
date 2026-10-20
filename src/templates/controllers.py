from bson import ObjectId
from bson.errors import InvalidId
from src.models.database import collection
from src.models.model import TraineeModel, TraineeUpdateModel


def helper_trainee(trainee) -> dict:
    return {
        "id": str(trainee["_id"]),
        "document": trainee.get("document"),
        "firstName": trainee.get("firstName"),
        "lastName": trainee.get("lastName"),
        "email": trainee.get("email"),
        "age": trainee.get("age"),
        "programn": trainee.get("programn"),  # Revisa si debería ser "program"
        "record_number": trainee.get("record_number"),
    }


def create_trainee(trainee: TraineeModel) -> dict:
    trainee_dict = trainee.model_dump()
    result = collection.insert_one(trainee_dict)
    new_trainee = collection.find_one({"_id": result.inserted_id})
    return helper_trainee(new_trainee)


def get_all_trainees() -> list:
    trainees = []
    for trainee in collection.find():
        trainees.append(helper_trainee(trainee))
    return trainees


def get_trainee_by_id(id: str):
    try:
        trainee = collection.find_one({"_id": ObjectId(id)})
        if trainee:
            return helper_trainee(trainee)
    except InvalidId:
        return None
    return None


def update_trainee(id: str, data: TraineeUpdateModel):
    try:
        data_update = {
            k: v for k, v in data.model_dump().items() if v is not None
        }
        if data_update:
            collection.update_one({"_id": ObjectId(id)}, {"$set": data_update})

        trainee_updated = collection.find_one({"_id": ObjectId(id)})
        if trainee_updated:
            return helper_trainee(trainee_updated)
    except InvalidId:
        return None
    return None


def delete_trainee(id: str) -> bool:
    try:
        trainee = collection.find_one({"_id": ObjectId(id)})
        if trainee:
            collection.delete_one({"_id": ObjectId(id)})
            return True
    except InvalidId:
        return False
    return False