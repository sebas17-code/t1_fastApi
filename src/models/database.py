import certifi
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, ServerSelectionTimeoutError

# URI de conexión a tu base de datos MongoDB Atlas
MONGO_URL = "mongodb+srv://sebastianmonsalve800_db_user:sebas17@cluster0.abqox6t.mongodb.net/"

# Crear la instancia del cliente con certifi para evitar errores de SSL/TLS
client = MongoClient(
    MONGO_URL,
    serverSelectionTimeoutMS=3000,
    tlsCAFile=certifi.where()  # <-- Agregado para solucionar el error de SSL
)

# Crear/seleccionar la base de datos y la colección
db = client.data_ap
collection = db.trainee

# Probar la conexión al arrancar el servidor
try:
    client.admin.command("ping")
    print("conexion exitosa con MongoDB")
except (ConnectionFailure, ServerSelectionTimeoutError) as e:
    print(f"error al conectar a MongoDB : {e}")