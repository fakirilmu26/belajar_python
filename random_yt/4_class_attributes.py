class Person:
    number_of_people = 0
    
    def __init__(self,name):
        self.name = name
        #Person.number_of_people +=1
        Person.add_person()
        
    #class method
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people
    
    @classmethod
    def add_person(cls):
        cls.number_of_people +=1
        
    
    
p1 = Person("tim")
#print(p1.number_of_people)
p2 = Person("jill")
#print(p2.number_of_people)
print(Person.number_of_people_())
#bisa akses seperti ini karena number of people bersifat general
# Person.number_of_people = 8

