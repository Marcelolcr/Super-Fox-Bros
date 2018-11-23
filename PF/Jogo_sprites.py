# -*- coding: utf-8 -*-
"""
Created on Tue May  1 13:12:43 2018

@author: Thomas
"""

import pygame
#import sys
from pygame.locals import *
#from random import randrange
from matplotlib.pyplot import imread
#from time import sleep
from pygame.time import wait

##CLASSES=========================================================

class Button(pygame.sprite.Sprite):
    def __init__(self,img,pos_x,pos_y):
        height, width, channels = imread(img).shape        
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x=pos_x
        self.rect.y=pos_y
        self.x=[pos_x,pos_x+width]
        self.y=[pos_y,pos_y+height]

class Raposa(pygame.sprite.Sprite):
    def __init__ (self, movimentos, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.counter = 0
        self.dict = movimentos
        self.image = movimentos['parado'][0]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def update(self):
        self.counter = (self.counter + 1) % len(self.sprites)
        self.image = self.sprites[counter]

##movimentos dos personagens
        
#movimentos = dict()
##    
##morte = [pygame.image.load("Fox sprites morrendo{}.png".format(i)) for i in range (1,5)]
#parado = [pygame.image.load("Fox sprites parada{}.png".format(i)) for i in range (1,7)]
#pulando = [pygame.image.load("FOx sprites 2d pulando{}.png".format(i)) for i in range (1,7)]
#andando = [pygame.image.load("Fox sprites 2d correndo{}.png".format(i)) for i in range (1,4)]
#   
#movimentos = {'morte': morte, 'parado': parado, 'pulando': pulando, 'andando': andando}
#        
#raposa = Raposa(movimentos, 50, 700)
#        
#
#raposa_group = pygame.sprite.Group()
#raposa_group.add(raposa)
#    
#    
#    --//--
#    
#    goomba = Goomba()
#    goomba_group = pygame.sprite.Group()
#    goomba_group.add(goomba)


#COLOCAR NO LOOPING PRINCIPAL DO JOGAR
#
#pressed_keys = pygame.key.get_pressed()
  
#  if pressed_keys[K_LEFT]:
#    raposa.rect.x -= 6
#    movimentos = movimentos['parado']
        
#  elif pressed_keys[K_RIGHT]:
#    raposa.rect.x += 6  
        
        
#  elif pressed_keys[K_UP]:
#    raposa.rect.y += 3

class Goomba(pygame.sprite.Sprite):
    def __init__ (self, img, pos_x, pos_y, vel_x, vel_y):
        pygame.sprite.Sprite.__init__(self)
        self.vx = vel_x
        self.vy = vel_y
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        
    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
    
    
    
##INICIALIZAÇÃO E MENU=========================================================
        
        

pygame.init()

global buttonsound
buttonsound = 1

def startmenu(Nome_Tela_Inicial):
    pygame.display.set_caption('Menu inicial')
    
    # Criação da janela com medidas baseadas na figura (Nome_Tela_Inicial)
    
    imgfundo=pygame.image.load(Nome_Tela_Inicial)
    altura,largura,chan=imread(Nome_Tela_Inicial).shape    
    tela = pygame.display.set_mode((largura,altura), 0, 32)  
    fundo = imgfundo.convert()
    
    tela.blit(fundo, (0, 0))
    
    exitcond = False
    
    rodando = True
    
    buttonclick = False
    
    exitplay = False
        
    # Grupo de botões
    
    but_group=pygame.sprite.Group()
    
    # Imagens dos botões
    
    sairimg='sairbot.png'
    ajudaimg='ajudabot.png'
    opcaoimg='opcaobot.png'
    jogarimg='jogar_maior.png'
    
    # Botões
    
    sairbot=Button(sairimg,150,455)
    ajudabot=Button(ajudaimg,150,355)
    opcaobot=Button(opcaoimg,150,255)
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
        
        for event in pygame.event.get(): 
            if event.type == QUIT:
                exitcond = True
                exitplay = True
                nextaction='ExitGame'
#            elif event.type == KEYDOWN:
#              if event.key == K_ESCAPE:
#                 exitcond = True
#                 nextaction='ExitGame'
        if pygame.mouse.get_pressed():
            if pygame.mouse.get_pressed()[0]==1:
                buttonclick=False
                if mousepos[0] in range(sairbot.x[0],sairbot.x[1])\
                and mousepos[1] in range(sairbot.y[0],sairbot.y[1]):
                    exitcond=True
                    exitplay = True

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
#                    exitplay=True
                    exitcond=True
                    nextaction='Play'
                    buttonclick=True
                
                if buttonclick:# and buttonmusic:
                    effect.set_volume(buttonsound)
                    effect.play()
                    buttonclick=False
                    if nextaction=='ExitGame':
                        wait(200)
        
        if exitcond:            
            rodando=False
            
    return nextaction



##AJUDA=========================================================================



def ajuda(Nome_Tela_Ajuda):
    
    pygame.init()
    pygame.display.set_caption('Ajuda')
    
    # Criação da janela com medidas baseadas na figura (Nome_Tela_Ajuda)
    
    imgfundo=pygame.image.load(Nome_Tela_Ajuda)
    altura,largura,chan=imread(Nome_Tela_Ajuda).shape
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
    
    voltar=Button(voltarimg,425,520)
    
    # Adicionar botões ao grupo

    but_group.add(voltar)
    
    ##### LOOP PRINCIPAL #####
    while rodando:
        voltar.image=pygame.image.load(voltarimg)
        but_group.draw(tela)
        
        mousepos=pygame.mouse.get_pos()
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
                if buttonclick:# and buttonmusic:
                    effect.set_volume(buttonsound)
                    effect.play()
                    buttonclick=False

        if exitcond:
            rodando=False
    return nextaction




##OPÇÕES==========================================================================

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
ORANGE = (200, 100, 50)
TRANS = (1, 1, 1)
font = pygame.font.SysFont("Courier New", 24)

class Slider():
    def __init__(self, name, val, maxi, mini, x_pos,y_pos):
        self.name=name
        self.val = val  # start value
        self.maxi = maxi  # maximum at slider position right
        self.mini = mini  # minimum at slider position left
        self.xpos = x_pos  # x-location on screen
        self.ypos = y_pos
        self.surf = pygame.surface.Surface((200, 100))
        self.hit = False  # the hit attribute indicates slider movement due to mouse interaction

        self.txt_surf = font.render(name, 1, BLACK)

        self.txt_rect = self.txt_surf.get_rect(center=(100, 30))

        # Static graphics - slider background #
        self.surf.fill((100, 100, 100))
        pygame.draw.rect(self.surf, GREY, [0, 0, 200, 100], 6)
        pygame.draw.rect(self.surf, ORANGE, [20, 20, 160, 20], 0)
        pygame.draw.rect(self.surf, WHITE, [20, 60, 160, 10], 0)

        self.surf.blit(self.txt_surf, self.txt_rect)  # this surface never changes

        # dynamic graphics - button surface #
        self.button_surf = pygame.surface.Surface((40, 40))
        self.button_surf.fill(TRANS)
        self.button_surf.set_colorkey(TRANS)
        pygame.draw.circle(self.button_surf, BLACK, (20, 20), 12, 0)
        pygame.draw.circle(self.button_surf, ORANGE, (20, 20), 8, 0)

    def draw(self,screen):
        surf = self.surf.copy()

        pos = (20+int((self.val-self.mini)/(self.maxi-self.mini)*160), 66)
        self.button_rect = self.button_surf.get_rect(center=pos)
        surf.blit(self.button_surf, self.button_rect)
        self.button_rect.move_ip(self.xpos, self.ypos)  # move of button box to correct screen position
        screen.blit(surf, (self.xpos, self.ypos))


    def move(self):
        self.val = (pygame.mouse.get_pos()[0] - self.xpos - 10) / 160 * (self.maxi - self.mini) + self.mini
        if self.val < self.mini:
            self.val = self.mini
        if self.val > self.maxi:
            self.val = self.maxi

def opcoes(Nome_Tela_Opcoes):
    global buttonsound
#    print(buttonsound)
    
    pygame.display.set_caption('Opções')
    imgfundo=pygame.image.load(Nome_Tela_Opcoes)
    altura,largura,chan=imread(Nome_Tela_Opcoes).shape    
    tela = pygame.display.set_mode((largura,altura), 0, 32)  
    fundo = imgfundo.convert()
    tela.blit(fundo, (0, 0))
    
    butsound = Slider("Botões", buttonsound, 1, 0, 500,300)
    sound = Slider("Fundo", 1, 1, 0, 200,300)
    slides = [butsound,sound]
    
    exitcond = False
    
    buttonclick = False
    
    but_group=pygame.sprite.Group()
    
    voltarimg='voltar.png'

    # Botões
    
    voltar=Button(voltarimg,425,520)
    
    # Adicionar botões ao grupo

    but_group.add(voltar)
    
    num = 0
    cond=True
    while cond:
        for s in slides:
            if s.hit:
                s.move()
                print(s.name,s.val)
        buttonsound=butsound.val
        num += 2
    
        for s in slides:
            s.draw(tela)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cond=False
            elif event.type == pygame.MOUSEBUTTONDOWN:
            
                pos = pygame.mouse.get_pos()
                for s in slides:
                    if s.button_rect.collidepoint(pos):
                        s.hit = True
            
            elif event.type == pygame.MOUSEBUTTONUP:
                for s in slides:
                    s.hit = False
                    
        voltar.image=pygame.image.load(voltarimg)
        but_group.draw(tela)
        
        mousepos=pygame.mouse.get_pos()
        if mousepos[0] in range(voltar.x[0],voltar.x[1])\
        and mousepos[1] in range(voltar.y[0],voltar.y[1]):
            voltarimg='voltardarker.png'
        else:
            voltarimg='voltar.png'
        
        pygame.display.update()
        
        if pygame.mouse.get_pressed():
            if pygame.mouse.get_pressed()[0]==1:
                if mousepos[0] in range(voltar.x[0],voltar.x[1])\
                and mousepos[1] in range(voltar.y[0],voltar.y[1]):
                    exitcond=True
                    nextaction='Start'
                    buttonclick = True
                if buttonclick:# and buttonmusic:
                    effect.set_volume(buttonsound)
                    effect.play()
                    buttonclick=False

        if exitcond:
            cond=False
            
    return nextaction        
   # return 'Start'






##JOGAR================================================================================
    


def jogar(imagem_fundo):
    pygame.display.set_caption('Super Fox Bros')
    
    ##INICIALIZAÇÃO DO JOGO##

##movimentos dos personagens
        
    movimentos = dict()
#    
#morte = [pygame.image.load("Fox sprites morrendo{}.png".format(i)) for i in range (1,5)]
    morte=1
    parado = [pygame.image.load("Fox sprites parada{}.png".format(i)) for i in range (1,7)]
    pulando = [pygame.image.load("FOx sprites 2d pulando{}.png".format(i)) for i in range (1,7)]
    andando = [pygame.image.load("Fox sprites 2d correndo{}.png".format(i)) for i in range (1,4)]
   
    movimentos = {'morte': morte, 'parado': parado, 'pulando': pulando, 'andando': andando}
        
    raposa = Raposa(movimentos, 50, 700)
        
    raposa_group = pygame.sprite.Group()
    raposa_group.add(raposa)
#    
#    
#    --//--
#    
#    goomba = Goomba()
#    goomba_group = pygame.sprite.Group()
#    goomba_group.add(goomba)
    
    # Criação da janela com medidas baseadas na figura (Nome_Tela_Opcoes)
    
    imgfundo=pygame.image.load(imagem_fundo)
    altura,largura,chan=imread(imagem_fundo).shape
    tela = pygame.display.set_mode((largura,altura), 0, 32)    
    fundo = imgfundo.convert()

    tela.blit(fundo, (0, 0))

    exitcond = False
    
    rodando = True
        
    # Grupo de botões
    
    but_group=pygame.sprite.Group()

    # Imagens dos botões

    voltarimg='voltar.png'

    # Botões
    
    voltar=Button(voltarimg,890,20)
    
    # Adicionar botões ao grupo

    but_group.add(voltar)
    
    
    ##### LOOP PRINCIPAL #####
    
    
    while rodando:
        #COLOCAR NO LOOPING PRINCIPAL DO JOGAR
#
#pressed_keys = pygame.key.get_pressed()
  
#  if pressed_keys[K_LEFT]:
#    raposa.rect.x -= 6
#    movimentos = movimentos['parado']
        
#  elif pressed_keys[K_RIGHT]:
#    raposa.rect.x += 6  
        
        
#  elif pressed_keys[K_UP]:
#    raposa.rect.y += 3
        
        voltar.image=pygame.image.load(voltarimg)
        but_group.draw(tela)
        
        mousepos=pygame.mouse.get_pos()
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
                if buttonclick:
                    effect.set_volume(buttonsound)
                    effect.play()
                    buttonclick=False

        if exitcond:
            rodando=False
            
        raposa_group.draw(tela)
        
    return nextaction



##CONFIGURAÇÕES GERAIS E MENU=======================================================



Tela_Inicial = "Fundo_top.png"
Tela_Ajuda= "Ajudaa2.png"
Tela_Opcoes="Conf.png"
Tela_Jogar="aviaao.PNG"
#Tela_Jogar="swamp2.png"

nextaction = "Start"

effect = pygame.mixer.Sound('click.wav')

while True:
    if nextaction=='ExitGame':
        pygame.display.quit()
        pygame.quit()
        break
    elif nextaction=='Start':
        nextaction=startmenu(Tela_Inicial)
    
    elif nextaction=='Play':
        nextaction=jogar(Tela_Jogar)
    
    elif nextaction=='Help':
        nextaction=ajuda(Tela_Ajuda)
        
    elif nextaction=='Options':
        nextaction=opcoes(Tela_Opcoes)
    
    
    
    
    