class Member:

    def __init__(self, name='', surname='', age='', phone=''):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone

    # getting
    @property
    def name(self):
        return self._name

    # setting
    @name.setter
    def name(self, name):
        self._name = name.upper()

    # deleting
    @name.deleter
    def name(self):
        del self._name

    @property
    def surname(self):
        return self._surname

    # setting
    @surname.setter
    def surname(self, surname):
        self._surname = surname.upper()

    # deleting
    @surname.deleter
    def surname(self):
        del self._surname

    @property
    def age(self):
        return self._age

    # setting
    @age.setter
    def age(self, age):
        self._age = age

    # deleting
    @age.deleter
    def age(self):
        del self._age

    @property
    def phone(self):
        return self._phone

    # setting
    @phone.setter
    def phone(self, phone):
        self._phone = phone

    # deleting
    @phone.deleter
    def phone(self):
        del self._phone
