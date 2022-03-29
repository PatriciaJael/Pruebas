from tkinter import *
from tkinter import ttk
import tkinter as tk
import cv2
import imutils
from PIL import Image, ImageTk
import os
# import csv
# import pandas as pd
# from pandastable import Table, TableModel
# Ventana ------------------------------------------------------------------------------------------
window = Tk()
window.geometry('900x600+50+50')
window.title("Interfaz de adquisición de datos")
# window.configure(bg='PeachPuff4')
window.resizable(False, False)   # evita que la ventana se maximice
# window.iconbitmap('./icono_pr.ico') ### cambia el icono de la interfaz
window.attributes('-topmost', 1)
window.lift()

# Login ------------------------

# Creación de pestañas ----------------------------------------------
tab_control = ttk.Notebook(window)   # panel para las pestañas
tab_control.pack(fill='both', expand=True)

tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Formulario')
tab_control.add(tab2, text='Base de Datos')

# Formulario de datos personales -------------------------------------
lbCod = tk.Label(tab1, text="Código", fg="black", bg="ivory", font="Arial")
lbCod.grid(column=0, row=0, padx=5, pady=5)
textCod = tk.Entry(tab1, font=("Arial", 12), width=15)
textCod.focus()
textCod.grid(column=1, row=0, padx=5, pady=5)

lbName = tk.Label(tab1, text="Nombre", fg="black", bg="ivory", font="Arial")
lbName.grid(column=0, row=1, padx=15, pady=15)
textName = tk.Entry(tab1, font=("Arial", 12), width=15)
textName.grid(column=1, row=1, padx=15, pady=15)

lbLAp = tk.Label(tab1, text="Apellido", fg="black", bg="ivory", font="Arial")
lbLAp.grid(column=0, row=2, padx=5, pady=5)
textAp = tk.Entry(tab1, font=("Arial", 12), width=15)
textAp.grid(column=1, row=2, padx=5, pady=5)

lbAge = tk.Label(tab1, text="Edad", fg="black", bg="ivory", font="Arial")
lbAge.grid(column=0, row=3, padx=15, pady=15)
textAge = tk.Entry(tab1, font=("Arial", 12), width=15)
textAge.grid(column=1, row=3, padx=15, pady=15)

lbCond = tk.Label(tab1, text="Condición médica", fg="black", bg="ivory", font="Arial")
lbCond.grid(column=0, row=4, padx=5, pady=5)
textCond = tk.Entry(tab1, font=("Arial", 12), width=15)
textCond.grid(column=1, row=4, padx=5, pady=5)

lbSex = tk.Label(tab1, text="Sexo", fg="black", bg="ivory", font="Arial")
lbSex.grid(column=0, row=5, padx=15, pady=15)
textSex = tk.Entry(tab1, font=("Arial", 12), width=15)
textSex.grid(column=1, row=5, padx=15, pady=15)


# Crear datos e insertar datos -------------------
Tabla = ttk.Treeview(tab2, height=20, columns=("#0", "#1", "#2", "#3", "#4", "#5"))
Tabla.grid(row=0, column=1)

Tabla.heading("#0", text="", anchor=CENTER)
Tabla.column("#0", width=0, stretch=NO)

Tabla.heading("#1", text="Cód")
Tabla.column("#1", width=50, anchor=CENTER)

Tabla.heading("#2", text="Nombre")
Tabla.column("#2", width=200, anchor=CENTER)

Tabla.heading("#3", text="Apellido")
Tabla.column("#3", width=200, anchor=CENTER)

Tabla.heading("#4", text="Edad")
Tabla.column("#4", width=70, anchor=CENTER)

Tabla.heading("#5", text="Condición médica")
Tabla.column("#5", width=120, anchor=CENTER)

Tabla.heading("#6", text="Sexo")
Tabla.column("#6", width=50, anchor=CENTER)


#
# def insertar():
#     info1 = textCod.get()
#     info2 = textName.get()
#     info3 = textAp.get()
#     info4 = textAge.get()
#     info5 = textCond.get()
#     info6 = textSex.get()
#     print(info1)
# boton1 = tk.Button(tab1, text="Click", command=insertar).grid()

# datos = []
# aux = 1
# for n in range(1, aux):
#     datos.append((f'#0{n}', f'#1{n}', f'#2{n}', f'#3{n}', f'#4{n}', f'#5{n}'))
# for dato in datos:
#     Tabla.insert('', tk.END, values=dato)
#     aux = aux + 1

# df = Table(tab2, showtoolbar=True, showstatusbar=True, on_bad_lines='skip')
# df.show()
# df = pd.DataFrame(columns=['Código', 'Nombre', 'Apellido', 'Edad', 'Condición', 'Sexo'])
# df['Código']= None
# df['Nombre']= None
# df['Apellido']= None
# df['Edad']= None
# df['Condición médica']= None
# df['Sexo']= None

# Creación de botones -----------------------------------------------------
# boton1 = tk.Button(tab1, text="Guardar").pack()


# Captura de imagen -------------------------------------------------------


def iniciar():
    global cap
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    visualizar()


def visualizar():
    global cap
    if cap is not None:
        ret, frame = cap.read()
        if ret == True:
            frame = imutils.resize(frame, width=450)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            im = Image.fromarray(frame)
            img = ImageTk.PhotoImage(image=im)

            lblVideo.configure(image=img)
            lblVideo.image = img
            lblVideo.after(5, visualizar)
        else:
            lblVideo.image = ""
            cap.release()


def guardar_imagen():
    global cap
    path_file = "C:/Users/Jael/Pictures/Camera Roll/Alm_base"
    if not os.path.exists(path_file):
        os.makedirs(path_file)
    c = 1
    ret, frame = cap.read()
    if ret == True:
        cv2.imwrite(path_file + "/imagen_0" + str(c) + ".png", frame)
        c = c + 1
        print("Foto tomada correctamente")
    else:
        print("Error al acceder a la cámara")
    cap.release()


cap = None
btnCaptura = Button(tab1, text="Encender", width=10, command=iniciar)
btnCaptura.grid(column=0, row=8, padx=5, pady=5, columnspan=1)

btnGuardar_img = Button(tab1, text="Guardar", width=10, command=guardar_imagen)
btnGuardar_img.grid(column=1, row=8, padx=5, pady=5, columnspan=1)

lblVideo = Label(tab1)
lblVideo.grid(column=2, row=0, padx=30, pady=30, rowspan=10)


# Cierre de ventana ---------------------------------------
window.mainloop()
