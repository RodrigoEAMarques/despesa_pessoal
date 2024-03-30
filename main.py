from tkinter import *
from tkinter import Tk, ttk

co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # verde
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # azul
co7 = "#3fbfb9"   # verde
co8 = "#263238"   # + verde
co9 = "#e9edf5"   # + verde

colors = ['#5588bb', '#66bbbb','#99bb55', '#ee9944', '#444466', '#bb5555']

# Criando janela
window = Tk()
window.title("Sistema de Controle Financeiro Pessoal")
window.geometry('900x650')
window.config(background=co9)
window.resizable(width=FALSE, height=FALSE)

style = ttk.Style(window)
style.theme_use("default")

# Frames para divisão de tela
frameCima = Frame(window, width=1043, height=50, bg=co1, relief="flat")
frameCima.grid(row=0, column=0)

frameMeio = Frame(window, width=1043, height=361, bg=co1, pady=20, relief="flat")
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBraixo = Frame(window, width=1043, height=300, bg=co1, relief="flat")
frameBraixo.grid(row=2, column=0, pady=0, padx=10, sticky=NSEW)



window.mainloop()
