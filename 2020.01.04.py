from tkinter import *
from PIL import ImageTk, Image
import os
import glob
files=glob.glob('*.jpg')
def draw_picture(picture):
    www = Tk()
    filename = picture
    img = Image.open(filename)
    img = img.resize((500, 500))
    width, height = img.size
    cv = Canvas(www, width=width, height=height)
    cv.pack()
    img_tk = ImageTk.PhotoImage(img)
    cv.create_image(0,0, image=img_tk, anchor=NW)
    www.after(1000, lambda: www.destroy())
    www.mainloop()
#filesにjpgファイルのリストがあります
for picture in files:
  draw_picture(picture)