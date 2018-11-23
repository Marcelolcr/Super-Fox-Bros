# -*- coding: utf-8 -*-
"""
Created on Tue May 22 18:49:44 2018

@author: Marcelo, Thomas e Paulo
"""

import pygame
from pygame.locals import *
from matplotlib.pyplot import imread
from pygame.time import wait


def perdeu(Nome_Tela_Perdeu):
    pygame.display.set_caption('Game over')
    
    # Criação da janela com medidas baseadas na figura (Nome_Tela_Ajuda)
    imgfundo = pygame.image.load(Nome_Tela_Perdeu)
    altura,largura,chan=imread(Nome_Tela_Perdeu).shape
    tela = pygame.display.set_mode((largura,altura), 0, 32)    
    fundo = imgfundo.convert()
    tela.blit(fundo, (0, 0))
    
    rodando = True
    
    nextaction="Start"
    ##### LOOP PRINCIPAL #####
    while rodando:                
        pygame.display.update()
        wait(3000)
        for event in pygame.event.get(): 
            if event.type == QUIT:      
                    nextaction='ExitGame'
        
        return nextaction