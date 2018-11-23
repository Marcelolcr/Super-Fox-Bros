# -*- coding: utf-8 -*-
"""
Created on Fri May 18 18:21:07 2018

@author: Thomas, Marcelo e Paulo
"""

import pygame
from pygame.locals import *
from matplotlib.pyplot import imread
from pygame.time import wait
from Fox_classes import *


def startmenu(Nome_Tela_Inicial,effect,buttonsound):
    pygame.display.set_caption('Menu inicial')
    
    # Criação da janela com medidas baseadas na figura (Nome_Tela_Inicial)
    imgfundo=pygame.image.load(Nome_Tela_Inicial)
    altura,largura,chan=imread(Nome_Tela_Inicial).shape    
    tela = pygame.display.set_mode((largura,altura),0, 32)  
    fundo = imgfundo.convert()
    tela.blit(fundo, (0, 0))
    
    exitcond = False
    rodando = True    
    buttonclick = False
            
    # Grupo de botões
    but_group=pygame.sprite.Group()
    
    # Imagens dos botões
    sairimg='sairbot.png'
    ajudaimg='ajudabot.png'
    opcaoimg='opcaobot.png'
    jogarimg='jogar_maior.png'
    
    # Botões
    sairbot=Button(sairimg,150,455)
    ajudabot=Button(ajudaimg,150,255)
    opcaobot=Button(opcaoimg,150,355)
    jogarbot=Button(jogarimg,125,130)
    
    # Adicionar botões ao grupo
    but_group.add(sairbot)
    but_group.add(opcaobot)
    but_group.add(ajudabot)
    but_group.add(jogarbot)
    
    ##### LOOP PRINCIPAL #####
    while rodando:
        
        sairbot.image=pygame.image.load(sairimg)
        ajudabot.image=pygame.image.load(ajudaimg)
        opcaobot.image=pygame.image.load(opcaoimg)
        jogarbot.image=pygame.image.load(jogarimg)

        but_group.draw(tela)
        mousepos=pygame.mouse.get_pos()
        
        if mousepos[0] in range(sairbot.x[0],sairbot.x[1])\
        and mousepos[1] in range(sairbot.y[0],sairbot.y[1]):
            sairimg='sairbotdarker.png'
        else:
            sairimg='sairbot.png'
        
        if mousepos[0] in range(ajudabot.x[0],ajudabot.x[1])\
        and mousepos[1] in range(ajudabot.y[0],ajudabot.y[1]):
            ajudaimg='ajudabotdarker.png'
        else:
            ajudaimg='ajudabot.png'
        
        if mousepos[0] in range(opcaobot.x[0],opcaobot.x[1])\
        and mousepos[1] in range(opcaobot.y[0],opcaobot.y[1]):
            opcaoimg='opcaobotdarker.png'
        else:
            opcaoimg='opcaobot.png'
        
        if mousepos[0] in range(jogarbot.x[0],jogarbot.x[1])\
        and mousepos[1] in range(jogarbot.y[0],jogarbot.y[1]):
            jogarimg='jogardarker_maior.png'
        else:
            jogarimg='jogar_maior.png'
        
        pygame.display.update()
        pressed_keys = pygame.key.get_pressed()
          
        if pressed_keys[K_SPACE] or pressed_keys[K_RETURN]:
            exitcond=True
            nextaction='Fases'
        if pressed_keys[K_ESCAPE]:
            exitcond=True
            nextaction='ExitGame'
        
        for event in pygame.event.get(): 
            if event.type == QUIT:
                exitcond = True
                nextaction='ExitGame'
        if pygame.mouse.get_pressed():
            if pygame.mouse.get_pressed()[0]==1:
                buttonclick=False
                if mousepos[0] in range(sairbot.x[0],sairbot.x[1])\
                and mousepos[1] in range(sairbot.y[0],sairbot.y[1]):
                    exitcond=True

                    nextaction='ExitGame'
                    buttonclick=True
                
                elif mousepos[0] in range(ajudabot.x[0],ajudabot.x[1])\
                and mousepos[1] in range(ajudabot.y[0],ajudabot.y[1]):
                    exitcond=True
                    nextaction='Help'
                    buttonclick=True
                
                elif mousepos[0] in range(opcaobot.x[0],opcaobot.x[1])\
                and mousepos[1] in range(opcaobot.y[0],opcaobot.y[1]):
                    exitcond=True
                    nextaction='Options'
                    buttonclick=True
                
                elif mousepos[0] in range(jogarbot.x[0],jogarbot.x[1])\
                and mousepos[1] in range(jogarbot.y[0],jogarbot.y[1]):
                    exitcond=True
                    nextaction='Fases'
                    buttonclick=True
                
                if buttonclick:
                    effect.set_volume(buttonsound)
                    effect.play()
                    buttonclick=False
                    if nextaction=='ExitGame':
                        wait(200)
        
        if exitcond:            
            rodando=False
            
    return nextaction
