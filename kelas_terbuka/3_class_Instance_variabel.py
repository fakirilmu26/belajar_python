class Hero:
   #class variabel
   jumlah = 0

   def __init__(self,inputName,inputHealth,inputPower,inputArmor):
   	#instance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print ("membuat hero dengan nama "+ inputName)
        

hero1 = Hero("sniper",1000,10,4) 
print(Hero.jumlah)
hero2 = Hero("helda",1000,10,5) 
print(Hero.jumlah)
hero3 = Hero("ucup",1000,10,6) 
print(Hero.jumlah)



