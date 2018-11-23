# -*- coding: utf-8 -*-
"""
Created on Tue May  1 13:12:43 2018

@author: Thomas,Marcelo,Paulo
"""

import pygame
from pygame.locals import *
from matplotlib.pyplot import imread
from pygame.time import wait
from random import randrange

from StartMenu import startmenu
from Help import ajuda
from Options import opcoes
from Fases import fases
from Pause import pause
from Play import jogar

from Classes import Button,Raposa,Goomba,R2D2,Slider


pygame.init()

global effect

global buttonsound

effect = pygame.mixer.Sound('click.wav')

buttonsound = 1

pygame.font.init()
font = pygame.font.SysFont("Courier New", 24)

Tela_Inicial = "Fundo_top2.png"
Tela_Ajuda= "Ajudaa2.png"
Tela_Opcoes="Conf.png"
Tela_Fases= "Fundo fases.png"
#Tela_Jogar2="aviaao.PNG"
Tela_Jogar="oriprop.png"
#Tela_Pause2 = "aviaaopausado.png"
Tela_Pause = "oriproppausado.png"

nextaction = "Start"

effect = pygame.mixer.Sound('click.wav')

somjogo = pygame.mixer.Sound('click.wav')
somjogo.play(-1)

gamesound=0 ############## Som de fundo

while True:
    somjogo.set_volume(gamesound)
    if nextaction=='ExitGame':
        pygame.display.quit()
        pygame.quit()
        break
    elif nextaction=='Start':
        nextaction=startmenu(Tela_Inicial,effect,buttonsound)
    
    elif nextaction=='Play':
        nextaction=jogar(Tela_Jogar,effect,buttonsound)
        
#    elif nextaction=='Play2':
#        nextaction=jogar(Tela_Jogar2)
    
    elif nextaction=='Help':
        nextaction=ajuda(Tela_Ajuda,effect,buttonsound)
        
    elif nextaction=='Fases':
        nextaction,Tela_Jogar=fases(Tela_Fases,effect,buttonsound)
        
    elif nextaction=='Options':
        nextaction,buttonsound,gamesound=opcoes(Tela_Opcoes,effect,buttonsound,gamesound,somjogo)
    
    elif nextaction=='Pause':
        nextaction=pause(Tela_Pause,effect,buttonsound)
        
#    elif nextaction=='Pause2':
#        nextaction=pause(Tela_Pause2)
    