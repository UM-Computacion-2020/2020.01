class Pelicula():

    def __init__(self, titulo, duracion=0, genero, personajes={}):
        self.titulo = titulo
        self.duracion = duracion
        self.genero = genero
        self.personaje = personaje

    def __str__(self):
        return "%s %d %s %s" % (self.titulo, self.duracion, self.genero, self.personaje)
