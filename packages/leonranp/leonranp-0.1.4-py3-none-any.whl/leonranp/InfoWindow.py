#Tkinter help-window code
#Coded by LeonMMcoset
import tkinter as tk
from tkinter import PhotoImage,Canvas
root = tk.Tk()
root.title('Leon Random Plus')
root.geometry('800x600+0+0')
canvas = Canvas(root,width=800,height=600)
canvas.pack()
def image(image,x,y):
    _image_ = PhotoImage(file=image)
    canvas.create_image(_image_,x,y)
def text(text,x,y):
    label = tk.Label(root,text=text)
    label.place(x=x,y=y)
text('-------------Leon Random Plus-------------', 10, 10)
text('Welcome to using Leon Random Plus!', 10, 50)
text('PyPI:https://pypi.org/project/leonranp/', 10, 100)
text('Wiki:http://leonmmcoset.jjmm.ink:8002/doku.php?id=leonranp', 10, 150)
text('Github:https://github.com/Leonmmcoset/leonranp/', 10, 200)
text('To upgrade,use "upgrade()" on your shell', 10, 250)
text('To have help,use "lrphelp()"', 10, 300)
text('To delete Leon Random Plus,use "dellrp()"', 10, 350)
text('------------------------------------------', 10, 400)
text('Star my github project!',10,450)
text('©LeonMMcoset 2022-2024',10,500)
root.mainloop()