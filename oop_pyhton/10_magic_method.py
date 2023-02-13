class Game:
    def __init__(self,title,price) :
        self.title =title
        self.price =price
        #print("aku dipanggil lho")
        
    def __str__(self):
        return f"{self.title}-${self.price}"
    
    def __eq__(self,other):
        #untuk mengecek apakah itu di memori  yang sama
        return self.title == other.title
    
    #mengecek greater than (gt)
    def __gt__(self,other):
        return self.price > other.price
    
    #menjumlahkan     
    def __add__(self,other):
        return self.price + other.price
        
zelda = Game("Bernafas sekali lagi", 69000)
zelda2 = Game("Bernafas sekali lagi", 60000)
mario = Game("Bernafas dua kali", 69000)

#ketika kita melempar objek, si zelda akan memanggil str
print(zelda)
print(zelda==zelda2)
print(zelda==mario)

#gt
print(zelda>zelda2)
#add
print(zelda+zelda2)

