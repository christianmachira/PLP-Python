# illustrating the use of OOP in python
# creating an employee class
class Employee:
    # creating a constructor that initializes the name, age, department and ID number of the employee
    def __init__(self,name,age,department,IDno):
        self.name = name
        self.age = age
        self.department = department
        self.IDno = IDno
    # creating a method that prints out the details of the employee
    def _str_(self):
        print(f"My name is {self.name}, I am {self.age} years old, I work in the {self.department} department and my ID number is {self.IDno}")

# creating an instance(object) of class Employee
person1=Employee("Chris", 23, "IT", 3780)

# printing out the details of the employee using the print() function
person1._str_()
print(person1.name)



         
