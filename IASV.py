#27C4B7 #28365D #161C2E #6699CC
from genericpath import exists
from tkinter import * 
from tkinter import ttk
from tkinter import messagebox as mess
from ttkbootstrap import Style
from PIL import ImageTk 
from PIL import Image
from functools import partial
from os import listdir
from ttkbootstrap import Style
from datetime import datetime
from time import strftime
from configparser import ConfigParser
import requests, qrcode, png, io, imutils, cv2, os, numpy, pyqrcode as pqr
import pandas as pd
import csv, glob, easygui, webbrowser

style = Style('superhero')
windows = style.master

windows.title("I.A. Security Vision")
windows["bg"] = "#28365D" 
windows["background"] = "#28365D" 
windows.geometry("1325x700+0+0") 
windows.resizable(width = False, height = False)
icon = PhotoImage(file = 'img/ICON_IASecurityVision.png') 
windows.iconphoto(False,icon)

#ABAS
aba = ttk.Notebook(windows)
aba.place(x=0, y=0, width = 3000, height = 3000)

inicio = Frame(aba)
inicio.configure(bg = "#28365D")

iaSecurity = Frame(aba)
iaSecurity.configure(bg = "#28365D")

seguranca = Frame(aba)
seguranca.configure(bg = "#28365D")

data = Frame(aba)
data.configure(bg = "#28365D")

contato = Frame(aba)
contato.configure(bg = "#28365D")

aba.add(inicio, text = "Início")
aba.add(iaSecurity, text = "I.A. Security Vision")
aba.add(seguranca, text = "Segurança")
aba.add(data, text = "Análise de Dados")
aba.add(contato, text = "Contato")

#Conteúdo da página Início
lb = Label(inicio, text="I.A Security Vision", bg="#28365D", fg="#27C4B7", 
font="Verdana 20 bold italic").place(x=1000,y=1000) #posição das janelas
lb1a = Label(inicio, text = "I.A. SECURITY VISION", bg="#28365D", font=("Century Gothic", 25, ' bold '), fg = "#27C4B7").place(x = 180, y = 310)
lb1b = Label(inicio, text = "O reconhecimento facial a seu favor!", 
    bg = "#28365D", fg = "#27C4B7", font=("Century Gothic", 15, ' bold ')).place(x = 160, y = 360)
img = PhotoImage(file="img/IASecurityVisionPNGVersion-250.png")
img1 = Label(inicio, image = img, bg = "#28365D").place(x=210, y=55)
LabelAuxInicio = Label(inicio, bg = "#161C2E", width = 10, height = 100).place(x = 0, y = 0)
logoAuxInicio = PhotoImage(file = "img/IASecurityVisionPNGVersion-70.png")
logoLabelAuxIASV = Label(inicio, bg = "#161C2E", image = logoAuxInicio).place(x = 5, y = 35)
imgPag1aux = PhotoImage(file = "img/sala.png")
imgPag1 = Label(inicio, image = imgPag1aux, bg = "#28365D").place(x = 622, y = -10)

#Relógio digital
n1 = datetime.today().strftime('%A')
n2 = (n1.upper())
n3 = (n2[0:2])

dateFrame = Frame(windows, width = 380, height = 200, bg = '#28365d')
dateFrame.place(x = 105, y = 500)

def tempo():
    n1 = strftime('%H : %M : %S')
    DateLabel.config(text = n1)
    DateLabel.after(1000, tempo)

DateLabel = Label(dateFrame, font=("Century Gothic", 40, ' bold '), bg = '#28365D', foreground = '#27C4B7')
DateLabel.place(x=105,y=70)
tempo()

def labels(): 
    DateLabel4 = Label(dateFrame, font=("Century Gothic", 8, ' bold '), bg = "#28365D", fg = '#27C4B7', text = 'HORAS')
    DateLabel4.place(x=120,y=140)

    DateLabel5 = Label(dateFrame, font=("Century Gothic", 8, ' bold '), bg = "#28365D", fg = '#27C4B7', text = 'MINUTOS')
    DateLabel5.place(x=215,y=140)

    DateLabel3 = Label(dateFrame, font=("Century Gothic", 8, ' bold '), bg = "#28365D", fg = '#27C4B7', text = 'SEGUNDOS')
    DateLabel3.place(x=315,y=140)
labels()

#Conteúdo da página I.A. Security Vision
lb2 = Label(iaSecurity, text="I.A Security Vision", bg="#28365D", font=("Century Gothic", 20, ' bold '), fg = "#27C4B7").place(x=220,y=50) #posição das janelas
lb2a = Label(iaSecurity, text = "O aplicativo de reconhecimento facial\n I.A. Security Vision foi feito para auxiliar os usuários \nque vivem em apartamentos e condomínios, incluindo \num chatbot de interação que pode auxilia-los. \nSua finalidade é aumentar a segurança com uso \ndo reconhecimento facial dos indivíduos \ncadastrados, com uso de imagens e banco de dados.", 
    bg = "#28365D", fg = "#27C4B7", font=("Century Gothic", 12, ' bold ')).place(x = 120, y = 150)
LabelAuxISAV = Label(iaSecurity, bg = "#161C2E", width = 10, height = 100).place(x = 0, y = 0)
logoAuxIASV = PhotoImage(file = "img/IASecurityVisionPNGVersion-70.png")
logoLabelAuxIASV = Label(iaSecurity, bg = "#161C2E", image = logoAuxIASV).place(x = 5, y = 35)
imgPag2aux = PhotoImage(file = "img/r2.png")
imgPag2 = Label(iaSecurity, image = imgPag2aux, bg = "#28365D").place(x = 622, y = -10)

#Conteúdo da página Segurança
lb3 = Label(seguranca, text = "Segurança", bg="#28365D", font=("Century Gothic", 20, ' bold '), fg = "#27C4B7").place(x=275, y=50)
lb3a = Label(seguranca, text = "Com a Inteligência Artificial em crescimento, \ndecidimos usar dessa\n mesma tecnologia para fins de segurança\n a sua pessoa, principalmente em residências \ncompartilhadas como os apartamentos e condomínios. \nRessaltamos o uso da I.A. (Inteligência Artificial), \n no reconhecimento facial para assegurar\n uma melhor experiência com essa\n tecnologia e uso para facilitação de processos. ", 
    bg = "#28365D", fg = "#27C4B7", font=("Century Gothic", 12, ' bold ')).place(x=140,y=150)
LabelAuxSEG = Label(seguranca, bg = "#161C2E", width = 10, height = 100).place(x = 0, y = 0)
logoAuxSEG = PhotoImage(file = "img/IASecurityVisionPNGVersion-70.png")
logoLabelAuxSEG = Label(seguranca, bg = "#161C2E", image = logoAuxSEG).place(x = 5, y = 35)
imgPag3aux = PhotoImage(file = "img/r3.png")
imgPag3 = Label(seguranca, image = imgPag3aux, bg = "#28365D").place(x = 622, y = -10)

#Conteúdo da Página Análise de dados
lb2 = Label(data, text="Análise de Dados", bg="#28365D", font=("Century Gothic", 20, ' bold '), fg = "#27C4B7").place(x=230,y=50) #posição das janelas
lb2a = Label(data, text = "A opção DataAnalytics (Análise de dados) presente \n nesse aplicativo se refere aos resultados de uma pesquisa \n realizada pelos próprios desenvolvedores, com o intuito de\n sabermos o cenário quanto ao uso da tecnologia\n de reconhecimento facial e de suas opiniões sobre.", 
    bg = "#28365D", fg = "#27C4B7", font=("Century Gothic", 12, ' bold ')).place(x = 120, y = 150)
LabelAuxDATA = Label(data, bg = "#161C2E", width = 10, height = 100).place(x = 0, y = 0)
logoAuxDATA = PhotoImage(file = "img/IASecurityVisionPNGVersion-70.png")
logoLabelAuxDATA = Label(data, bg = "#161C2E", image = logoAuxDATA).place(x = 5, y = 35)
imgPagDATAaux = PhotoImage(file = "img/cozinha.png")
imgPag2 = Label(data, image = imgPagDATAaux, bg = "#28365D").place(x = 622, y = -10)

#Conteúdo da página Contato
lb5 = Label(contato, text="Contato", bg="#28365D", font=("Century Gothic", 20, ' bold '), fg = "#27C4B7").place(x=280, y =50)
IconEmail =PhotoImage(file = "img/Email (1).png")
emailIcon = Label(contato, image = IconEmail, bg = "#28365D").place(x = 70, y = 168)
IconEmail2 =PhotoImage(file = "img/Email (1) - Copia.png")
emailIcon2 = Label(contato, width= 30, height=30, image = IconEmail2, bg = "#28365D").place(x = 105, y = 240)
lb5a = Label(contato, text="Entre em contato com os seguintes meios:", 
bg="#28365D", font="Poppins 15 bold", fg = "#27C4B7").place(x=100, y=150)
lb5c = Label(contato, text="E-mail: henriquemarquessantossilva@hotmail.com", bg="#28365D", 
fg="#27C4B7", font=("Century Gothic", 10, 'bold')).place(x=150, y=245)
LabelAuxCONT = Label(contato, bg = "#161C2E", width = 10, height = 100).place(x = 0, y = 0)
logoAuxCONT = PhotoImage(file = "img/IASecurityVisionPNGVersion-70.png")
logoLabelAux2 = Label(contato, bg = "#161C2E", image = logoAuxCONT).place(x = 5, y = 35)
imgPag4aux = PhotoImage(file = "img/r1.png")
imgPag4 = Label(contato, image = imgPag4aux, bg = "#28365D").place(x = 622, y = -10)

#Gerando QRCode
code = pqr.create('http://iasecurityvision.000webhostapp.com/')
code_aux = code.xbm(scale=3)
#qrButton = Button(text = '', bd = 10, bg = "#28365D", fg = "#28365D", width = 10, height = 5).place(x = 1145, y = 775)
code_bpm = BitmapImage(data = code_aux)
code_bpm.config(foreground = '#28365D', background = 'white')

labelQr = Label(image=code_bpm)
labelQr.place(x=280, y = 430)


textQR = Label(windows, text = 'Acesse nosso site!', bg = '#28365D', fg = '#27C4B7', 
font=("Century Gothic", 10, ' bold ')).place(x = 420, y = 500)

def cameraIA(): #CAMERA
    command = 'reconhecimento.py'
    os.system(command)    

def solicitar():
    commandSolicitar = 'solicitacao.pdf'
    os.system(commandSolicitar) 

def chatbot(): #CHATBOT - APLICATIVO GERAL  
    class Chatbotapp:
    
        def __init__(self):
            self.root = Tk()
            self.principal()
            self.root.mainloop()

        def principal(self):    
            self.root.title("Chatbot")  
            self.root.geometry("800x600")
            self.root.configure(background='#28365D')
            self.root.resizable(width=False, height=False)
            self.root.iconbitmap('img/icon.ico')

            self.titulo = Label(self.root, text="Chatbot de suporte", font=("Century Gothic", 14, 'bold'), pady=10, bg="#28365D", fg="white")
            self.titulo.place(relwidth=1)
            self.linha = Label(self.root, width=450, bg="#2cc4b3")
            self.linha.place(relwidth=1, rely=0.07, relheight=0.012)
            self.opcoes = Label(self.root, bg="#2cc4b3", height=100)
            self.opcoes.place(relwidth=1, rely=0.75)
            self.chat = Text(self.root, width=20, height=2, bg="#28365D", fg="white", padx=5, pady=5)
            self.chat.place(relwidth=1, rely=0.08, relheight=0.67)
            self.chat.configure(cursor="arrow", state=DISABLED)

            self.relogio = Label(self.titulo, font=("Century Gothic", 13, 'bold'), bg="#28365D", pady=10, fg="white")
            self.relogio.place(relwidth=0.15)
            self.horario()

            self.buttonA = Button(self.opcoes, text="Pesquisa", font=("Century Gothic", 11, 'bold'), command=self.clickA, bg="#28365D", fg="white", bd = 1)
            self.buttonB = Button(self.opcoes, text="Lista dos usuários", font=("Century Gothic", 11, 'bold'), command=self.clickB, bg="#28365D", fg="white", bd = 1)
            self.buttonC = Button(self.opcoes, text="Site do projeto", font=("Century Gothic", 11, 'bold'), command=self.clickC, bg="#28365D", fg="white", bd = 1)
            self.buttonD = Button(self.opcoes, text="Iniciar reconhecimento facial", font=("Century Gothic", 11, 'bold'), command=self.clickD, bg="#28365D", fg="white", bd = 1)
            self.buttonE = Button(self.opcoes, text="Limpar mensagens", font=("Century Gothic", 11, 'bold'), command=self.clickE, bg="#28365D", fg="white", bd = 1)
            self.buttonQUIT = Button(self.opcoes, text="Fechar chatbot", command=self.root.destroy, font=("Century Gothic", 11, 'bold'), bg="#5d2828", fg="white", bd = 1)

            self.buttonA.place(relwidth=0.3, relheight=0.03, rely=0.008)
            self.buttonB.place(relwidth=0.3, relheight=0.03, rely=0.05)
            self.buttonC.place(relwidth=0.3, relheight=0.03, rely=0.008, relx=0.35)
            self.buttonD.place(relwidth=0.3, relheight=0.03, rely=0.05, relx=0.35)
            self.buttonE.place(relwidth=0.3, relheight=0.03, rely=0.008, relx=0.7)
            self.buttonQUIT.place(relwidth=0.3, relheight=0.03, rely=0.05, relx=0.7)

            self.scroll = Scrollbar(self.chat)
            self.scroll.place(relheight=1, relx=0.985, rely=0)
            self.scroll.configure(command=self.chat.yview)
            self.chat['yscrollcommand'] = self.scroll.set

        def horario(self):
            hor=strftime('%H : %M : %S')
            self.relogio.config(text=hor)
            self.relogio.after(1000,self.horario)

        def clickA(self):
            msg = "Você clicou em Pesquisa"
            self.chat.configure(state=NORMAL)
            self.chat.insert(END, msg + '\n')
            list_of_files = glob.glob('Registro\*') 
            latest_file = max(list_of_files, key=os.path.getctime) 
            myvar = easygui.enterbox("Digite o nome do usuário que você procura")
            myvar = ("['"+myvar+"']")   
            f=open(latest_file)
            reader=csv.reader(f)
            found = "Nome não encontrado no sistema, verifique a digitação e tente novamente."
            for row in reader:
                if myvar in row:
                    found = (" ".join(row))
            self.chat.insert(END, found + '\n')
            self.chat.configure(state=DISABLED)
        def clickB(self):
            msg = "Você clicou em Lista dos usuários. Apresentando agora a lista de usuários:"
            self.chat.configure(state=NORMAL)
            self.chat.insert(END, msg + '\n')            
            list_of_files = glob.glob('Registro\*') 
            latest_file = max(list_of_files, key=os.path.getctime)            
            df  = pd.read_csv(latest_file)
            msg = str(df)
            self.chat.insert(END, msg + '\n')
            self.chat.configure(state=DISABLED)
        def clickC(self):
            msg = "Você clicou em site do projeto, você será redirecionado de acordo com seu navegador padrão"
            self.chat.configure(state=NORMAL)
            self.chat.insert(END, msg + '\n')
            webbrowser.open('http://iasecurityvision.000webhostapp.com/')
            self.chat.configure(state=DISABLED)
        def clickD(self):
            msg = "Você iniciou o reconhecimento facial."
            self.chat.configure(state=NORMAL)
            self.chat.insert(END, msg + '\n')
            command2 = 'reconhecimento.py'
            os.system(command2)  
            self.chat.configure(state=DISABLED)
        def clickE(self):
            self.chat.configure(state=NORMAL)
            self.chat.delete("1.0", END)
            self.chat.configure(state=DISABLED)

    app = Chatbotapp()


#funcao dataanalytics
def data(): 
    command = 'data.py'
    os.system(command)

#funcao help
def help():
    commandHelp = 'help.py'
    os.system(commandHelp)
    
#Botao da camera
cameraImg = ImageTk.PhotoImage(file = "img/camera_ICON_45x50.png")
camera = Button(text = "", bg = "#28365D", fg = "#28365D", command = cameraIA, bd = 0, activebackground = "#28365D")
camera.configure(image=cameraImg, highlightthickness = 0, bd = 0)
camera.place(x=22,y=185)
cameraTxt = Button(text = "Reconhecimento", bg = "#161C2E", fg = "#27C4B7", font=("Century Gothic", 7, ' bold '), command = cameraIA, bd = 0).place(x = 6, y = 230)

#Botão de solicitar acesso a imagem
Icon5 = PhotoImage(file = 'img/Icon5.png')
Icon5Aux = Button(bd = 0, activebackground = "#28365D", bg = '#161C2E', command = solicitar)
Icon5Aux.configure(image = Icon5, highlightthickness = 0, bd = 0, bg = "#161C2E")
Icon5Aux.place(x = 10, y= 270)
Icon5Text = Label(text = "Solicitação", bg = "#161C2E", fg = "#27C4B7", font=("Century Gothic", 7, ' bold '), bd = 0).place(x = 20, y = 330)

#Botão do chatbot
ChatImg = ImageTk.PhotoImage(file = "img/chat_ICON_45x50.png")
chat = Button(text = "", bg = "#161C2E", fg = "#27C4B7", command = chatbot, bd = 0, activebackground = "#161C2E")
chat.configure(image = ChatImg, highlightthickness = 0, bd = 0)
chat.place(x = 22, y = 375)
chatTxt = Button(text = "Chatbot", bg = "#161C2E", fg = "#27C4B7", font=("Century Gothic", 7, ' bold '), command = chatbot, bd = 0).place(x = 25, y = 425)

#Botao de dados (gráficos, análise etc...)
bdImg = ImageTk.PhotoImage(file = "img/bd_ICON_45x50.png")
bd = Button(text="", bg = "#161C2E", fg = "#161C2E", bd = 0, command = data, activebackground = "#28365D")
bd.configure(image=bdImg, highlightthickness = 0, bd = 0) 
bd.place(x = 22, y = 465)
bdTxt = Button(text = "DataAnalytics", bg = "#161C2E", fg = "#27C4B7", font=("Century Gothic", 7, ' bold '), bd = 0).place(x = 13, y = 515)

#Botão de ajuda aos usuários  
helpImg = PhotoImage(file = "img/Help_65.png") 
helpAux = Button(text = "", bg = "#161C2E", fg = "#161C2E", bd = 0, command= help, activebackground = "#28365D")
helpAux.place(x = 22, y = 550)
helpAux.configure(image = helpImg, highlightthickness = 0, bd = 0)
helpTxt = Label(text = "Ajuda", bg = "#161C2E", fg = "#27C4B7", font = ("Century Gothic", 7, ' bold '), bd = 0).place(x = 33, y = 596)

sairImg = PhotoImage(file = "img/Sair_25.png")
sairAux = Button(command = windows.destroy, bd = 0, bg = "#161C2E", activebackground = "#28365D")
sairAux.place(x = 33, y = 645)
sairAux.configure(image = sairImg, highlightthickness = 0, bd = 0, bg = "#161C2E")
sairTxt = Label(text = "Sair", bg = "#161C2E", fg = "#27C4B7", font=("Century Gothic", 7, ' bold '), bd = 0).place(x = 36, y = 675)

line = Label(text = "____________", bg = "#161C2E", fg = "#27C4B7", font=("Century Gothic", 10, ' bold '), bd  = 0).place(x = 2, y = 145)
line2 = Label(text = "____________", bg = "#161C2E", fg = "#27C4B7", font=("Century Gothic", 10, ' bold '), bd  = 0).place(x = 2, y = 610)

windows.mainloop() #carregamento da página