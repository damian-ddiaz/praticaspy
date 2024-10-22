#mi libreria tkinter que permitira hacer mi formulario
import tkinter as tk 

#importar los modulos restantes de tkinter

from tkinter import *

from tkinter import ttk
from tkinter import messagebox

class FormularioUsarios:
    def Formulario():
        try:
            base =Tk()
            base.geometry("1200x300")
            base.title("Formulario Python")
            
            groupBox = LabelFrame(base,text="Datos del Usuario",padx=5,pady=5)
            groupBox.grid(row=0,column=0,padx=10,pady=10)
            
            labelId = Label(groupBox,text="Id",width=13,font=("arial",12)).grid(row=0,column=0)
            texBoxId = Entry(groupBox)
            texBoxId.grid(row=0,column=1)
             
            labelNombre = Label(groupBox,text="Nombres",width=13,font=("arial",12)).grid(row=1,column=0)
            texBoxId = Entry(groupBox)
            texBoxId.grid(row=1,column=1)
             
            labelCorreo = Label(groupBox,text="Correo",width=13,font=("arial",12)).grid(row=2,column=0)
            texBoxId = Entry(groupBox)
            texBoxId.grid(row=2,column=1) 
            
            labelClave = Label(groupBox,text="Clave",width=13,font=("arial",12)).grid(row=3,column=0)
            texBoxId = Entry(groupBox)
            texBoxId.grid(row=3,column=1) 
            
            labelEstatus = Label(groupBox,text="Estatus",width=13,font=("arial",12)).grid(row=4,column=0)
            seleecionEtatus = tk.StringVar()
            combo = ttk.Combobox(groupBox,values=["Activo","Inactivo"],textvariable=seleecionEtatus)
            combo.grid(row=4,column=1)  
            seleecionEtatus.set("Activo")        
            
            
                
            base.mainloop()
        except ValueError as error:
            print("Error al mostrar la interfaz, error: {}".format(error))
                
    Formulario()