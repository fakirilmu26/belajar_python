#inner function adalah method yang ada didalam method
class Game :
    def __init__(self,title,price):
        self.title = title
        self.price = price
    #ini inner function
    def info(self):
        def print_title():
            return f"Title : {self.title}"
            
        def print_price():
            return f"Price : {self.price}"
        
        return print_title
        
        
        
print("")



zelda = Game("bernafas sekali lagi",69)
title = zelda.info()
print(title)
print(title())

