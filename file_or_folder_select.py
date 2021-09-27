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
import os
import glob
from tkinter import filedialog as tkFileDialog
import tkinter as tk
from tkinter import font
from tkinter.scrolledtext import ScrolledText

filenames =[]
select_file=[]

#最初の画面のクラス
class image_gui():  
    imgs = []
    def __init__(self, main):  
        
        button1 = Button(root_main, text=u'フォルダー選択', command=self.button1_clicked)  
        button1.grid(row=0, column=1)  
        button1.place(x=50, y=12) 

        button3= Button(root_main, text=u'ファイル   選択', command=self.button3_clicked)  
        button3.grid(row=0, column=1)  
        button3.place(x=50, y=42) 


    def button1_clicked(self):  

        global filenames
        ini_dir = 'C:'
        ret = tkinter.filedialog.askdirectory(initialdir=ini_dir, title='file dialog test', mustexist = True)
        print(str(ret))
        os.chdir(str(ret))
        filenames = glob.glob('*.jpg')
        textExample.insert(tkinter.END,filenames)

    def button3_clicked(self):  
        global filenames
        
        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        filenames = tkFileDialog.askopenfilenames(filetypes= [("JPEG", ".jpg") ], initialdir=iDir)
        textExample.insert(tkinter.END,filenames)

    def quit(self):
        root_main.destroy()

root_main= tkinter.Tk()  
image_gui(root_main)  
root_main.title("ファイル名を出力するだけ")  
root_main.geometry("1000x600") 

textExample=ScrolledText(root_main, height=35,width=120, wrap=tkinter.CHAR)
textExample.pack()
textExample.place(x=90, y=70)

textExample.delete("1.0",tkinter.END)

root_main.mainloop()

