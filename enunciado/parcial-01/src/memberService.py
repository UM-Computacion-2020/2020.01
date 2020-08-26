from repository import Repository


class MemberService:

    # Devuelve repositorio memberList
    def get_membersList(self):
        return Repository.membersList

    # Agrega member en repositorio memeberList
    # parametros : Object member
    # return: Key legajo
    def add_member(self, member):
        lastKey = -1
        for key in Repository.membersList:
            lastKey = key
        legajo_new = int(lastKey) + 1
        Repository.membersList[legajo_new] = member.__dict__
        return legajo_new

    # Actualiza member en repositorio memberList
    # parametros :  key legajo , Object member
    def update_member(self, legajo, member):
        if legajo not in Repository.membersList:
            raise ValueError("El legajo no existe")
        Repository.membersList.update({legajo: member.__dict__})

    # Elimina member de membersList
    # parametros: key legajo, Object member
    def delete_member(self, legajo):
        if legajo not in Repository.membersList:
            raise ValueError("El legajo a elminar no existe")
        del Repository.membersList[legajo]
