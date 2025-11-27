"""Global variable"""
x = 10
y = 5
def pre():
    """Function"""
    print(x)
    y=10
    print(y)
    z=1
    global Z 
    Z = 2
    print(z)
# print(x,y,z) wrong as z is local varian=ble not global one 
pre()
print(x,y,Z)