#class
class Hero:
    #function
    def __init__(self,name,health,armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        #self.__info = "name {} : \n\thealth:{}".format(self.__name,self.__health)
    #ketika coba dibuatkan get maka warna health di parent berubah
    # def getHealth(self):
    #     return self.__health
    #diganti dengan property (mengubah method seperty variabel)
    @property
    def info(self):
        #name.nya bisa dirubah disini
       return "name {} : \n\thealth:{}".format(self.name,self.__health)
       #return self.__info
       
    #METHOD
    @property
    def armor(self):
        pass
    
    @armor.getter
    def armor(self):
        return self.__armor
    
    
#instansiasi
sniper = Hero('sniper',100,20)


print('merubah info')
print(sniper.info)
sniper.name = 'dadang'
print(sniper.info)

print('getter dan setter untuk __armor:')
print(sniper.armor)






#print(sniper.__dict__)
#masalahnya disini variabelnya bisa dioverride oleh client makanya harus menggunakan property @
#sniper.info = "info"

#print(sniper.getHealth())

#KEUNGGULANNYA : CLIENT TIDAK BISA MERUBAH NILAI INFO KETIKA SUDAH DI PRIVAT
    