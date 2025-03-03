from tkinter import *

janela = Tk()
janela.title('Exemplo Pack')

Button(janela, text='Topo').pack(side=TOP, fill=X, padx=5, pady=5) # side=TOP: Alinha o botão na parte superior da janela. | fill=X: Faz o botão se expandir horizontalmente.
Button(janela, text='Esquerda').pack(side=LEFT, fill=Y, padx=5, pady=5) # side=LEFT: Alinhamento à esquerda | fill=Y: Faz o botão se expandir verticalmente.
Button(janela, text='Direita').pack(side=RIGHT, fill=Y, padx=5, pady=5)
Button(janela, text='Base').pack(side=BOTTOM, fill=X, padx=5, pady=5)

janela.mainloop()
