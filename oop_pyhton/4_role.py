#PRIVAT ROLE __ROLE
class User :
    #class variable (didalam class) diluar contructor dan berlaku global bisa untuk menghitung berapa user yang dibuat
    total = 0
    #contructor
    def __init__(self,name,email,role):
        self.name = name
        self.email = email
        #pake private variabel, cuma bisa diakses hanya dalam kelas
        self.__role = role
        User.total += 1
    #membuat behavior perkenalan
    def info(self):
        return f"{self.name} - {self.email} - {self.__role}"
    
    def update_role(self, new_role):
        #jika bukan user maka bisa mengupdate role
        if self.__role != "user":
            self.__role =new_role
            
        
#instan variable
zelda = User("Zelda","Zelda@gmail.com","user")

#CARA AKSESNYA.....
print(zelda.__dict__)
print(zelda._User__role)
# zelda._User__role ="moderator"
# print(zelda.info())
print(zelda.getRole())



