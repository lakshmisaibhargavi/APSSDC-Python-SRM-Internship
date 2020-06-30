class Parent:
    name = 'abdul'
    fromLoc = 'kadpa'
    def msg():
        print('I am fromparent class')

class Child(Parent):
    cname = 'abdulla'
    cfromL='vmpli'
    def childMsg():
        print("i am from child class")

cobj = Child
print(cobj.name,cobj.fromLoc,cobj.cname)

cobj.msg()
cobj.childMsg()
