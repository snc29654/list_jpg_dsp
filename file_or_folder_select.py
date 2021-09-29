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

select_file=[]

#最初の画面のクラス
class image_gui():  
    imgs = []
    def __init__(self, main):  
        self.combovalue = "jpg"
        self.filenames =[]
        
        button1 = Button(root_main, text=u'フォルダー選択', font=24,command=self.button1_clicked)  
        button1.grid(row=0, column=1)  
        button1.place(x=50, y=12) 

        button3= Button(root_main, text=u'ファイル選択', font=24,command=self.button3_clicked)  
        button3.grid(row=0, column=1)  
        button3.place(x=50, y=50) 

        button4= Button(root_main, text=u'クリア', font=24,command=self.button4_clicked,bg='#f0e68c')  
        button4.grid(row=0, column=1)  
        button4.place(x=250, y=12) 

        self.textExample=ScrolledText(root_main, height=22,width=90, wrap=tkinter.CHAR,bg="lightgreen")
        self.textExample.pack()
        self.textExample.place(x=90, y=100)
        self.textExample.config(font=24)
        self.textExample.delete("1.0",tkinter.END)


        item_list = ['jpg', 'txt']
        self.test_combobox = ttk.Combobox(
            master=root_main,
            values=item_list,
            )

        #値選択時に発生するイベントと関数を紐づけ
        self.test_combobox.bind(
            '<<ComboboxSelected>>',     #選択時に発生するイベント
            self.show_selected,              #呼び出す関数
        )

        self.test_combobox.current(0)
        self.test_combobox.pack()




    def button1_clicked(self):  

        ini_dir = 'C:'
        ret = tkinter.filedialog.askdirectory(initialdir=ini_dir, title='file dialog test', mustexist = True)
        print(str(ret))
        os.chdir(str(ret))
        if(self.combovalue=="jpg"):
            self.filenames = glob.glob('*.jpg')
            self.textoutjpg()     
        if(self.combovalue=="txt"):
            self.filenames = glob.glob('*.txt')
            self.textouttxt()     

    def button3_clicked(self):  

        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        if(self.combovalue=="jpg"):
            self.filenames = tkFileDialog.askopenfilenames(filetypes= [("JPEG", ".jpg")], initialdir=iDir)
            self.textoutjpg()     
        if(self.combovalue=="txt"):
            self.filenames = tkFileDialog.askopenfilenames(filetypes= [("TEXT", ".txt") ], initialdir=iDir)
            self.textouttxt()     

    def button4_clicked(self):  
        self.textExample.delete("1.0",tkinter.END)

    def textoutjpg(self):  
        for file in self.filenames:
            self.textExample.insert(tkinter.END,file+"\n")

    def textouttxt(self):  
        for file in self.filenames:
            self.textExample.insert(tkinter.END,file+"\n")

            f = open(file, 'r')
            self.textExample.insert(tkinter.END,f.read()+"\n")
            f.close()

    def quit(self):
        root_main.destroy()

    def show_selected(self,event):       #eventを引数に
        self.combovalue=self.test_combobox.get()
        print(self.combovalue)  #選択した値を表示





root_main= tkinter.Tk()  
image_gui(root_main)  
root_main.title("ファイル名を出力するだけ")  
root_main.geometry("1200x600") 





root_main.mainloop()

