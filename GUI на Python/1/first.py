from tkinter import *
from childwindow import Childwindow


class Window:
    def __init__(self, width, height, title="mywindow", resizable=(False, False), icon=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(f"{width}x{height}+200+200")
        self.root.resizable(resizable[0], resizable[1])
        if icon:
            self.root.iconbitmap(icon)

    def run(self):
        self.root.mainloop()


    def create_child(self, width, height, title="child", resizable=(False, False), icon=None):
        Childwindow(self.root, width, height, title, resizable, icon)

if __name__ == "__main__":
    window = Window(500, 500, "kkkkkk")
    window.create_child(200, 100)


    window.run()

# window.title("hello tkinter")
'''
window = Tk()
width = 400
height = 500
x = 600
y = 300
window.geometry(f'{width}x{height}+{x}+{y}')
'''
'''
window.geometry('800x600+200+300')
window.resizable(False, False)
window.iconbitmap("1.ico")
window.mainloop()
'''
