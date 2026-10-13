from pymongo import MongoClient
from pymongo.errors import ConnectionFailure,ServerSelectionTimeoutError
#agregra la URI de conexion a tu base de datos MongoBD

MONGO_URL = "mongodb+srv://juanpablozapatagonsales_db_user:8XY747K70EzLYcVl@clusterapi.ln61rig.mongodb.net/?appName=Taller1_fastAPI"
#crear una instancia de cliente de MongoDB y asignar un tiempo de espera para la seccion del servidor

client = MongoClient(MONGO_URL, serverSelectionTimeoutMS=3000)
#Crear la base de datos y la coleccion
db = client.data_ap
collection = db.trainee

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
