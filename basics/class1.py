#Class and objects sample

class Employee:
    #initilize properties
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"ID : {self.id} \nName: {self.name}")

#creating an instance emp of the employee class

emp = Employee(1, "coder")
# display the emp's id and name
emp.display()
#delete emp's id
#del emp.id
#delete emp oject itself
try:
    print(emp.id)
except NameError:
    print("emp.id is not defined")

del emp
try:
    emp.display() # it will give error after deleting emp
except NameError:
    print("emp is not defined")