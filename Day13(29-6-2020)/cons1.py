##class Info:
##    def __init__(self):
##        print("i am default cons")
##
##
##obj = Info()


class ClassInfo:
    def __init__(self,name,branch,age):
        self.Name=name
        self.Branch = branch
        self.Age = age
        print(self.Name,' data is added')
    def display(self):
        print('Name = ',self.Name)
        print('Age = ',self.Age)
        print('branh=',self.Branch)
        print('mobilr no=',self.mbno)
        print('Mail Id=',self.eid)

    def setprofileInfo(self,mbno,eid):
        self.mbno = mbno
        self.eid = eid
        
abdul = ClassInfo('abdul','cse',25)
abdul.display()
abdul.setprofileInfo('8956230147','abdul@gmail.com')





##ravi = ClassInfo('ravi','it',28)
##raja = ClassInfo('raja','ece',30)
##raja.display()
##raja.eduInfo()






        
