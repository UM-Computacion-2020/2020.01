from employee import Employee, Person

class Administration:
    listEmploye={}



    def add_employee(self,employee):
        legajo=len(self.listEmploye)
        self.listEmploye[legajo]=employee
        return

if __name__ == "__main__":
    adm= Administration()
    adm.add_employee({"name":"Franco", "surname":"Trifiro", "age":20, "phone":2615870558})
    adm.add_employee({"name":"Nicolas", "surname":"Pico", "age":30, "phone":2615870558})
    print(adm.listEmploye)
