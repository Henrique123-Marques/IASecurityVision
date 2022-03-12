import tkinter as tk #importacao das bibliotecas
from tkinter import Message ,Text
import cv2,os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk 
import tkinter.font as font

treinamento = tk.Tk()
treinamento.title("Reconhecimento")
dialog_title = 'SAIR'
dialog_text = ''
treinamento.configure(background='#28365D')
treinamento.geometry('800x600+250+50')
treinamento.resizable(width=False, height=False)
icon = tk.PhotoImage(file = 'img/ICON_IASecurityVision.png') #icone do aplicativo
treinamento.iconphoto(False,icon)

titulo = tk.Label(treinamento, text="Reconhecimento", font=("Century Gothic", 15, 'bold'), bg="#28365D", fg="#27C4B7")
titulo.place(relwidth=1, y=20)

linha = tk.Label(treinamento, bg="#2cc4b3")
linha.place(relwidth=1, relheight=0.012, y=60)

lbl = tk.Label(treinamento, text="Entre com o ID : ", width=20, height=2, fg="#27C4B7", bg="#28365D", font=("Century Gothic", 14, ' bold ')) 
lbl.place(x=12, y=100)

txt = tk.Entry(treinamento, width=41,  bg="white" ,fg = "#28365d",font=('Helvetica', 14))
txt.place(x=260, y=110)

lbl2 = tk.Label(treinamento, text="Entre com o Nome : ", width=20, fg="#27C4B7", bg="#28365D", height=2 ,font=("Century Gothic", 14, ' bold ')) 
lbl2.place(x=30, y=180)

txt2 = tk.Entry(treinamento,width=41, bg="white", fg="#28365D", font=('Helvetica', 14))
txt2.place(x=260, y=190)

lbl3 = tk.Label(treinamento, text="Notificação : ", width=20, fg="#27C4B7"  ,bg="#28365D"  ,height=2 ,font=("Century Gothic", 14, ' bold ')) 
lbl3.place(x=3, y=260)

message = tk.Label(treinamento, text="" ,bg="#28365d", fg="#27C4B7"  ,width=41  ,height=1, activebackground = "#28365D" ,font=('Helvetica', 14)) 
message.place(x=260, y=270)

lbl3 = tk.Label(treinamento, text="Registro : ",width=20, fg="#27C4B7"  ,bg="#28365D"  ,height=2 ,font=("Century Gothic", 15, ' bold ')) 
lbl3.place(x=30, y=480)

message2 = tk.Label(treinamento, text="" ,fg="#27C4B7", bg="#28365d",activeforeground = "#28365D",width=41  ,height=2  ,font=('Helvetica', 14)) 
message2.place(x=260, y=480)
      
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False
 
def Analisar():        
    Id=(txt.get())
    name=(txt2.get())
    if(is_number(Id) and name.isalpha()):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector=cv2.CascadeClassifier(harcascadePath)
        sampleNum=0
        while(True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(183,196,39),2)        
               
                sampleNum=sampleNum+1
                
                cv2.imwrite("ImagensTreinadas\ "+name +"."+Id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
                
                cv2.imshow('frame',img)
             
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            
            elif sampleNum>60:
                break
        cam.release()
        cv2.destroyAllWindows() 
        res = "Imagem salva com o ID : " + Id +" Name : "+ name
        row = [Id , name]
        with open('Nomes\StudentDetails.csv','a+') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow(row)
        csvFile.close()
        message.configure(text= res)
    else:
        if(is_number(Id)):
            res = "Entre com o Nome novamente"
            message.configure(text= res)
        if(name.isalpha()):
            res = "Entre com o Id"
            message.configure(text= res)
    
def TrainImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    harcascadePath = "haarcascade_frontalface_default.xml"
    detector =cv2.CascadeClassifier(harcascadePath)
    faces,Id = getImagesAndLabels("ImagensTreinadas")
    recognizer.train(faces, np.array(Id))
    recognizer.save("Trainner\Trainner.json")
    res = "Imagem Treinada"
    message.configure(text= res)

def getImagesAndLabels(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    faces=[]
    Ids=[]
    for imagePath in imagePaths:
        pilImage=Image.open(imagePath).convert('L')
        imageNp=np.array(pilImage,'uint8')
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(imageNp)
        Ids.append(Id)        
    return faces,Ids

def TrackImages():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("Trainner\Trainner.json")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);    
    df=pd.read_csv("Nomes\StudentDetails.csv")
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX        
    col_names =  ['Id','Name','Date','Time']
    attendance = pd.DataFrame(columns = col_names)    
    while True:
        ret, im =cam.read()
        gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
        faces=faceCascade.detectMultiScale(gray, 1.2,5)    
        for(x,y,w,h) in faces:
            cv2.rectangle(im,(x,y),(x+w,y+h),(183,196,39),2)
            Id, conf = recognizer.predict(gray[y:y+h,x:x+w])                                   
            if(conf < 50):
                ts = time.time()      
                date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                aa=df.loc[df['Id'] == Id]['Name'].values
                tt=str(Id)+"-"+aa
                attendance.loc[len(attendance)] = [Id,aa,date,timeStamp]
                
            else:
                Id='Desconhecido'                
                tt=str(Id)  
            if(conf > 75):
                noOfFile=len(os.listdir("Desconhecidos"))+1
                cv2.imwrite("Desconhecidos\Image"+str(noOfFile) + ".jpg", im[y:y+h,x:x+w])            
            cv2.putText(im,str(tt),(x,y+h), font, 1,(183,196,39),2)        
        attendance=attendance.drop_duplicates(subset=['Id'],keep='first')    
        cv2.imshow('im',im) 
        if (cv2.waitKey(1)==ord('q')):
            break
    ts = time.time()      
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
    Hour,Minute,Second=timeStamp.split(":")
    fileName="Registro\Registro_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
    attendance.to_csv(fileName,index=False)
    cam.release()
    cv2.destroyAllWindows()
    res=attendance
    message2.configure(text= res)
  
takeImg = tk.Button(treinamento, text="Analisar Imagem", command=Analisar  ,fg="#161C2E"  ,bg="#27C4B7"  ,width=15  ,height=1, activebackground = "#27C4B7" ,font=("Century Gothic", 14, ' bold '))
takeImg.place(x=50, y=380)
trainImg = tk.Button(treinamento, text="Treinar Imagem", command=TrainImages  ,fg="#161C2E"  ,bg="#27C4B7"  ,width=15  ,height=1, activebackground = "#27C4B7" ,font=("Century Gothic", 14, ' bold '))
trainImg.place(x=300, y=380)
trackImg = tk.Button(treinamento, text="Reconhecer", command=TrackImages  ,fg="#161C2E"  ,bg="#27C4B7"  ,width=15  ,height=1, activebackground = "#27C4B7" ,font=("Century Gothic", 14, ' bold '))
trackImg.place(x=550, y=380)

treinamento.mainloop()