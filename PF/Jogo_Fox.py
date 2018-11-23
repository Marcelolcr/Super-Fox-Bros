# -*- coding: utf-8 -*-
"""
Created on Tue May  1 13:12:43 2018

@author: Thomas, Marcelo e Paulo
"""

import pygame,sys

from Fox_StartMenu import startmenu
from Fox_help import ajuda
from Fox_options import opcoes
from Fox_fases import fases
from Fox_play import jogar
from Fox_play2 import jogar2

pygame.init()

buttonsound = 1


Tela_Inicial = "Fundo_top3.png"
Tela_Ajuda= "Ajuda.png"
Tela_Opcoes="Conf.png"
Tela_Fases= "Fundo fases3.png"
Tela_Jogar2="aviaao.PNG"
Tela_Jogar="oriprop.png"

nextaction = "Start"

effect = pygame.mixer.Sound('click.wav')
effect.set_volume(buttonsound)

somjogo = pygame.mixer.Sound('Fundo.wav')
somjogo.play(-1)

#Sons efeitos bandeira
acabou =  pygame.mixer.Sound('acabou.wav') #1afase
acabou.set_volume(buttonsound)
burro =  pygame.mixer.Sound('chaves.wav')
burro.set_volume(buttonsound)
bazinga =  pygame.mixer.Sound('bazinga.wav')
bazinga.set_volume(buttonsound)
victory =  pygame.mixer.Sound('ganhou.wav') #2a fase
errou =  pygame.mixer.Sound('faustao-errou.wav')


gamesound = 0.2 ############## Som de fundo
nenemy=0
#try:
while True:

    somjogo.set_volume(gamesound)

    if nextaction=='ExitGame':
        pygame.display.quit()
        pygame.quit() 
        break
    elif nextaction=='Start':
        nextaction=startmenu(Tela_Inicial,effect,buttonsound)
     
    elif nextaction=='Play':
        nextaction=jogar(Tela_Jogar,effect,buttonsound,nenemy,acabou,burro,bazinga)
        
    elif nextaction=='Play2':
        nextaction=jogar2(Tela_Jogar2,effect,buttonsound,nenemy,victory,errou)
                
    elif nextaction=='Help':
        nextaction=ajuda(Tela_Ajuda,effect,buttonsound)
        
    elif nextaction=='Fases':
        nextaction,Tela_Jogar,nenemy=fases(Tela_Fases,effect,buttonsound)
        
    elif nextaction=='Options':
        nextaction,buttonsound,gamesound=opcoes(Tela_Opcoes,effect,buttonsound,gamesound,somjogo)
        
#except:
 #   pygame.quit()
#    print("deu merda irmaum")

try:
    sys.exit()
except SystemExit:
    pass