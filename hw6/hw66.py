class First:
    color = "red"
    form = "circle"
    style = "cool"
    def changecolor(self,newcolor):
        self.color = newcolor
    def changeform(self,newform):
        self.form = newform
    def changestyle(self,newstyle):
        self.style = newstyle

class Second:
    color = "red"
    def changecolor(self, newcolor):
        self.color = newcolor


obj1 = First()
obj2 = Second()

print (obj1.color, obj1.form, obj1.style)
print (obj2.color) 
a=input("enter color: ")
obj1.changecolor(a)
if obj1.color == "green" :
    obj2.changecolor("blue")

print (obj1.color)
print (obj2.color)