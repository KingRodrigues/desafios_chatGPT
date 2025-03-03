from tkinter import *

# cores --------------------------------
cor0 = "#444466" # preto
cor1 = "feffff" # branco
cor2 = "#f05a43" # vermelho

# janela
janela = Tk()
janela.title('')
janela.geometry('295x350')
janela.configure(bg=cor1)

frame_cima = Frame(janela, width=280, height=50, bg=cor1, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0,sticky=NSEW)

frame_baixo = Frame(janela, width=280, height=310, bg=cor1, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEWS)

janela.mainloop()
