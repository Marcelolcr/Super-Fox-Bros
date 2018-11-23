# -*- coding: utf-8 -*-
"""
Created on Fri May 18 18:24:33 2018

@author: Thomas, Marcelo e Paulo
"""
import pygame
from pygame.locals import *
from matplotlib.pyplot import imread
from random import randrange

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
        self.sprites = self.dict['parado']
        self.image= self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.posyin=pos_y
        self.listaposicao=[self.rect,self.rect]
        self.velx=0
        self.vely=0
        self.isfalling=False
        self.check = True
        
    def change(self, action):
        if action == 'andando' and self.sprites!=self.dict['andando']:
            self.sprites = self.dict['andando']
            self.counter = -1
        if action == 'andandoesq' and self.sprites!=self.dict['andandoesq']:
            self.sprites = self.dict['andandoesq']
            self.counter = -1
        elif action == 'pulando' and self.sprites!=self.dict['pulando']:
            self.sprites = self.dict['pulando']
            self.counter = -1
        elif action == 'pulandoesq' and self.sprites!=self.dict['pulandoesq']:
            self.sprites = self.dict['pulandoesq']
            self.counter = -1
        elif action == 'morrendo' and self.sprites != self.dict['morrendo']:
            self.sprites = self.dict['morrendo']
            self.counter = -1
        
        elif action == 'parado' and self.sprites != self.dict['parado']:
            self.sprites = self.dict['parado']
            self.counter = -1

    def update(self):
        self.counter = (self.counter + 1) % len(self.sprites)
        self.image = self.sprites[self.counter]
        px=self.rect.x
        py=self.rect.y
        self.rect=self.image.get_rect()
        self.rect.x = px
        self.rect.y = py
        self.listaposicao.append(self.rect)
        del self.listaposicao[0]
        if self.listaposicao[1]==self.listaposicao[0]: pass    
        if self.check:
            if self.rect.y<self.posyin:
                self.isfalling=True
            else:
                self.rect.y=self.posyin
        else:
            self.check=True        
        if self.isfalling:
            self.vely=10
            self.rect.y+=self.vely 
        else:
            self.vely=0

class Wall(object): 
    def __init__(self, px, py, comp):
        self.rect = pygame.Rect(px,py, comp, 16)
        
        
class Goomba(pygame.sprite.Sprite):
    def __init__ (self, img, pos_x, pos_y, vel_x):
        pygame.sprite.Sprite.__init__(self)
        self.vx = vel_x
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        
    def move(self):
        self.rect.x += self.vx
    
    def change(self):
        if self.vx < 0:
            self.image = pygame.image.load('R2D2 Esquerda.png')
        else:
            self.image = pygame.image.load('R2D2 Direita.png')
            
    def update(self):
        self.move()
        self.change()
        
    def reset(self, largura):
        self.rect.x = randrange(60,largura)
        self.vx = abs(self.vx)
    
    
class R2D2(pygame.sprite.Sprite):
    def __init__ (self, img, pos_x, pos_y, vel_x):
        pygame.sprite.Sprite.__init__(self)
        self.vx = vel_x
        self.image = pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        
    def move(self):
        self.rect.x += self.vx
    
    def change(self):
        if self.vx < 0:
            self.image = pygame.image.load('Gomba_sprites2.png')
        else:
            self.image = pygame.image.load('Gomba_sprites2d.png')
            
    def update(self):
        self.move()
        self.change()
        
    def reset(self,largura):
        self.rect.x = randrange(60,largura)
        self.vx = abs(self.vx)


class Flag(pygame.sprite.Sprite):
    def __init__(self,img,pos_x,pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x=pos_x
        self.rect.y=pos_y


class Slider():
    def __init__(self, name, val, maxi, mini, x_pos,y_pos):
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        GREY = (200, 200, 200)
        ORANGE = (200, 100, 50)
        TRANS = (1, 1, 1)
        
#        pygame.font.init()
        font = pygame.font.SysFont("Courier New", 24)
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
#        font=0
#        pygame.font.quit()

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


