import tkinter as tk 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class FormularioUsuarios:
    def __init__(self):
        self.formulario()

    def formulario(self):
        try:
            base = Tk()
            base.geometry("1200x300")
            base.title("Formulario Python")
            
            # Aquí puedes agregar más widgets al formulario

            base.mainloop()  # Corrección del error tipográfico
        except ValueError as error:
            print("Error al mostrar la interfaz, error: {}".format(error))

# Crear una instancia de la clase
FormularioUsuarios()