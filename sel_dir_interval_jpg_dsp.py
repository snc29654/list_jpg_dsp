### インポート
import tkinter
import glob
from tkinter import *
from PIL import ImageTk, Image
import os
import sys
import time
import tkinter
from PIL import Image, ImageTk
import threading
import time
import glob
import os,sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import shutil
import os
import glob
from tkinter import filedialog as tkFileDialog
import tkinter as tk
from tkinter import font

interval = 1.0
sizerate = 1.0
filenames =[]
select_file=[]

#最初の画面のクラス
class image_gui():  
    imgs = []
    def __init__(self, main):  
        
        button1 = Button(root_main, text=u'フォルダー選択', command=self.button1_clicked)  
        button1.grid(row=0, column=1)  
        button1.place(x=670, y=12) 

        button3= Button(root_main, text=u'ファイル選択', command=self.button3_clicked)  
        button3.grid(row=0, column=1)  
        button3.place(x=670, y=42) 


        button2 = tk.Button(root_main, text = '実行', command=self.quit)
        button2.grid(row=0, column=1)  
        button2.place(x=770, y=12) 


        #文字色、背景色、サイズ、フォントを指定。
        font1 = font.Font(family='Helvetica', size=12, weight='bold')
        label2 = tkinter.Label(root_main, text="インターバル(秒）", fg="red", bg="white", font=font1)
        label2.pack(side="top")
        label2.place(x=100, y=28) 

        label4 = tkinter.Label(root_main, text="サイズ倍率", fg="red", bg="white", font=font1)
        label4.pack(side="top")
        label4.place(x=400, y=28) 



    def button1_clicked(self):  
        global interval
        interval =txt2.get()
        global sizerate
        sizerate =txt4.get()
        
        if interval=="":
            txt3.insert(tkinter.END,str(interval)+"インターバルが未設定です。")
        else:
            txt3.insert(tkinter.END,str(interval)+"秒 に設定しています。" )

        if sizerate=="":
            txt3.insert(tkinter.END,str(interval)+"倍率が未設定です。")
        else:
            txt3.insert(tkinter.END,str(interval)+"倍に設定しています。" )


        global filenames
        ini_dir = 'C:'
        ret = tkinter.filedialog.askdirectory(initialdir=ini_dir, title='file dialog test', mustexist = True)
        print(str(ret))
        os.chdir(str(ret))
        #filenames = []
        filenames = glob.glob('*.jpg')
        print(filenames)


    def button3_clicked(self):  
        global filenames
        global interval
        interval =txt2.get()
        global sizerate
        sizerate =txt4.get()
        
        if interval=="":
            txt3.insert(tkinter.END,str(interval)+"インターバルが未設定です。")
        else:
            txt3.insert(tkinter.END,str(interval)+"秒 に設定しています。" )

        if sizerate=="":
            txt3.insert(tkinter.END,str(interval)+"倍率が未設定です。")
        else:
            txt3.insert(tkinter.END,str(interval)+"倍に設定しています。" )


        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        filenames = tkFileDialog.askopenfilenames(filetypes= [("Image file", ".bmp .png .jpg .tif"), ("Bitmap", ".bmp"), ("PNG", ".png"), ("JPEG", ".jpg"), ("Tiff", ".tif") ], initialdir=iDir)
        print(filenames)


    def quit(self):
        root_main.destroy()




 
def get_index(event):
    value = tkinter.StringVar()
 
    index = event.widget.curselection()
 
    n = event.widget.get(index)
    value.set(n)
    select_one_image(n)
    print("get_index=" + n)


def view_image():
    global item, canvas


    sub = tkinter.Tk()
    sub.title("subです")  
    list_disp(filenames)

    sub.geometry("500x300")


    sub.mainloop()
 
 


def select_one_image(n):

    root_one = tkinter.Tk()
    root_one.title("root_oneです")  
    root_one.geometry("1x1")

    txt2 = tk.Entry(width=100)
    txt2.place(x=90, y=400)
    img2 = Image.open(n)
    before_x, before_y = img2.size[0], img2.size[1]
    x = int(round(float(300 / float(before_y) * float(before_x))))
    y = 300
    img2.thumbnail((x*float(sizerate), y*float(sizerate)), Image.ANTIALIAS)
    img2 = ImageTk.PhotoImage(img2)
    canvas = tkinter.Canvas(bg = "white", width=500, height=400)
    canvas.place(x=0, y=0)
    item = canvas.create_image(30, 30, image=img2, anchor=tkinter.NW)
    canvas.itemconfig(item,image=img2)
    txt2.delete(0, tk.END)
    txt2.insert(tk.END,n)
    #list_disp(filenames)
    root_one.after(10, lambda: root_one.destroy())
    root_one.mainloop()


def list_disp(filenames):

    root_list = tkinter.Tk()
    root_list.title("root_listです")  
    root_list.geometry("1x1")
    root_list.configure(bg="white")
    value = tkinter.StringVar()
    frame = tkinter.Frame(master=None)
    scrollbar = tkinter.Scrollbar(master=frame, orient="vertical")
    listbox = tkinter.Listbox(master=frame,  bg="white", height=15, yscrollcommand=scrollbar.set)
    for name in filenames:
        listbox.insert(tkinter.END, name)
    scrollbar.config(command=listbox.yview)
    label = tkinter.Label(master=root_list, textvariable=value,  fg="black", bg="white", height=3, width=15)
    frame.pack(padx=50,pady=100)
    scrollbar.pack(side=tkinter.RIGHT, fill="y")
    listbox.pack(padx=480)
    label.pack(pady=200, side="bottom")
    listbox.bind("<<ListboxSelect>>", get_index)
 
    #root_list.after(100, lambda: root_list.destroy())
    root_list.mainloop()

root_main= tkinter.Tk()  
image_gui(root_main)  
root_main.title("rootです")  
root_main.geometry("850x300") 
txt2 = tkinter.Entry(width=10)
txt2.place(x=10, y=30)
txt2.insert(tkinter.END,"1.0")

txt4 = tkinter.Entry(width=10)
txt4.place(x=330, y=30)
txt4.insert(tkinter.END,"1.0")


txt3 = tkinter.Entry(width=80)
txt3.place(x=10, y=60)
txt3.insert(tkinter.END,"")

root_main.mainloop()


thread1 = threading.Thread(target=view_image)
thread1.start()

    

