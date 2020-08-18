from peliculas_repo import PeliculaRepo
from pelicula import Pelicula

class PeliculaService():
    def listar(self):
        repository = PeliculaRepo()
        for pelicula in repository.peliculas:
            print("Listar %s" % repository.peliculas[pelicula])

    def agregar_pelicula(self):
        repository = PeliculaRepo()
        pelicula = Pelicula("Avengers: Endgame", 181, "accion", {})
        repository.peliculas["001"] = pelicula
        for pelicula in repository.peliculas:
            print("Agregar %s" % repository.peliculas[pelicula])

        self.listar()

