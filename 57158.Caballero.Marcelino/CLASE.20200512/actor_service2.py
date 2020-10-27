from actor2 import Actor2


class ActorService2():
    def __init__(self, repository):
        self.repository = repository

    def listar(self):
        print("\n Listando")
        for key in self.repository.actores:
            print("--> %s" % (self.repository.actores[key]))

    def agregar_actor(self):
        print("\n Agregando")
        actor2 = Actor2()
        actor2.ingresar()
        self.repository.actores2[actor2.key] = actor2

    def eliminar(self):
        print("\n Eliminando")
        key = input("Ingrese el codigo a eliminar: ")
        del self.repository.actores2[key]

    def modificar(self):
        print("\n Modificando")
        key = input("Ingrese el codigo a modificar: ")
        actor2 = self.repository.actores2[key]
        print("Actor %s" % actor2)
        actor2.ingresar(True)
        self.repository.actores2[key] = actor2
