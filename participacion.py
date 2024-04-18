import os
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog

def abrirarchivo():
    archivo = filedialog.askopenfilename()
    if archivo:
        with open(archivo, "r") as f:
            contenido = f.read()
            print(contenido)

ventana = tk.Tk()
ventana.title("Abrir")

boton_abrir = tk.Button(ventana, text="Abrir", command=abrirarchivo)
boton_abrir.pack(pady=10)

ventana.mainloop()


root = Tk()
frm = ttk.Frame(root, padding=20)
frm.grid()
ttk.Label(frm, text="").grid(column=0, row=0)
ttk.Button(frm, text="Abrir archivo", command=root.destroy).grid(column=1, row=0)
root.mainloop()

def caracteres(ruta_archivo):
    
    ruta_completa = os.path.abspath(ruta_archivo)
    
    frecuencia_caracteres = {}
    

    if not os.path.exists(ruta_completa):
        print(f"No se encontró el archivo: {ruta_completa}")
        return None
 
    
    try:
        with open(ruta_completa, 'r', encoding='utf-8') as archivo:
            texto = archivo.read()
    except Exception as e:
        print(f"Error al leer el archivo: {e}")
        return None
        
    # Contar la frecuencia de cada carácter en el texto
    for caracter in texto:
        if caracter in frecuencia_caracteres:
            frecuencia_caracteres[caracter] += 1
        else:
            frecuencia_caracteres[caracter] = 1
    
    # Ordenar el diccionario por valor (frecuencia) de mayor a menor
    frecuencia_ordenada = dict(sorted(frecuencia_caracteres.items(), key=lambda item: item[1], reverse=True))
    
    return frecuencia_ordenada

# Ejemplo de uso
ruta_archivo = "Holaaaa.txt"
resultado = caracteres(ruta_archivo)

if resultado is not None:
    print("Caracteres ordenados por frecuencia:")
    for caracter, frecuencia in resultado.items():
        print(f"'{caracter}': {frecuencia}")