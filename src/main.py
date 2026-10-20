from src.templates.controllers import create_trainee,get_all_trainees,get_trainee_by_id,update_trainee,delete_trainee

from src.models.model import TraineeModel,TraineeUpdateModel
from fastapi import FastAPI ,HTTPException, status

app = FastAPI(
    title="Gestion de datos de aprendices",
    description="Api simple para la gestion de datos de aprendices",
    version="1.0.0"
)
#mesaje de bienvenida
@app.get("/")
async def root():
    return{"message":"Hello Word"}
#Regsitrar aprendices
@app.post(
    "/trainee/", response_description="registrar un nuevo aprendiz",
    status_code=status.HTTP_201_CREATED,
)

def api_create_trainee(trainee:TraineeModel):
    #validar si ya existe el documento
    return create_trainee(trainee)

#Obtener la lista de aprendices
@app.get(
    "/trainee/", response_description="listar todos los aprendices"
)
def get_all_trainees_api():
    return get_all_trainees(
    )

#Obtener un aprendiz por su ID
@app.get(
    "/trainee/{id}", response_description="Obtener un aprendiz por su id"
)
def get_trainee_by_id_api():
    trainee = get_trainee_by_id(id)
    if not trainee: 
        raise HTTPException(status_code=404,detail="Aprendiz no encontrado")
    return trainee

#Actualizar datos de un aprendiz por su id
@app.put(
   "/trainee/{id}", response_description="actualizar datos de  un aprendiz por su id" 
)

def update_trainee_api(id:str, trainee: TraineeUpdateModel):
    trainee = update_trainee(id, trainee)
    if not trainee:
        raise HTTPException(
            status_code=404, detail="Aprendiz no encontrado o sin datos a actualizar",
        )
#Eliminar una aprendiz
@app.delete(
    "/trainee/{id}", response_description="Eliminar un aprendiz"
)

def delete_trainee_api(id: str):
    trainee = delete_trainee(id)
    if not trainee:
        raise HTTPException(
            status_code=404, detail="Aprendiz no encontrado"
        )
    return{"mensaje": "Aprendiz eliminado"}    