# -*- coding: utf-8 -*-
"""
Created on Fri May 18 19:04:00 2018

@author: Thomas, Marcelo e Paulo
"""

import pygame
from pygame.locals import *
from matplotlib.pyplot import imread
from random import randrange
from Fox_classes import *


def pause(Nome_Tela_Pause,effect,buttonsound):
    pygame.display.set_caption('Pausado')
    
    # Criação da janela com medidas baseadas na figura (Nome_Tela_Ajuda)
    imgfundo = pygame.image.load(Nome_Tela_Pause)
    altura,largura,chan=imread(Nome_Tela_Pause).shape
    tela = pygame.display.set_mode((largura,altura), 0, 32)    
    fundo = imgfundo.convert()
    tela.blit(fundo, (0, 0))
    
    exitcond = False 
    pausado = True
    buttonclick = False
    
    # Grupo de botões
    but_group=pygame.sprite.Group()

    # Imagens dos botões
    voltarimg='voltar.png' #sair para o menu
    sairimg='teclamenu.png'

    # Botões
    voltar=Button(voltarimg,270,250)
    sair=Button(sairimg,600,250)
    
    # Adicionar botões ao grupo
    but_group.add(voltar)
    but_group.add(sair)
    
    ##### LOOP PRINCIPAL #####
    while pausado:
        voltar.image=pygame.image.load(voltarimg)
        sair.image=pygame.image.load(sairimg)
        but_group.draw(tela)
        
        mousepos=pygame.mouse.get_pos()
        if mousepos[0] in range(voltar.x[0],voltar.x[1])\
        and mousepos[1] in range(voltar.y[0],voltar.y[1]):
            voltarimg='voltardarker.png'
        else:
            voltarimg='voltar.png'
            
        mousepos2=pygame.mouse.get_pos()    
        if mousepos2[0] in range(sair.x[0],sair.x[1])\
        and mousepos2[1] in range(sair.y[0],sair.y[1]):
            sairimg='menudarker.png'
        else:
            sairimg='teclamenu.png'    
                
        pygame.display.update()
        
        for event in pygame.event.get(): 
            if event.type == QUIT:      
                    exitcond = True            
                    nextaction='ExitGame'
        
        if pygame.mouse.get_pressed():
            if pygame.mouse.get_pressed()[0]==1:
                if mousepos[0] in range(voltar.x[0],voltar.x[1])\
                and mousepos[1] in range(voltar.y[0],voltar.y[1]):
                    if Nome_Tela_Pause == "oriproppausado.png":
                        exitcond=True
                        nextaction='Play'
                        buttonclick = True
                    elif Nome_Tela_Pause == "aviaaopausado.png":
                        exitcond=True
                        nextaction='Play2'
                        buttonclick = True
                if mousepos2[0] in range(sair.x[0],sair.x[1])\
                and mousepos2[1] in range(sair.y[0],sair.y[1]):
                    exitcond=True
                    nextaction='Start'
                    buttonclick = True
                if buttonclick:
                    effect.set_volume(buttonsound)
                    effect.play()
                    buttonclick=False

        if exitcond:
            pausado=False
            
    return nextaction