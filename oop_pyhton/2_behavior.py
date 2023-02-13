class User :
    #class variable (didalam class) diluar contructor dan berlaku global bisa untuk menghitung berapa user yang dibuat
    total = 0
    #contructor
    def __init__(self,name,email,role):
        self.name = name
        self.email = email
        self.role = role
        User.total += 1


#instan variable
zelda = User("Zelda","Zelda@gmail.com","user")
print(User.total)
mario = User("Mario","mario@gmail.com","user")
print(User.total)
#akses class variable
