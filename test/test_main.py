from pymongo import MongoClient
from pymongo.errors import ConnectionFailure,ServerSelectionTimeoutError

#agregra la URI de conexion a tu base de datos MongoBD
MONGO_URL = "mongodb+srv://juanpablozapatagonsales_db_user:8XY747K70EzLYcVl@clusterapi.ln61rig.mongodb.net/?appName=Taller1_fastAPI"
#crear una instancia de cliente de MongoDB y asignar un tiempo de espera para la seccion del servidor
client = MongoClient(MONGO_URL,ServerSelectionTimeoutMS=3000)
#Crear la base de datos y la coleccion
db = client.Ambiente703
collection = db.Mesas

#crear el modelo de datos para la coleccion
nueva_mesa = {
  "name":"Juan pablo",
  "status":"alive",
  "species":"human",
  "gender":"male",
}

#insertar el modelo de datos en la coleccion
collection.insert_one(nueva_mesa)
print("Documento insertado en la coleccion 'Mesas' de la base de datos 'Ambiente703' exitosamente.")

try:
  #intentar obtener informacion del servidor para verificar la conexion
  client.server_info()
  client.admin.command("ping")
  print("conexion exitosa con MongoDB")
except (ConnectionFailure,ServerSelectionTimeoutError) as e:
  print(f"error al conectar a MongoDB : {e}")
finally:
  #cerrar la conexion al cliente MongoDB
  client.close()
