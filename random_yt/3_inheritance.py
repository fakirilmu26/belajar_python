# class Cat:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def speak(self):
#         print("meow")
    

# class Dog :
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
    
#     def speak(self):
#         print("Bark")

# TUJUANNYA MENYEDERHANAKAN DUA KELAS DIATAS YANG MIRIP HANYA SPEAK.NYA YANG BERBEDA


#GENERALITATION CLASS
#PARENT
class Pet :
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what I say")
    


#SPECIFIC CLASS & INHERIT FROM PET
#CHILD
class Cat(Pet) :
    def __init__(self,name,age,color):
        #super digunakan untuk memanggil attribut dari parent
        super().__init__(name,age)
        self.color = color
    
    def speak(self):
        print("Meow")
       
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}") 
    
class Dog(Pet) :
    def speak(self):
        print("Bark")
    
    
        

class Fish(Pet):
    pass

p = Pet("Tim",19)
p.show()
c = Cat("Bill",34,"Red")
c.speak()
c.show()
d = Dog("Jill",34)
#d.speak()
d.show()
f= Fish("chubby",12)
f.speak()
        