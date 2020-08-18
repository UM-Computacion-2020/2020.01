class Pelicula():
    def __init__(self, title="", duration=0, genre="", characters={}):
        self.title = title
        self.duration = duration
        self.genre = genre
        self.characters = characters

    def __str__(self):
        return "%s %d %s %s" % (self.title, self.duration, self.genre, self.characters)
        