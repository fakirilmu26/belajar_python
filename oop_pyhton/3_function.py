class User :
    #class variable (didalam class) diluar contructor dan berlaku global bisa untuk menghitung berapa user yang dibuat
    total = 0
    #contructor
    def __init__(self,name,email,role):
        self.name = name
        self.email = email
        self.role = role
        User.total += 1
    #membuat behavior perkenalan
    def info(self):
        return f"{self.name} - {self.email} - {self.role}"
    
    def update_role(self, new_role):
        #jika bukan user maka bisa mengupdate role
        if self.role != "user":
            self.role =new_role
            
        
#instan variable
zelda = User("Zelda","Zelda@gmail.com","user")
#print(zelda.info())
zelda.update_role("moderator")
print(zelda.info())
print(User.total)


#percobaan update role dengan menggunakan role admin
mario = User("Mario","mario@gmail.com","admin")
print(mario.info())
mario.update_role("moderator")
print(mario.info())
print(User.total)
#akses class variable
