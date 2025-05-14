import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os 
from analisis import DataAnalyzer
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox
data = pd.read_csv("adult.csv")
analizar = DataAnalyzer(data)

def informacion():
    try:
        text_area.delete("1.0",tk.END) #Para vaciar al ejecutar
        info = analizar.summary()
        text_area.insert(tk.END, info)
    except:
        messagebox.showerorr("Error", "No se puede") 


ventana = tk.Tk()
ventana.title("Analisis de datos")

boton_summary = tk.Button(ventana, text= "Info", command =informacion)
boton_summary.pack()

text_area = tk.scrolledtext.ScrolledText(ventana, width = 70, height=30)
text_area.pack()
ventana.mainloop()