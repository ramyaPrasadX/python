class Employee:

    def __init__(self, num, name):
        self.id = num
        self.name = name

    def display(self):
        print(f"ID: {self.id} \nName: {self.name}")


# Creating an emp instance of Employee class
emp = Employee(1, "coder")

emp.display()
print(emp.id)
#delete id property of the object
#del emp.id

#delete object itslef
try:
    print(emp.id)
except NameError:
    print("emp,id ain't defined")

del emp

try:
    emp.display() # will give error after deleteing
except NameError:
    print("emp is not defined")
