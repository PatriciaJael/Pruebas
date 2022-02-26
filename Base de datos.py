from msilib import Table
from tkinter import *
from tkinter import ttk
import tkinter as tk
import os
import cv2
import imutils
from PIL import ImageTk
import numpy as np
import sys
from PIL import Image, ImageTk


#Ventana
window = Tk()
#window.protocol("WM_DELETE_WINDOW", onClossing)
window.geometry('800x500')
window.title("Interfaz de adquisición de datos")

# def onClossing():
#     window.quit()
#     cap.release()
#     print("Cámara desconectada")
#     window.destroy()

# #Creación de pestañas
tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Formulario')
tab_control.add(tab2, text='Detección')

lbl1 = Label(tab1, text= 'label1')
lbl1.grid(column=0, row=0)
lbl2 = Label(tab2, text= 'label2')
lbl2.grid(column=0, row=0)
tab_control.pack(expand=1, fill='both')


#########Formulario de datos personales
lb1 = tk.Label( tab1, text="Código",fg="black", bg="ivory").place(x=10,y=50)
texto1 = tk.Entry(tab1, font=("Arial",15), width=10).place(x=120,y=50)

lb2 = tk.Label(tab1, text="Nombre",fg="black", bg="ivory").place(x=10,y=90)
texto2 = tk.Entry(tab1, font=("Arial",15), width=10).place(x=120,y=90)

lb3 = tk.Label( tab1, text="Apellido",fg="black", bg="ivory").place(x=10,y=130)
texto3 = tk.Entry(tab1, font=("Arial",15), width=10).place(x=120,y=130)

lb4 = tk.Label( tab1, text="Edad",fg="black", bg="ivory").place(x=10,y=170)
texto4 = tk.Entry(tab1, font=("Arial",15), width=10).place(x=120,y=170)

lb5 = tk.Label( tab1, text="Condición médica",fg="black", bg="ivory").place(x=10,y=210)
texto5 = tk.Entry(tab1, font=("Arial",15), width=10).place(x=120,y=210)

lb6 = tk.Label( tab1, text="Sexo",fg="black", bg="ivory").place(x=10,y=250)
texto6 = tk.Entry(tab1, font=("Arial",15), width=10).place(x=120,y=250)


########Crear datos e insertar datos
#class Tabla:
#    def __init__(self, root):
#       for a in range(total_rows):
#           for b in range(total_columns):
#                self.e = Entry(root, width=20, fg='blue', font=('Arial', 16, 'bold'))
#                self.e.grid(row=a, column=b)
#               self.e.insert(END, lst[a][b])

#lst =[(texto1, texto2, texto3,texto4, texto5, texto6)]

#total_rows= len(lst)
#total_columns= len(lst[0])
#t = Table(window)





#########Creación de botones
boton = tk.Button(tab1, text="Guardar").place(width=60,x=120,y=300)


#####Captura de imagen
def onClossing():
    window.quit()
    cap.release()
    print("Cámara desconectada")
    window.destroy()

def callback():
    # cap.open(url)
    ret, frame = cap.read()

    if ret:
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img.thumbnail((400, 400))
        tkimage = ImageTk.PhotoImage(img)
        label5.configure(image=tkimage)
        label5.image = tkimage
        window.after(1, callback)
    else:
        onClossing()

cap = cv2.VideoCapture(0)
if cap.isOpened():
    print("Cámara inicializada")
else:
    sys.exit("Cámara desconectada")

window.protocol("WM_DELETE_WINDOW", onClossing)

label5 = Label(tab2)
label5.grid(column=3, row=3)


window.after(1, callback)



####Cierre de ventana
window.mainloop()
