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

        button4= Button(root_main, text=u'クリア', command=self.button4_clicked)  
        button4.grid(row=0, column=1)  
        button4.place(x=150, y=12) 

    def button1_clicked(self):  
        global combovalue

        global filenames
        ini_dir = 'C:'
        ret = tkinter.filedialog.askdirectory(initialdir=ini_dir, title='file dialog test', mustexist = True)
        print(str(ret))
        os.chdir(str(ret))
        if(combovalue=="jpg"):
            filenames = glob.glob('*.jpg')
            self.textoutjpg()     
        if(combovalue=="txt"):
            filenames = glob.glob('*.txt')
            self.textouttxt()     

    def button3_clicked(self):  
        global filenames

        fTyp = [('', '*')] 
        iDir = os.path.abspath(os.path.dirname(__file__)) 
        if(combovalue=="jpg"):
            filenames = tkFileDialog.askopenfilenames(filetypes= [("JPEG", ".jpg")], initialdir=iDir)
            self.textoutjpg()     
        if(combovalue=="txt"):
            filenames = tkFileDialog.askopenfilenames(filetypes= [("TEXT", ".txt") ], initialdir=iDir)
            self.textouttxt()     

    def button4_clicked(self):  
        textExample.delete("1.0",tkinter.END)

    def textoutjpg(self):  
        global filenames
        for file in filenames:
            textExample.insert(tkinter.END,file+"\n")

    def textouttxt(self):  
        global filenames
        for file in filenames:
            textExample.insert(tkinter.END,file+"\n")

            f = open(file, 'r')
            textExample.insert(tkinter.END,f.read()+"\n")
            f.close()

    def quit(self):
        root_main.destroy()


combovalue = "jpg"

def show_selected(event):       #eventを引数に
    global combovalue
    combovalue=test_combobox.get()
    print(combovalue)  #選択した値を表示



root_main= tkinter.Tk()  
image_gui(root_main)  
root_main.title("ファイル名を出力するだけ")  
root_main.geometry("1000x600") 

textExample=ScrolledText(root_main, height=35,width=120, wrap=tkinter.CHAR,bg="lightgreen")
textExample.pack()
textExample.place(x=90, y=70)

textExample.delete("1.0",tkinter.END)


item_list = ['jpg', 'txt']
test_combobox = ttk.Combobox(
    master=root_main,
    values=item_list,
    )

#値選択時に発生するイベントと関数を紐づけ
test_combobox.bind(
    '<<ComboboxSelected>>',     #選択時に発生するイベント
    show_selected,              #呼び出す関数
)

test_combobox.current(0)
test_combobox.pack()



root_main.mainloop()

