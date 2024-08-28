class Employee:

    salary = 2000000
    language = "Py"
    def __init__(self):
        print("I am init method, being called whenever an object of this Employee class is getting created")

class Engineer:
    def __init__(self):
        print("This is engineers squad")

class Coder(Employee,Engineer):

    def __init__(self):
        super().__init__()
        print("I am Coder")

#    name = "Krishna"
#    salary = 1500000   # class instance attributes
#    language = "Python"


# Ashu = Employee()
# Ashu.name = " Ashwini "  # object/instance attributes
# Ashu.language = "Java "
# print(Ashu.name, Ashu.salary, Ashu.language)

# Deepak = Employee()
# Deepak.name = "Deepak PS"
# print(Deepak.name, Deepak.salary, Deepak.language)

# Dee = Engineer()
Deee = Coder()