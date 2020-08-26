class App():
    def __init__(self):
        self repository = PeliculaRepository
    def menu(self):
        print("1. Listar Peliculas")
        print("2. Agregar Pelicula")
        print("3. Modificar Pelicula")
        print("4, Eliminar Pelicula")

    

if __name__ == "__main__":
    app = App()
    opcion = app.menu()