class Hero:
	#class variabel
	jumlah_hero= 0

	def __init__(self,inputName,inputHealth,inputPower,inputArmor):
		#instance variabel
		self.name = inputName
		self.health = inputHealth
		self.power = inputPower
		self.armor = inputArmor
		Hero.jumlah_hero += 1

	#INI METHOD---------------------------
	#void function, method tanpa return
	def siapa(self):
		print("namaku adalah " + self.name)


	#method dengan argumen
	def healthUp(self,up):
		self.health += up

	#method dengan return
	def getHealth(self):
		return self.health
	#------------------------------------

#instansiasi
hero1 = Hero("sniper",1000,10,4) 
hero2 = Hero("helda",1000,10,5) 

# print(hero1.__dict__)
# print(hero2.__dict__)
hero1.siapa()
#print void
hero1.healthUp(10)
#cara manggil sebelum di return print(hero1.health)
print(hero1.getHealth())

