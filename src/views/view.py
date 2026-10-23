
import requests

BASE_URL = "https://t1-fastapi-zthw.onrender.com"


class TraineeView:

    def __init__(self):
        self.url = BASE_URL.rstrip("/")
        self.session = requests.Session()

    def enviar(self, metodo, ruta, **kwargs):
        try:
            respuesta = self.session.request(
                metodo,
                f"{self.url}{ruta}",
                timeout=60,
                **kwargs
            )

            if respuesta.content:
                resultado = respuesta.json()
            else:
                resultado = respuesta.status_code

            if respuesta.ok:
                print("\nResultado:", resultado)
            else:
                print(
                    f"\nError HTTP {respuesta.status_code}:",
                    resultado
                )

        except requests.exceptions.RequestException as error:
            print("No fue posible conectar con la API:", error)

        except ValueError:
            print("La respuesta de la API no es JSON válido.")

    def crear(self):
        try:
            datos = {
                "document": input("Documento: "),
                "firstName": input("Nombre: "),
                "lastName": input("Apellido: "),
                "email": input("Correo: "),
                "age": int(input("Edad: ")),
                "programn": input("Programa: "),
                "record_number": int(input("Número de registro: "))
            }

            self.enviar("POST", "/trainee/", json=datos)

        except ValueError:
            print("La edad y el número de registro deben ser números.")

    def consultar(self):
        self.enviar("GET", "/trainee/")

    def consultar_por_id(self):
        id = input("ID del aprendiz: ")
        self.enviar("GET", f"/trainee/{id}")

    def actualizar(self):
        id = input("ID del aprendiz: ")
        datos = {}

        campos = {
            "firstName": "Nuevo nombre: ",
            "lastName": "Nuevo apellido: ",
            "email": "Nuevo correo: ",
            "age": "Nueva edad: ",
            "programn": "Nuevo programa: ",
            "record_number": "Nuevo número de registro: "
        }

        try:
            for campo, mensaje in campos.items():
                valor = input(mensaje)

                if valor.strip():
                    if campo in ("age", "record_number"):
                        valor = int(valor)

                    datos[campo] = valor

            if datos:
                self.enviar("PUT", f"/trainee/{id}", json=datos)
            else:
                print("No ingreso datos para actualizar.")

        except ValueError:
            print("La edad y el número de registro deben ser números.")

    def eliminar(self):
        id = input("ID del aprendiz que deseas eliminar: ")

        if input("¿Confirmas la eliminación? (s/n): ").lower() == "s":
            self.enviar("DELETE", f"/trainee/{id}")
        else:
            print("Eliminación cancelada.")

    def menu(self):
        while True:
            print("\n===== GESTIÓN DE APRENDICES =====")
            print("1. Crear aprendiz")
            print("2. Consultar todos")
            print("3. Consultar por ID")
            print("4. Actualizar aprendiz")
            print("5. Eliminar aprendiz")
            print("6. Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == "1":
                self.crear()
            elif opcion == "2":
                self.consultar()
            elif opcion == "3":
                self.consultar_por_id()
            elif opcion == "4":
                self.actualizar()
            elif opcion == "5":
                self.eliminar()
            elif opcion == "6":
                self.session.close()
                print("Programa finalizado.")
                break
            else:
                print("Opción no válida.")


if __name__ == "__main__":
    vista = TraineeView()
    vista.menu()
