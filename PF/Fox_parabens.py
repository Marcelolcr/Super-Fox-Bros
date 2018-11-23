# -*- coding: utf-8 -*-
"""
Created on Tue May 22 18:49:44 2018

@author: Marcelo, Thomas e Paulo
"""

import pygame
from pygame.locals import *
from matplotlib.pyplot import imread
from pygame.time import wait


def parabens(Nome_Tela_Parabens):
    pygame.display.set_caption('Parabéns')
    
    # Criação da janela com medidas baseadas na figura (Nome_Tela_Ajuda)
    imgfundo = pygame.image.load(Nome_Tela_Parabens)
    altura,largura,chan=imread(Nome_Tela_Parabens).shape
    tela = pygame.display.set_mode((largura,altura), 0, 32)    
    fundo = imgfundo.convert()
    tela.blit(fundo, (0, 0))
    
    rodando = True
    
    nextaction="Start"
    ##### LOOP PRINCIPAL #####
    while rodando:                
        pygame.display.update()
        wait(4000)
        for event in pygame.event.get(): 
            if event.type == QUIT:      
                    nextaction='ExitGame'

        return nextaction