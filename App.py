from tkinter import * #importacao das bibliotecas
from tkinter import ttk
from tkinter.ttk import Progressbar
import os

windows = Tk() #inicializacao da janela
windows_width = 427
windows_height = 250
loading_width = windows.winfo_screenwidth()
loading_height = windows.winfo_screenheight()
x_cord =(loading_width/2)-(windows_width/2)
y_cord = (loading_height/2)-(windows_height/2)
windows.geometry("%dx%d+%d+%d"%(windows_width, windows_height,x_cord, y_cord))
windows.overrideredirect(1)

aux = ttk.Style()
aux.theme_use('clam')
aux.configure('red.Horizontal.TProgressbar', foreground = '#27C4B7', background = '#27C4B7')
progresso = Progressbar(windows, style = 'red.Horizontal.TProgressbar', orient = HORIZONTAL, length = 500, mode = 'determinate')

#Funcao de acesso ao aplicativo geral
def IASecurityVision():
	command = 'IASV.py'
	os.system(command)

#Funcao de carregamento
def bar():
	label = Label(windows, text = 'Carregando...', fg = '#27C4B7', bg = '#28365D', font = 'Poppins 10 bold').place(x = 18, y = 210)
	import time
	r = 0
	for i in range(100):
		progresso['value']=r
		windows.update_idletasks()
		time.sleep(0.03)
		r=r+1

	windows.destroy()
	IASecurityVision()
progresso.place(x=10,y=235)

#design da janela de carregamento
Frame(windows, width = 427, height = 241, bg = "#28365D").place(x=0,y=0)
button1 = Button(windows, width = 10, height = 1, text = "Iniciar", command = bar, border = 0, fg = "#28365D", bg = "#27C4B7", font = "Poppins 10 bold").place(x=170,y=200)
label1 = Label(windows, text = "I.A. SECURITY VISION", fg = '#27C4B7', bg = "#28365D", font = 'Poppins 18 bold').place(x = 150, y = 80)
logo = PhotoImage(file = "img/IASecurityVisionPNGVersion-150.png")
img = Label(windows, bg = '#28365D', image = logo).place(x = 0, y = 25)
windows.mainloop()
