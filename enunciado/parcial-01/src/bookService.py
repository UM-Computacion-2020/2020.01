from repository import Repository


class BookService:

    # Devuelve repositorio bookList
    def get_booksList(self):
        return Repository.booksList

    # Agrega book en repositorio booksList
    # parametros : Object book
    # return: Key id
    def add_book(self, book):
        lastKey = -1
        for key in Repository.booksList:
            lastKey = key
        id_new = int(lastKey) + 1
        Repository.booksList[id_new] = book.__dict__
        return id_new

    # Actualiza book en repositorio bookList
    # parametros :  key id , Object book
    def update_book(self, id, book):
        if id not in Repository.booksList:
            raise ValueError("El id no existe")
        Repository.booksList.update({id: book.__dict__})

    # Asigna un libro a un member
    # parametros :  key id , key legajo
    def assign_book(self, id_book, legajo):
        if id_book not in Repository.booksList:
            raise ValueError("El id no existe")
        if legajo not in Repository.membersList:
            raise ValueError("El legajo  no existe")

        Repository.booksList[id_book]['_memberLegajo'] = legajo
