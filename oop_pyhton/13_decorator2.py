#inner function adalah method yang ada didalam method
def info(func):
    def wrapper():
        print("*"*10)
        func()    
        print("*"*10)    
    return wrapper
print("")
#pakai dekorator
@info
def say_hello():
    print("say hello")

#say_hello()
#menambahkan behavior dari sebuah fungsi tanpa mengubah fungsi sebelumnya

#say_hello = info(say_hello)
say_hello()
