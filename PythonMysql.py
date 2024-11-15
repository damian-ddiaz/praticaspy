#mi libreria tkinter que permitira hacer mi formulario 22
import tkinter as tk 

#importar los modulos restantes de tkinter Damian Diaz desde en san jacinto vereda 4

from tkinter import *

from tkinter import ttk 
from tkinter import messagebox

from Usuarios import *
from Conexion import * 

class FormularioUsarios:

    global base
    base = None

    global texBoxId
    texBoxId = None

    global texBoxNombre
    texBoxNombre = None

    global texBoxCorreo
    texBoxCorreo = None

    global texBoxClave
    texBoxClave = None

    global seleecionEtatus
    seleecionEtatus = None

    global groupBox
    groupBox = None

    global tree
    tree = None
     
def Formulario():
        global base
        global texBoxId
        global texBoxNombre
        global texBoxCorreo
        global texBoxClave
        global seleecionEtatus
        global groupBox
        global tree
    
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
            texBoxNombre = Entry(groupBox)
            texBoxNombre.grid(row=1,column=1)
             
            labelCorreo = Label(groupBox,text="Correo",width=13,font=("arial",12)).grid(row=2,column=0)
            texBoxCorreo = Entry(groupBox)
            texBoxCorreo.grid(row=2,column=1) 
            
            labelClave = Label(groupBox,text="Clave",width=13,font=("arial",12)).grid(row=3,column=0)
            texBoxClave = Entry(groupBox)
            texBoxClave.grid(row=3,column=1) 
            
            labelEstatus = Label(groupBox,text="Estatus",width=13,font=("arial",12)).grid(row=4,column=0)
            seleecionEtatus = tk.StringVar()
            combo = ttk.Combobox(groupBox,values=["Activo","Inactivo"],textvariable=seleecionEtatus)
            combo.grid(row=4,column=1)  
            seleecionEtatus.set("Activo")       

            Button(groupBox,text="Guardar",width=10,command=guardarRegistros).grid(row=5,column=0) 
            Button(groupBox,text="Modificar",width=10).grid(row=5,column=1) 
            Button(groupBox,text="Eliminar",width=10).grid(row=5,column=2) 

            groupBox = LabelFrame(base,text="Lista de Personal",padx=5,pady=5,)
            groupBox.grid(row=0,column=1,padx=5,pady=5)
            
            # Crear un TREVIEW
            tree = ttk.Treeview(groupBox,columns=("id","Nombre","Correo","contraseña","Estatus"),show='headings',height=5,)
            tree.column("# 1",anchor=CENTER)
            tree.heading("# 1", text="Id")
            tree.column("# 2",anchor=CENTER)
            tree.heading("# 2", text="Nombre")
            tree.column("# 3",anchor=CENTER)
            tree.heading("# 3", text="Correo")
            tree.column("# 4",anchor=CENTER)
            tree.heading("# 4", text="Clave")
            tree.column("# 3",anchor=CENTER)
            tree.heading("# 3", text="Estaus")

            #Agregar los Datos a la Tabla
            # Mostrar la Tabla
            for row in CUsuarios.mostrarUsuarios():
                tree.insert("","end",values=row)

            tree.pack()

            base.mainloop()
        except ValueError as error:
            print("Error al mostrar la interfaz, error: {}".format(error))
    
def guardarRegistros():
        global texBoxNombre,texBoxCorreo,texBoxClave,seleecionEtatus

        try:
            #verificar si los widgets estanm inicializados
            if texBoxNombre is None or texBoxCorreo is None or texBoxClave is None or seleecionEtatus is None:
                print("Los widgets No estan Inicializados")
                return

            nombre  = texBoxNombre.get()
            correo  = texBoxCorreo.get() 
            clave   = texBoxClave.get()
            estatus  = seleecionEtatus.get()

            CUsuarios.ingresarUsuarios(nombre,correo,clave,estatus)
            messagebox.showinfo("Informcion","Los Datos Fueron Guardados")

            #limiando Campos
            texBoxNombre.delete(0,END)
            texBoxCorreo.delete(0,END)
            texBoxClave.delete(0,END)

  
        except ValueError as error:
            print("Error el ingresar datos {}".format(error))


Formulario()