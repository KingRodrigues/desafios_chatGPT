print('='*6,'DESAFIO 021','='*6)
#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

'''import pygame
import time

#iniciar pygame
pygame.init()

#Iniciar drivers
pygame.mixer.init()

#mixer
pygame.mixer.music.load('ex021.mp3')

#carregar
pygame.mixer.music.play()

#Aguardar a música terminar (duração do arquivo, em segundos)
while pygame.mixer.music.get_busy():
    time.sleep(1) # Esperar um segundo entre verificações

#pygame.event.wait() #Encerrar 

#Encerrar o programa
pygame.quit()'''

import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()
