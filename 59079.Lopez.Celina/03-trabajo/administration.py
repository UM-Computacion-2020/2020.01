from employee import Employee, Person

class Administration:
    listEmployee={}
    
    
    def add_employee(self,employee):
        legajo=len(self.listEmployee)
        self.listEmployee[legajo]=employee
        return

if __name__ == '__main__':
   adm=Administration()
   adm.add_employee({'name':"Celina",'surname':"Lopez",'age':21,'phone':261478529})
   adm.add_employee({'name':"Agustin",'surname':"Perez",'age':30,'phone':261748294})            
   print(adm.listEmployee)   
   