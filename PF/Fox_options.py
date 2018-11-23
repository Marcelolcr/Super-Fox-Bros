# -*- coding: utf-8 -*-
"""
Created on Fri May 18 18:40:04 2018

@author: Thomas, Marcelo e Paulo
"""

import pygame
from pygame.locals import *
from matplotlib.pyplot import imread
from random import randrange
from Fox_classes import *

pygame.font.init()
font = pygame.font.SysFont("Courier New", 24)

def opcoes(Nome_Tela_Opcoes,effect,buttonsound,gamesound,somjogo):
#    global buttonsound
    
    pygame.display.set_caption('Opções')
    imgfundo=pygame.image.load(Nome_Tela_Opcoes)
    altura,largura,chan=imread(Nome_Tela_Opcoes).shape    
    tela = pygame.display.set_mode((largura,altura), 0, 32)  
    fundo = imgfundo.convert()  
    tela.blit(fundo, (0, 0))
    
    exitcond = False
    rodando = True
    buttonclick = False

    # Grupo de botões
    but_group=pygame.sprite.Group()

    # Imagens dos botões
    voltarimg='voltar.png'

    # Botões    
    voltar=Button(voltarimg,425,420)
    
    # Adicionar botões ao grupo
    but_group.add(voltar)

    butsound = Slider("Botões", buttonsound, 1, 0, 510,250)
    sound = Slider("Fundo", gamesound, 1, 0, 280,250)
    slides = [butsound,sound]
    
    while rodando:
        
        voltar.image=pygame.image.load(voltarimg)
        but_group.draw(tela)
        
        mousepos=pygame.mouse.get_pos()
        if mousepos[0] in range(voltar.x[0],voltar.x[1])\
        and mousepos[1] in range(voltar.y[0],voltar.y[1]):
            voltarimg='voltardarker.png'
        else:
            voltarimg='voltar.png'
        
        if pygame.mouse.get_pressed():
            if pygame.mouse.get_pressed()[0]==1:
                if mousepos[0] in range(voltar.x[0],voltar.x[1])\
                and mousepos[1] in range(voltar.y[0],voltar.y[1]):
                    exitcond=True
                    nextaction='Start'
                    buttonclick = True
                if buttonclick:
                    effect.set_volume(buttonsound)
                    effect.play()
                    buttonclick=False

        for s in slides:
            if s.hit:
                s.move()
        buttonsound=butsound.val
        gamesound=sound.val
        somjogo.set_volume(gamesound)
        for s in slides:
            s.draw(tela)
            
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                nextaction='ExitGame'
                exitcond=True
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for s in slides:
                    if s.button_rect.collidepoint(pos):
                        s.hit = True
            
            elif event.type == pygame.MOUSEBUTTONUP:
                for s in slides:
                    s.hit = False
                        
        if exitcond:
            rodando=False

    return nextaction,buttonsound,gamesound
