# faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
# ex: escreva('Olá, Mundo!')

def escreva(msg):
    tam = len(msg) + 4 # tamanho
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)

# programa principal
escreva('Olá, Mundo!')
