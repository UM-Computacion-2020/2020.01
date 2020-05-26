class Person:

    def __init__(self, name=None, surname=None, age=None):
        self._name = name
        self._surname = surname
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def age(self):
        return self._age
