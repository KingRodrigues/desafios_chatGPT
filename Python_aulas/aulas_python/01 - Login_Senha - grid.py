# grid
from tkinter import *

bgk = '#242323'

janela = Tk()
janela.title("Exemplo Grid")
janela.geometry('300x150')
janela.config(bg=bgk)

# usuário
Label(janela, text='Usuário: ', fg='red', bg=bgk).grid(row=0, column=0, padx=5, pady=5)
Entry(janela).grid(row=0, column=1, padx=5, pady=5) # entrada de texto para o usuário
# senha
Label(janela, text='Senha: ', fg='red', bg=bgk).grid(row=1, column=0, padx=5, pady=5)
Entry(janela, show='*').grid(row=1, column=1, padx=5, pady=5) # entrada de texto para senha, 'show='*': Substitui o texto digitado pelo caractere '*'.
# botão para login
Button(janela, text='Entrar', fg='red', bg=bgk).grid(row=2, column=0, columnspan=2, pady=10) # columnspan=2: Faz o botão ocupar duas colunas (centralizado na grade)

janela.mainloop()
