from pelicula_service import PeliculaService
from peliculas_repo import PeliculaRepo

class App():
    def __init__(self):
        self.repository = PeliculaRepo()

    def menu(self):
        print("1. Listar peliculas")
        print("2. Agregar pelicula")
        print("3. Modificar pelicula")
        print("4. Eliminar pelicula")
        return int(input("Elija una opcion: "))


if __name__ == "__main__":
    app = App()
    opcion = app.menu()
    service = PeliculaService()
    if opcion == 1:
        service.listar()
    if opcion == 2:
        service.agregar_pelicula()
    if opcion == 3:
        pass
    if opcion == 4:
        pass
