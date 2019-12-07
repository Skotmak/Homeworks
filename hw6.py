class First:
    color = "red"
    def out(self):
        print (self.color + "!")

obj1 = First()
obj2 = First()

print (obj1.color)
print (obj2.color)
obj1.out()
obj2.out()


class Second:
    color = "red"
    form = "circle"
    style = "cool"
    def changecolor(self,newcolor):
        self.color = newcolor
    def changeform(self,newform):
        self.form = newform
    def changestyle(self,newstyle):
        self.style = newstyle

obj1 = Second()
obj2 = Second()
obj3 = Second()

print (obj1.color, obj1.form) # вывод на экран "red circle"
print (obj2.color, obj2.form) # вывод на экран "red circle"
print (obj3.color, obj3.form, obj3.style)

obj1.changecolor("green") # изменение цвета первого объекта
obj2.changecolor("blue") # изменение цвет второго объекта
obj2.changeform("oval") # изменение формы второго объекта
obj3.changecolor("white")
obj3.changeform("rectungle") 
obj3.changestyle("not cool")

print (obj1.color, obj1.form) # вывод на экран "green circle"
print (obj2.color, obj2.form) # вывод на экран "blue oval"
print (obj3.color, obj3.form, obj3.style)