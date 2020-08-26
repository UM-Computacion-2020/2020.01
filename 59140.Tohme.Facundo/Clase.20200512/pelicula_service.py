# listra peliculas
# se define un servicio que actua sobre un repositorio(para que haga cosas)
# listar=recorrer todos los datos y mostrarlos en pantalla

from pelicula import pelicula
from pelicula_repository import PeliculaRepository


class PeliculaService():
    def __init__(self):
        self.repository = PeliculaRepository()

    def listar(self):
        print("listar")
        if self.repository.pelicula is not None:
            for key in self.repository.pelicula:
                print("Listar %s %s" % (key, self.repository.pelicula[key]))

    def agregar_pelicula(self):
        print("agregar")
        if self.repository.pelicula is not None:
            self.repository.pelicula = {}
        pelicula = pelicula("Avangers:Endgame", 181, 
                            "accion, aventura, drama", {})
        self.repository.pelicula["tt4154796"] = pelicula
        pelicula = pelicula("Titanic", 194,
                            "drama, romance", {})
        self.repository.pelicula["tt0120338"] = pelicula
        for key in self.repository.pelicula:
            print("Agregar%s %s" % (key, self.repository.pelicula[key]))
        self.listar()
