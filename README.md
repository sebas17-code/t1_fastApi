# API de Gestión de Aprendices

Proyecto desarrollado en Python para registrar y administrar aprendices mediante una API REST. Los datos se almacenan en MongoDB Atlas y la API se despliega en Render. Incluye un menú de consola para consumir la API.

## Herramientas utilizadas

- **Python:** lenguaje de programación.
- **FastAPI:** creación de la API REST y sus rutas.
- **Uvicorn:** servidor para ejecutar la aplicación FastAPI.
- **MongoDB Atlas:** base de datos en la nube.
- **PyMongo:** conexión y operaciones con MongoDB.
- **Pydantic:** validación de los datos de entrada.
- **email-validator:** validación de correos electrónicos mediante `EmailStr`.
- **Requests:** envío de solicitudes HTTP desde el menú de consola hacia la API.
- **Certifi:** certificados de confianza para la conexión TLS.
- **GitHub:** almacenamiento y control de versiones del código.
- **Render:** despliegue de la API en Internet.

## Funcionalidades

- Registrar aprendices.
- Consultar todos los aprendices.
- Consultar un aprendiz por su ID.
- Actualizar los datos de un aprendiz.
- Eliminar un aprendiz.
- Ejecutar las operaciones desde un menú de consola que consume la API.

## Estructura del proyecto

```text
t1_fastAPI/
├── .venv/                      # Entorno virtual
├── data/                       # Datos locales
├── src/
│   ├── main.py                 # Rutas y configuración de FastAPI
│   ├── models/
│   │   ├── database.py         # Conexión con MongoDB Atlas
│   │   └── model.py            # Modelos y validación de datos
│   ├── templates/
│   │   └── controllers.py      # Operaciones CRUD
│   └── views/
│       └── view.py             # Menú de consola para consumir la API
├── test/
│   └── test_main.py            # Pruebas unitarias
├── .env                        # Variables de entorno
├── .gitignore                  # Archivos ignorados por Git
├── requirements.txt            # Dependencias del proyecto
└── structure.sh                # Script de estructura
``` 

## Instalación y ejecución local

1. Clonar el repositorio y entrar a la carpeta del proyecto:

   ```bash
   git clone URL_DEL_REPOSITORIO
   cd t1_fastAPI
   ```

2. Instalar las dependencias incluidas en `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

3. Configurar la URI de MongoDB Atlas como variable de entorno `MONGO_URL`. No publicar credenciales en GitHub ni escribirlas directamente en el código.

4. Ejecutar la API localmente:

   ```bash
   python -m uvicorn src.main:app --reload
   ```

5. Abrir la documentación interactiva en el navegador:

   ```text
   http://127.0.0.1:8000/docs
   ```


## Rutas principales de la API

| Método | Ruta | Acción |
|---|---|---|
| `GET` | `/` | Mensaje de bienvenida |
| `POST` | `/trainee/` | Registrar un aprendiz |
| `GET` | `/trainee/` | Consultar todos los aprendices |
| `GET` | `/trainee/{id}` | Consultar un aprendiz por ID |
| `PUT` | `/trainee/{id}` | Actualizar un aprendiz |
| `DELETE` | `/trainee/{id}` | Eliminar un aprendiz |

## Despliegue

El código se guarda en GitHub y la API se despliega en Render. En Render se deben configurar las variables de entorno necesarias, incluida `MONGO_URL`, y en MongoDB Atlas se debe autorizar el acceso de red del servicio.
