class Person:
    def __init__(self, namec="", surnamec="", agec=0):
        self.namec = namec
        self.surnamec = surnamec
        self.agec = agec

    @property
    def name(self):
        return self.namec

    @name.setter
    def name(self, namep):
        self.namec = namep.upper()

    @property
    def surname(self):
        return self.surnamec

    @surname.setter
    def surname(self, surnamep):
        self.surnamec = surnamep.upper()

    @property
    def age(self):
        return self.agec

    @age.setter
    def age(self, agep):
        self.agec = agep

    def get_person(self):
        o = {"Name: ": self.name, "Surname: ": self.surname, "Age: ": self.age}
        return o
