class Employee:
    languague = "Py"  # this is Class attribute
    Salary = 150000   # this is Class attribute


Ashu = Employee()
# print(Ashu)   # this will print address of the object
#output: <__main__.Employee object at 0x000001C6380A44A0> 
# print(id(Ashu))
#Output : 1950855349408 

Ashu.name = "Ashwini Jadhav"   # Instance attributes
Ashu.married = True            # Instance attributes

print( Ashu.name, Ashu.languague, Ashu.Salary, Ashu.married)

Deepak = Employee()
Deepak.name = "Deepak P S"
Deepak.married = True
print( Deepak.name, Deepak.languague, Deepak.Salary, Deepak.married)