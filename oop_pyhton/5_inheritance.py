#inherintance,extend,overide
class Employee :
    def __init__(self,name,email):
        self.name = name
        self.email = email
        
    def work(self):
        return f"{self.name} is working"
    
    
# turunan dari Employee
#dia dapet warisan atribut,property method
class Programmer(Employee):
    pass

print("")
employee = Employee("Agung","agung@company.com")
print(employee.work())

programmer = Programmer("Taufik","nurtaufik20220@gmail.com")
print(programmer.work())