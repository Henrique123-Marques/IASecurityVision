#27C4B7 #28365D #161C2E #6699CC

from genericpath import exists
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox as mess
import csv
from ttkbootstrap import Style
from PIL import ImageTk
from PIL import Image
from functools import partial
from os import listdir
from configparser import ConfigParser
import requests, qrcode, png, io, imutils, cv2, os, numpy, pyqrcode as pqr
import pandas as pd
import matplotlib.pyplot as plt 

w = Tk()
w.geometry('800x200+200+100')
w['background'] = '#28365D'
w.title('Análise de dados')
w.resizable(width = False, height = False)
icon = PhotoImage(file = 'img/ICON_IASecurityVision.png') 
w.iconphoto(False,icon)

def g1():
    commandg1 = '1WaffleGraphic.py'
    os.system(commandg1)

def g2():
    commandg2 = '2PizzaGraphic.py'
    os.system(commandg2)

def g3():
    commandg3 = '3BarraGraphic.py'
    os.system(commandg3)

def g4():
    commandg4 = '4PizzaGraphic.py'
    os.system(commandg4)


l1 = Label(w, text = 'Selecione o gráfico que deseje ver:', font=("Century Gothic", 20, ' bold ',), 
    fg = '#27c4b7', bg = '#28365d').place(x=160, y = 10)


#Primeiro Grafico
IMGb1 = PhotoImage(file = "img/WaffleGraphic.png")
label1 =  Label(w, text="", image = IMGb1, bg = "#28365d").place(x=130, y = 50)
b1 = Button(w, text  = '1º Gráfico', font=("Century Gothic", 10, ' bold ',), 
    fg = '#28365d', bg = '#27c4b7', bd = 1, activebackground = "#27c4b7", command = g1).place(x = 145, y = 150)

#Segundo Grafico
IMGb2 = PhotoImage(file = 'img/PizzaGraphic.png')
labelB2 = Label(w, text = '', image = IMGb2, bg = '#28365d').place(x = 287, y = 50)
b2 = Button(w, text = '2º Gráfico', font=("Century Gothic", 10, ' bold ',), 
    fg = '#28365d', bg = '#27c4b7', bd = 1, command = g2, activebackground = "#27c4b7").place(x = 297, y = 150)

#Terceiro grafico (PIZZA)
IMGb3 = PhotoImage(file = 'img/BarraGraphic.png')
labelB3 = Label(w, text = '', image = IMGb3, bg = '#28365d').place(x = 435, y = 57)
b3 = Button(w, text = '3º Gráfico', font=("Century Gothic", 10, ' bold ',), 
    fg = '#28365d', bg = '#27c4b7', bd = 1, command = g3, activebackground = '#27c4b7').place(x = 445, y = 150)

#Quarto Gráfico
IMGb4 = PhotoImage(file = 'img/PizzaGraphic.png')
labelB4 = Label(w, text = '', image = IMGb4, bg = "#28365d").place(x = 580, y = 50)
b4 = Button(w, text = '4° Gráfico', font=("Century Gothic", 10, ' bold ',), 
    fg = '#28365d', bg = '#27c4b7', bd = 1, command = g4, activebackground = "#27c4b7").place(x = 593, y = 150)

w.mainloop()



