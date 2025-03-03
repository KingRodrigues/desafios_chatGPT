from tkinter import *

janela = Tk()
janela.title('Exemplo Place')
janela.geometry('300x200')

Label(janela, text='Texto no topo').place(x=100, y=20) # place: usa cordenadas absolutas
Button(janela, text='Botão 1').place(x=50, y=80)
Button(janela, text='Botão 2').place(x=150, y=80)

janela.mainloop()
