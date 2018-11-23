# -*- coding: utf-8 -*-
"""
Created on Fri May 18 18:51:46 2018

@author: Thomas, Marcelo e Paulo
"""
import pygame
from pygame.locals import *
from matplotlib.pyplot import imread
from random import randrange
from Fox_classes import *
from pygame.time import wait


def fases(Nome_Tela_Fase,effect,buttonsound):
    pygame.display.set_caption('Escolha uma fase')
    
    # Criação da janela com medidas baseadas na figura (Nome_Tela_Ajuda)
    imgfundo=pygame.image.load(Nome_Tela_Fase)
    altura,largura,chan=imread(Nome_Tela_Fase).shape
    tela = pygame.display.set_mode((largura,altura), 0, 32)    
    fundo = imgfundo.convert()
    tela.blit(fundo, (0, 0))
    
    exitcond = False
    rodando = True
    buttonclick = False
    
    # Grupo de botões
    but_group=pygame.sprite.Group()

    # Imagens dos botões
    campimg='campestrepqbw.png' #sair para o menuimg
    voltarimg='voltar.png'
    aviaoimg='aviaopqbw.png'
    difimg='facil.png'

    # Botões
    
    camp=Button(campimg,140,175)
    voltar=Button(voltarimg,340,510)
    aviao=Button(aviaoimg,555,175)
    dif=Button(voltarimg,510,510)
    
    nenemy=2
    
    # Adicionar botões ao grupo
    
    but_group.add(voltar)
    but_group.add(camp)
    but_group.add(aviao)
    but_group.add(dif)
    
    ##### LOOP PRINCIPAL #####
    while rodando:
        camp.image=pygame.image.load(campimg)
        aviao.image=pygame.image.load(aviaoimg)
        voltar.image=pygame.image.load(voltarimg)
        dif.image=pygame.image.load(difimg)
        but_group.draw(tela)
        Tela=""
        mousepos=pygame.mouse.get_pos()

        if mousepos[0] in range(camp.x[0],camp.x[1])\
        and mousepos[1] in range(camp.y[0],camp.y[1]):
            campimg='campestrepq.png'
        else:
            campimg='campestrepqbw.png'
        
        if mousepos[0] in range(aviao.x[0],aviao.x[1])\
        and mousepos[1] in range(aviao.y[0],aviao.y[1]):
            aviaoimg='aviaopq.png'
        else:
            aviaoimg='aviaopqbw.png'   
        
        if mousepos[0] in range(voltar.x[0],voltar.x[1])\
        and mousepos[1] in range(voltar.y[0],voltar.y[1]):
            voltarimg='voltardarker.png'
        else:
            voltarimg='voltar.png'    
                
        pygame.display.update()
        
        for event in pygame.event.get(): 
            if event.type == QUIT:      
                    exitcond = True        
                    nextaction='ExitGame'
        
        if pygame.mouse.get_pressed():
            if pygame.mouse.get_pressed()[0]==1:
                if mousepos[0] in range(voltar.x[0],voltar.x[1])\
                and mousepos[1] in range(voltar.y[0],voltar.y[1]):
                    exitcond=True
                    nextaction='Start'
                    buttonclick = True
                if mousepos[0] in range(aviao.x[0],aviao.x[1])\
                and mousepos[1] in range(aviao.y[0],aviao.y[1]):
                    exitcond=True
                    nextaction='Play2'
                    Tela="aviaao.png"
                    buttonclick = True
                if mousepos[0] in range(camp.x[0],camp.x[1])\
                and mousepos[1] in range(camp.y[0],camp.y[1]):
                    exitcond=True
                    nextaction='Play'
                    Tela="oriprop.png"
                    buttonclick = True
                if mousepos[0] in range(dif.x[0],dif.x[1])\
                and mousepos[1] in range(dif.y[0],dif.y[1]):
                    nenemy+=1
                    if nenemy==6:
                        nenemy=2
                    if nenemy==2:
                        difimg='facil.png'
                    if nenemy==3:
                        difimg='medio.png'
                    if nenemy==4:
                        difimg='dificil.png'
                    if nenemy==5:
                        difimg='expert.png'
                    wait(200)
                    #print(nenemy)
                    buttonclick = True

                if buttonclick:
                    effect.set_volume(buttonsound)
                    effect.play()
                    buttonclick=False
        
#        
#        
#        voltar.image=pygame.image.load(voltarimg)
#        but_group.draw(tela)
#        
#        mousepos=pygame.mouse.get_pos()
#        if mousepos[0] in range(voltar.x[0],voltar.x[1])\
#        and mousepos[1] in range(voltar.y[0],voltar.y[1]):
#            voltarimg='voltardarker.png'
#        else:
#            voltarimg='voltar.png'
#            
#        mousepos2=pygame.mouse.get_pos() 
#        if mousepos2[0] in range(sair.x[0],sair.x[1])\
#        and mousepos2[1] in range(sair.y[0],sair.y[1]):
#            sairimg='menudarker.png'
#        else:
#            sairimg='teclamenu.png'        
#            
#        pygame.display.update()
#        
#        for event in pygame.event.get(): 
#            if event.type == QUIT:      
#                    exitcond = True            
#                    nextaction='ExitGame'
#        
#        if pygame.mouse.get_pressed():
#            if pygame.mouse.get_pressed()[0]==1:
#                if mousepos[0] in range(voltar.x[0],voltar.x[1])\
#                and mousepos[1] in range(voltar.y[0],voltar.y[1]):
#                    exitcond=True
#                    nextaction='Play'
#                    buttonclick = True
#                if mousepos2[0] in range(sair.x[0],sair.x[1])\
#                and mousepos2[1] in range(sair.y[0],sair.y[1]):
#                    exitcond=True
#                    nextaction='Start'
#                    buttonclick = True
#                if buttonclick:
#                    effect.set_volume(buttonsound)
#                    effect.play()
#                    buttonclick=False

        if exitcond:
            rodando=False
            
    return nextaction,Tela,nenemy
