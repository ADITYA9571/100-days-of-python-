"""
print("this is default arguments function:\n")
def average1(a=3,b=5):
    print("average is ",(a+b)/2)
def average2(a=3, b=5):
    return (a + b) / 2
print("average1 \n error ",average1(5,5))
print("average1 \n ",average2(5,5))
print("average2 \n ",average2(5))
print("average1 \n ",average2()) 

print("this is keyword arguments function:\n")
def namecard1(fname,mname,lname):
    print("Hello",fname,mname,lname)
def namecard2(fname,mname,lname):
    print("Hello",lname,mname,fname)
def namecard3(lname,mname,fname):
    print("Hello",lname,mname,fname)
namecard1(fname="aditya",mname="mohan",lname="jha")
namecard2(fname="aditya",mname="mohan",lname="jha")
namecard3(fname="aditya",mname="mohan",lname="jha")
namecard1(lname="aditya",mname="mohan",fname="jha")
namecard1("aditya","mohan","jha")
namecard2("aditya","mohan","jha")
namecard3("aditya","mohan","jha") 

print("this is required arguments function:\n")
namecard1("aditya","mohan","jha")
namecard1("jha","mohan","aditya")
"""
print("this is arbitary arguments function:")
print("This is kind of dictionary thing")
print("here we have to use *, this we can write in some kind of array structure:")
def name(*name):
    print("hello",name[0],name[1],name[2])
name("Aditya","Mohan","Jha")
def name2(*name2):
    print("hello",name2[2],name2[1],name2[0])
name2("Aditya","Mohan","Jha")
def average(*number):
    sum = 0
    for i in number:
        sum = sum+ + i 
    return sum/len(number)
print("average is ",average(5,6,7))