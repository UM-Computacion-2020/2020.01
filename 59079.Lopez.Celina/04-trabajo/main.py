from person import Person
from personService import PersonService

if __name__ == '__main__':
   
    personService = PersonService()

    
    p1 = Person()
    p1.name = 'celina'
    p1.surname = 'lopez'
    p1.age = '21'
    personService.add_person(p1)

    
    p1 = Person()
    p1.name ='juan'
    p1.surname = 'perez'
    p1.age = '30'
    personService.add_person(p1)

    
    p2 = p1
    p2.name = 'agustin'
    p2.age = 30
    personService.add_person(p2)
    
    print (personService.get_personList()) 

    
    p2.age = 41
    personService.update_person(1, p2)
    
    print (personService.get_personList()) 
    

    
    personService.delete_person(2)
    print (personService.get_personList()) 
    