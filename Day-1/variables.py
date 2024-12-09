print("Hello world")

carname = "Volvo"
print(carname)

x, y, z = "BMW", "Benz", "Bentley"
print(x)
print(y)
print(z)

x = y = z = "Aston Martin"
print(x)
print(y)
print(z)

## Global variable
x = "Cheen tapak"

def newFunc() :
    ## Global variable with global keyword
    global x
    x = "Dum"
    print(x + " Dum dum")

newFunc()     

