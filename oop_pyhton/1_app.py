# class User:
#     pass


# #zelda,link
# #name,email,role

# zelda = User()
# link = User()

#ini kelas
class User :
    def __init__(self,name,email,role):
        self.name = name
        self.email = email
        self.role = role
  
zelda = User("Zelda","Zelda@gmail.com","user")
# link = User("Link")       
#objek dari sebuah kelas user/intansiasi
# zelda = User("Zelda")
# link = User("Link")
#atribut assign
# zelda.name ="Zelda"
# link.name ="link"

print(zelda.name)
# print(link.name)

