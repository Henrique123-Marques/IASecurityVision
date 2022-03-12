from tkinter import *
from datetime import datetime
from time import strftime

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

        self.buttonA = Button(self.opcoes, text="Pesquisa", font=("Century Gothic", 11, 'bold'), command=self.clickA, bg="#28365D", fg="white")
        self.buttonB = Button(self.opcoes, text="Lista dos usuários", font=("Century Gothic", 11, 'bold'), command=self.clickB, bg="#28365D", fg="white")
        self.buttonC = Button(self.opcoes, text="Adicionar usuários", font=("Century Gothic", 11, 'bold'), command=self.clickC, bg="#28365D", fg="white")
        self.buttonD = Button(self.opcoes, text="Remover usuários", font=("Century Gothic", 11, 'bold'), command=self.clickD, bg="#28365D", fg="white")
        self.buttonE = Button(self.opcoes, text="Limpar mensagens", font=("Century Gothic", 11, 'bold'), command=self.clickE, bg="#28365D", fg="white")
        self.buttonQUIT = Button(self.opcoes, text="Fechar chatbot", command=self.root.destroy, font=("Century Gothic", 11, 'bold'), bg="#5d2828", fg="white")

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
        self.chat.configure(state=DISABLED)
    def clickB(self):
        msg = "Você clicou em Lista dos usuários"
        self.chat.configure(state=NORMAL)
        self.chat.insert(END, msg + '\n')
        self.chat.configure(state=DISABLED)
    def clickC(self):
        msg = "Você clicou em Adicionar usuários"
        self.chat.configure(state=NORMAL)
        self.chat.insert(END, msg + '\n')
        self.chat.configure(state=DISABLED)
    def clickD(self):
        msg = "Você clicou em Remover usuários"
        self.chat.configure(state=NORMAL)
        self.chat.insert(END, msg + '\n')
        self.chat.configure(state=DISABLED)
    def clickE(self):
        self.chat.configure(state=NORMAL)
        self.chat.delete("1.0", END)
        self.chat.configure(state=DISABLED)

app = Chatbotapp()