# class Hero:
# 	def __init__(self,name,health,attackPower,armorNumber):
# 		self.name = name
# 		self.health = health
# 		self.attackPower = attackPower
# 		self.armorNumber = armorNumber

# 	def serang(self):
# 		print(self.name + ' menyerang')

# 	def diserang(self):
# 		print(self.name + ' diserang')

# sniper = Hero('sniper',100,10,5)
# Helda = Hero('sniper',100,10,5)


# sniper.serang()
#-----------------------------------
#interaksi yang  hanya memasukan nama bisa menghasilkan argumen saling serang dan diserang coba run di terminal
class Hero:
	def __init__(self,name,health,attackPower,armorNumber):
		self.name = name
		self.health = health
		self.attackPower = attackPower
		self.armorNumber = armorNumber

	def serang(self,lawan):
		print(self.name + ' menyerang ' + lawan.name)
		lawan.diserang(self)

	def diserang(self,lawan):
		print(self.name + ' diserang ' + lawan.name)

sniper = Hero('sniper',100,10,5)
helda = Hero('helda',100,10,5)


#PUNCH LINE
sniper.serang(helda)
# masukan ke method serang helda.diserang()

# print(helda)



# def fungsi(argumen1,argumen2):
# 	print(argumen1)
# 	print(argumen2)