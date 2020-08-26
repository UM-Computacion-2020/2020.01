class Book:

    def __init__(self, name='', authorName='', memberLegajo=''):

        self.name = name
        self.authorName = authorName
        self.memberLegajo = memberLegajo

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
    def authorName(self):
        return self._authorName

    # setting
    @authorName.setter
    def authorName(self, authorName):
        self._authorName = authorName.upper()

    # deleting
    @authorName.deleter
    def authorName(self):
        del self._authorName

    @property
    def memberLegajo(self):
        return self._memberLegajo

    # setting
    @memberLegajo.setter
    def memberLegajo(self, memberLegajo):
        self._memberLegajo = memberLegajo

    # deleting
    @memberLegajo.deleter
    def memberLegajo(self):
        del self._memberLegajo
