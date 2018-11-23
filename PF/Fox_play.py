# -*- coding: utf-8 -*-
"""
Created on Fri May 18 19:15:14 2018

@author: Thomas, Marcelo e Paulo
"""
import pygame
from pygame.locals import *
from matplotlib.pyplot import imread
from pygame.time import wait
from random import randrange

from Fox_pause import pause
from Fox_classes import *
from Fox_parabens import parabens
from Fox_perdeu import perdeu

pygame.font.init()


def parabola(x,afin,stoptime,conc): #funcao pulo
    tempotot=stoptime+afin
    stop=afin/2+stoptime
    if x<=afin/2:
        return x*(x-afin)/conc # OK
    elif afin/2<x<=stop:
        return -(afin/2)**2/conc
    else: 
        return (x-stoptime)*(x-tempotot)/conc

##JOGAR================================================================================



def jogar(imagem_fundo,effect,buttonsound,nenemy,acabou,burro,bazinga):
    nextaction="Play"
    pygame.display.set_caption('Super Fox Bros')
    
    relogio = pygame.time.Clock()
    
    afin=19 #diminui tempo do pulo
    stoptime=2 #quanto tempo vai permanecer no topo
    conc=1 #quao alto ele vai
    tempotot=stoptime+afin
    
    ##INICIALIZAÇÃO DO JOGO##

    # Criação da janela com medidas baseadas na figura (Nome_Tela_Opcoes)
    imgfundo=pygame.image.load(imagem_fundo)
    altura,largura,chan=imread(imagem_fundo).shape
    tela = pygame.display.set_mode((largura,altura), 0, 32)    
    fundo = imgfundo.convert()
    tela.blit(fundo, (0, 0))

    #movimentos dos personagens
    morte = [pygame.image.load("Fox sprites morrendo{}d.png".format(i)) for i in range (1,3) for k in range(4)]
    parado = [pygame.image.load("Fox sprites parada{}.png".format(i)) for i in range (1,7)]
    pulandoesquerda = [pygame.image.load("FOx sprites 2d pulando{}.png".format(i)) for i in range (1,7)]
    andando = [pygame.image.load("Fox sprites 2d correndo{}.png".format(i)) for i in range (1,4)]
    pulando = [pygame.image.load("FOx sprites 2d pulando{}d.png".format(i)) for i in range (1,7)]
    andandoesquerda = [pygame.image.load("Fox sprites 2d correndoesquerda{}.png".format(i)) for i in range (1,4)]
    
    mov={'parado': parado, 'pulando': pulando, 'andando': andando, 'morrendo': morte,\
         'pulandoesq': pulandoesquerda, 'andandoesq': andandoesquerda}
    
    velx=12

    raposa = Raposa(mov,45,422)
    raposa_group = pygame.sprite.Group()
    raposa_group.add(raposa)
    
    raposa.rect.y-=200
    
    goomba_group = pygame.sprite.Group()
    goombas=[]
    for i in range(nenemy):
        goomba = Goomba('R2D2 Direita.png', randrange(largura),460, randrange(3,15))
        goombas.append(goomba)
        goomba_group.add(goomba)
        
    bandeira = Flag("banderola.png", 950, 450)
    bandeira_group = pygame.sprite.Group()
    bandeira_group.add(bandeira)
    
    exitcond = False
    rodando = True
    buttonclick=False
    pausado=False
    
    # Grupo de botões   
    but_group=pygame.sprite.Group()

    # Imagens dos botões
    pausarimg='PauseY.png'
    coracaoimg = pygame.image.load("heart.png")
    coracaoimg_2 = pygame.transform.scale(coracaoimg, (25, 25))

    # Botões 
    pausar=Button(pausarimg,largura-70,20)
    
    # Adicionar botões ao grupo
    but_group.add(pausar)
    
    
    ##### LOOP PRINCIPAL #####
    
    pulocond=False
    pulo=0
    morte = False
    mortecont=0
    ganhou = False
    
    vidas = 3
    acertou = 3
    
    myfont = pygame.font.SysFont('Comic Sans Bold', 40)
    life_texto = myfont.render('x ' + str(vidas), 1, (255, 0, 0))
    
    while rodando and imagem_fundo=="oriprop.png":
        relogio.tick(15)
        
        pressed_keys = pygame.key.get_pressed()
        
        andaresq=True
        andardir=True
        
        if raposa.rect.x < 0: #quando chega no final da tela ele para
            andaresq=False
        elif raposa.rect.x > 920: 
            andardir=False
            
        ###MOVIMENTOS###
            
        if (pressed_keys[K_LEFT] or pressed_keys[K_a]) and andaresq and not morte:
            raposa.change('andandoesq')
            raposa.rect.x -= velx
                  
        if (pressed_keys[K_RIGHT] or pressed_keys[K_d]) and andardir and not morte:
            raposa.rect.x += velx
            raposa.change('andando')
        
        if not any(pressed_keys) and raposa.sprites!=raposa.dict['morrendo']:
            raposa.change('parado')
            
        if (pressed_keys[K_SPACE] or pulocond or pressed_keys[K_UP] or pressed_keys[K_w]) and not morte:
            if not pulocond:
                pulo=0
                pinicial=raposa.rect.y
                pulocond=True
            if pulocond:
                raposa.rect.y=pinicial+parabola(pulo,afin,stoptime,conc)
                pulo+=1
            if pulo>tempotot:
                pulocond=False
                pulo=0
            raposa.change('pulando')
        
        if not morte:
            for goomba in goombas:
                goomba.update()
                if pygame.sprite.spritecollide(goomba,raposa_group,False):
                    vidas -= 1
                    life_texto = myfont.render('x ' + str(vidas), 1, (255, 0, 0))
                    if vidas != 0:
                        raposa.rect.x = 42
                        raposa.rect.y = 422
                    for goomba2 in goombas:
                        goomba2.reset(largura)
                    if vidas == 0:
                        raposa.change('morrendo')
                        morte=True
                        mortecont=0
    
                if goomba.rect.x < 0 or goomba.rect.x > 990:
                    goomba.vx = - goomba.vx
            
        if morte:
            mortecont+=1
            if mortecont==17:
                exitcond=True
                
        if pygame.sprite.spritecollide(bandeira,raposa_group,False):
            acertou-=1
            bandeira.rect.x =randrange(largura)
            if acertou == 2:
                burro.play()
            if acertou == 1:
                bazinga.play()
            if acertou == 0:
                acabou.play()
                ganhou=True
                exitcond=True
                acabou.play(0)
                    
          
        ##SAIDAS DO JOGO##
        pausar.image=pygame.image.load(pausarimg)
        tela.blit(coracaoimg_2, (25, 35))
        but_group.draw(tela)
        
        mousepos=pygame.mouse.get_pos()
        
        if mousepos[0] in range(pausar.x[0],pausar.x[1])\
        and mousepos[1] in range(pausar.y[0],pausar.y[1]):
            pausarimg='PauseYD.png'
        else:
            pausarimg='PauseY.png'
            
        pygame.display.update()
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[K_ESCAPE]:
            exitcond=True
            nextaction='Start'
            
        for event in pygame.event.get(): 
            if event.type == QUIT:      
                exitcond = True            
                nextaction='ExitGame'
                
        if pygame.mouse.get_pressed():
            if pygame.mouse.get_pressed()[0]==1:
                if mousepos[0] in range(pausar.x[0],pausar.x[1])\
                and mousepos[1] in range(pausar.y[0],pausar.y[1]) and not morte:
                    pausado=True
                    buttonclick = True
                    
                if buttonclick:
                    effect.set_volume(buttonsound)
                    effect.play()
                    buttonclick=False
                if pausado:
                    nextaction = pause("oriproppausado.png",effect,buttonsound)
                    pausado=False
        
        if exitcond or nextaction!="Play":
            rodando=False
            if morte:
                nextaction=perdeu('GamoOver2.png')
                return nextaction
            
            rodando=False
            if ganhou:
                nextaction=parabens('parabens.png')
                return nextaction
            
        tela.blit(fundo, (0, 0))
        raposa_group.draw(tela)
        raposa_group.update()
        goomba_group.draw(tela)
        goomba_group.update()
        bandeira_group.draw(tela)
        #pygame.draw.rect(tela, (255,0,0), raposa.rect)
        tela.blit(life_texto, (55,35))
        
    return nextaction