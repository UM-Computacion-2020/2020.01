from pelicula_service import PeliculaService
from pelicula_repository import PeliculaRepository


class App():
    def __init__(self):
        self.repository = PeliculaRepository

    def menu(self):
        print("1. listar pelucica")
        print("2. agregar pelucica")
        print("3. modificar pelicula")
        print("4. eliminar pelicula")
        return int(input("Elija pelicula)"))


if __name__ == '__main__':
    app = App()
    # opcion = app.menu()
    print("1")
    service = PeliculaService()
    print("2")
    service.listar()
    print("3")
    service.agregar_pelicula
    print("4")
    service.listar()

    # if opcion == 1 : 
     # service.listar()
    # if opcion == 2:
     # service.agregar.pelicula
    # if opcion == 3:
        # pass
    # if opcion == 4:
        # pass
