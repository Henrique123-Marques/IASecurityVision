#27C4B7 #28365D #161C2E #6699CC

from tkinter import *
import os
import qrcode, pyqrcode as pqr

#Configuracao da interface da página
helpWindows = Tk()
helpWindows.title("Ajuda")
helpWindows["bg"] = "#28365D"
helpWindows["background"] = "#28365D"
helpWindows.geometry("700x700+300+0")
iconH = PhotoImage(file = 'img/ICON_IASecurityVision.png')
helpWindows.iconphoto(False,iconH)
helpWindows.resizable(width = False, height = False)

#Textos da página
label1 = Label(helpWindows, text= "AJUDA", font=("Century Gothic", 20, ' bold '), fg = "#27C4B7", bg = "#28365D").place(x=310,y=10)
label2 = Label(helpWindows, text = "Problemas mais comuns:" , font=("Century Gothic", 12, ' bold '), fg = "#27C4B7", bg = "#28365D").place(x=250,y=65)
l2txt1 = Label(helpWindows, text = '1 - Verifique se o sistema possui câmeras instaladas no computador; \n\n 2 - Em caso de travamento, reinicie o programa; \n \n3 - Em caso de falha de reconhecimento, verifique as imagens \ntreinadas acessando a pasta de acesso restrito a fim de\n procurar a do morador respectivo.\n Assim, treine novamente o morador da residência \n com o seu respectivo ID; \n\n 4 - Em caso de acesso indevido das imagens dos usuários, \n entre em contato com pelo e-mail acessando o QrCode abaixo; \n\n 6 - Em caso de falha no programa, verifique se o Python \n está instalado juntamente com as bibliotecas necessárias; \n\n 7 - Em caso de falha no chatbot ou no banco de dados,\n entre em contato com por e-mail pelo QrCode abaixo.', bg = "#28365d", fg = "white", font=("Century Gothic", 12, ' bold ')).place(x = 90, y = 95)
label3 = Label(helpWindows, text = "ATENÇÃO: Apenas responderemos e-mails que sejam relacionados à problemas\n com o sistema.", fg = "#27C4B7", bg = "#28365D", font=("Century Gothic", 12, ' bold ')).place(x=40, y = 450)


#QRCode Gmail
code = pqr.create('https://www.google.com/gmail/')
code_aux = code.xbm(scale=3)
code_bpm = BitmapImage(data = code_aux)
code_bpm.config(foreground = '#28365D', background = 'white')
labelQr = Label(image=code_bpm)
labelQr.place(x=295, y = 515)
labelGmail = Label(helpWindows, text = "Acessar E-mail", fg = "#27c4b7", bg = "#28365D", font=("Century Gothic", 10, ' bold ')).place(x=307,y=650)

helpWindows.mainloop()