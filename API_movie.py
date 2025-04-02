import requests

class ApiMovie:
    def __init__(self):
        try:
            # Solicita al usuario el nombre de la película y elimina espacios extra
            self.nombre_pelicula = str(input("Ingresa el nombre de la pelicula para ver su informacion: ")).strip()
            
            # Valida que el usuario haya ingresado un nombre de película
            if not self.nombre_pelicula:
                print("Los campos no pueden estar vacíos.")
                return
            
            # Construye la URL de la API con el nombre de la película
            self.url_key = f"http://www.omdbapi.com/?t={self.nombre_pelicula}&apikey=TU_API_KEY"
        
        except ValueError:
            print("Error de digitación. Ingresa nuevamente el valor correcto.")
    
    def busqueda_pelicula(self):
        try:
            # Realiza la solicitud GET a la API de OMDB
            respuesta = requests.get(self.url_key)
            
            # Convierte la respuesta a formato JSON
            peticion_json = respuesta.json()
            
            # Extrae la descripción y el póster de la película
            descripcion_pelicula = peticion_json["Plot"]
            poster_pelicula = peticion_json["Poster"]
            
            # Verifica que la solicitud haya sido exitosa
            if 200 <= respuesta.status_code < 300:
                print("\n--- Información de la Película ---")
                print(f"Descripción de la película: {descripcion_pelicula}.")
                print(f"Póster de la película: {poster_pelicula}\n.")
            else:
                print(f"Error: {respuesta.status_code}, {respuesta.text}.")
        
        except Exception as error:
            print(f"Error en el programa: {error}.")

# Ejecuta la búsqueda de la película si el script se ejecuta directamente
if __name__ == "__main__":
    busqueda = ApiMovie()
    busqueda.busqueda_pelicula()
