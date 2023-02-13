class Hero:
    #private class variabel
    __jumlah = 0
    
    def __init__(self,name):
        self.__name = name
        Hero.__jumlah += 1
    
    #membuat getter untuk mendapatkan nilai dari  jumlah
    #method ini hanya berlaku untuk objek
    def getJumlah(self):
        return Hero.__jumlah
    
    #method ini tidak berlaku untuk objek tapi berlaku untuk kelas
    def getJumlah1():
        return Hero.__jumlah
    
    #method static (decorator) nempel ke objek dan class
    @staticmethod
    def getJumlah2():
        return Hero.__jumlah
    
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah
    
    
    
sniper = Hero('sniper')
print(sniper.getJumlah())
print(Hero.getJumlah1())

#pake staticmethod
rikimaru= Hero('rikimaru')
print(Hero.getJumlah2())
drowranger= Hero('drowranger')
print(sniper.getJumlah2())

#pake classmethod
drowranger= Hero('drowranger')
print(sniper.getJumlah3())



