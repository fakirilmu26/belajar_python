# class Hero:
#     def __init__(self,x):
#         print("halo", x)
        
# hero1 = Hero(10) 
#------------------------------------------
# class Hero:
#     def __init__(self,inputName):
#         self.name = inputName
        
# hero1 = Hero("sniper") 
# hero2 = Hero("helda") 
# hero3 = Hero("ucup") 

# print(hero1.name)
# print(hero2.name)
# print(hero3.name)
#-------------------------------------------
class Hero:
    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        
        
hero1 = Hero("sniper",1000,10,4) 
hero2 = Hero("helda",1000,10,5) 
hero3 = Hero("ucup",1000,10,6) 


print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
# print(hero1.name)
# print(hero2.name)
# print(hero3.name)