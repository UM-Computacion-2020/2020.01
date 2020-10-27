from pelicula_repository2 import PeliculaRepository2
from pelicula_service2 import PeliculaService2
from actor_repository2 import ActorRepository2
from actor_service2 import ActorService2


class App2():
    def __init__(self):
        self.peliculas_db = PeliculaRepository2({})
        self.actores_db = ActorRepository2({})

    def menu_pelicula(self):
        print("\n\n1: Listar Peliculas")
        print("\n\n2: Agregar Pelicula")
        print("\n\n3: Modificar Pelicula")
        print("\n\n4: Eliminar Pelicula")
        return int(input("Elija una opcion: "))

    def menu_actor(self):
        print("\n\n1: Listar Actores/Actrices")
        print("\n\n2: Agregar Actor/Actriz")
        print("\n\n3: Modificar Actor/Actriz")
        print("\n\n4: Eliminar Actor/Actriz")
        return int(input("Elija una opcion: "))

    def menu(self):
        print("\n\n1: Menu Peliculas")
        print("\n\n2: Menu Actores")
        return int(input("Elija una opcion: "))


if __name__ == '__main__':
    app2 = App2()
    while True:
        opcion = app2.menu()
        if opcion == 1:
            while True:
                opcion_pelicula == app2.menu_pelicula()
                if opcion_pelicula == 1:
                    service = PeliculaService2(app2.peliculas_db)
                    service.listar()
                    service = None
                if opcion_pelicula == 2:
                    service = PeliculaService2(app2.peliculas_db)
                    service.agregar()
                    service = None
                if opcion_pelicula == 3:
                    service = PeliculaService2(app2.peliculas_db)
                    service.modificar()
                    service = None
                if opcion_pelicula == 4:
                    service = PeliculaService2(app2.peliculas_db)
                    service.eliminar()
                    service = None
                if opcion_pelicula < 1 or opcion_pelicula > 4:
                    break
        if opcion == 2:
            while True:
                opcion_actor == app2.menu_actor()
                if opcion_actor == 1:
                    service = ActorService2(app2.actores_db)
                    service.listar()
                    service = None
                if opcion_actor == 2:
                    service = ActorService2(app2.actores_db)
                    service.agregar()
                    service = None
                if opcion_actor == 3:
                    service = ActorService2(app2.actores_db)
                    service.modificar()
                    service = None
                if opcion_actor == 4:
                    service = ActorService2(app2.actores_db)
                    service.eliminar()
                    service = None
                if opcion_actor < 1 or opcion_actor > 4:
                    break
        if opcion < 1 or opcion > 2:
            break
