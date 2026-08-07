from prettytable import PrettyTable

class Student:
    def __init__(self):
        pass
    
    def display(self):
        print("Hi this is display method!")
        
student = Student()
student.display()


# ---------------------------Car Class --------------------
class Car:
    def __init__(self):
        print("--init__ method of Car class called...")
    
    def speed(self):
        print("this is speed method")

car = Car()
car.speed()
# ---------------------------------------------------------

## Example of PreetyTable module use.
table = PrettyTable()

# table.add_column("Name", ["hairsh", "sonal"])
table.field_names = (["Name", "City", "Age"])
table.add_row(["sunit", "indore", 32])
table.add_row(["pushpa", "bhopal", 44])

print(table)





