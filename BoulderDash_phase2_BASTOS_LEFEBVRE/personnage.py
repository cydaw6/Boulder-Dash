#!/usr/bin/env python
# -*- coding: utf-8 -*-

from upemtk import *
from grille import *
from time import sleep



__all__ = ['mise_a_jour_direction','effaceDeplacementPerso',
            'deplacementPerso','persoSortie']




"""
Ce module comprend les fonctions qui sont en rapport avec le personnage; le choix du joueur sur sa direction, son déplacement, les contraintes qu'il subit, etc...

"""


def mise_a_jour_direction(direction,vardebug,debug):
    """
    Prend en entrer la direction et la change en retournant la nouvelle selon l'événement capturé.
    
    :param direction str: direction précédente 
    :return: nouvelle direction (str)
    
    """
    nouvelle_dir=direction
    ev=donne_evenement()
    type_ev=type_evenement(ev)
    if type_ev=="Touche":
        t=touche(ev)
        if t=="Right":
            nouvelle_dir='droite'
        elif t=="Left":
            nouvelle_dir='gauche'
        if t=="Up":
            nouvelle_dir='haut'
        elif t=="Down":
            nouvelle_dir='bas'
        if t=='Escape':
            exit()
                    
        elif t=="d":
            vardebug+=1
                    
            if vardebug % 2 == 0:
                debug = True
            else:
                debug = False

        
    return nouvelle_dir,vardebug,debug


def effaceDeplacementPerso(direction,grille,posx,posy):
    
    """ 
    Vérifie si la case en rapport avec la nouvelle direction est correcte, et s'il déplace ou non un rocher.
    Si oui, efface la case ou se trouve le joueur (et potentiellement celle du rocher).
    
    :param str direction: la nouvelle direction
    :param list grille: grille de l'état des cases du jeu
    :param int posx: position x de la case du joueur
    :param int posy: position y de la case du joueur
    """
    
    pos=0
    x,y = posx,posy
    
    
    infranchissable = ['W','B','T'] #direction haut et bas
    infranchissable2 = ['W','T'] #direction droite et gauche
    
    verifDeplace = False
    VerifDeplaceRocher = False
    
    
    ligneY = grille[y]
    
    if direction == 'droite' or direction == 'bas':
        a = 1
    elif direction == 'gauche' or direction == 'haut':
        a = -1
    
    if direction == 'droite' or direction == 'gauche':
        
        if ligneY[x+a][2] not in infranchissable2:    
            if ligneY[x+a][2] == 'B': # si la case de déplacement est un rocher
                        
                        
                if ligneY[x+a*2][2] == '.' : # si la case après le rocher est vide
                            
                            
                    ligneY[x+a] == (ligneY[x+a][0],ligneY[x+a][1],'.') # rend vide la case du rocher
                    VerifDeplaceRocher =True
                else:
                    return verifDeplace, VerifDeplaceRocher
                        
                        
            ligneY[x] = (ligneY[x][0],ligneY[x][1],'.') # rend vide la case du joueur
            verifDeplace = True
                    
    
    elif direction == 'haut' or direction == 'bas':
        
        if grille[y+a][x][2] not in infranchissable:
            ligneY[x] = (ligneY[x][0],ligneY[x][1],'.')
            verifDeplace = True
        
    return  verifDeplace, VerifDeplaceRocher
    
    
    
def deplacementPerso(direction,grille,posx,posy,verifDeplace,VerifDeplaceRocher,nbDiamant,decompte):
    """ 
    Si le déplacement est confirmé, remplace l'état de la case en rapport avec la nouvelle direction
    par celle du joueur (Rockford) (et celle d'après par un rocher s'il en déplace un).
    - Incrémente +1 si le joueur efface une case avec pour état un diamant.
    
    :param str direction: la nouvelle direction
    :param list grille: grille de l'état des cases du jeu
    :param int posx: position x de la case du joueur
    :param int posy: position y de la case du joueur
    :param bool verifDeplace: autorisation de déplacement du joueur
    :param bool VerifDeplaceRocher: autorisation de deplacement du rocher
    :param int nbDiamant: nombre de diamants récolté
    :return: la nouvelle grille `grillefonc` les positions du joueur `x` et `y` et le nouveau nombre de diamants possedé `nbDiams`
    """
    
    x,y = posx,posy
    nbDiams = nbDiamant
    ligne = grille[y]
    
    
    d = 'R4'
    
    if verifDeplace == True:
    
        if direction == 'droite':
            d = 'R1'
        elif direction == 'gauche':
            d = 'R2'
        elif direction == 'haut':
            d = 'R3'
      
            
        if direction == 'droite' or direction == 'bas':
            a = 1
        elif direction == 'gauche' or direction == 'haut':
            a = -1
            
            
        if direction == 'droite' or direction == 'gauche':
            
            if ligne[x+a][2] == 'D': # si case de déplacement est un diamant, nombre de diamant possedé +1
                decompte += diamantAddTime
                nbDiams += 1
            
            if VerifDeplaceRocher == True:

                ligne[x+a*2] = (ligne[x+a*2][0],ligne[x+a*2][1],'B') # place un rocher sur la case après le joueur
                    
            ligne[x+a] = (ligne[x+a][0],ligne[x+a][1],d) # place le joueur sur la case après l'ancienne position
            
            x,y=x+a,y
            
            
        elif direction == 'haut' or direction == 'bas':
            
            ligne = grille[y+a]
                
            if ligne[x][2] == 'D':
                decompte += diamantAddTime
                nbDiams += 1
            
            ligne[x] = (ligne[x][0],ligne[x][1],d)
                
            x,y=x,y+a
            
    else:
        ligne[x] = (ligne[x][0],ligne[x][1],d)
            
    return x,y, nbDiams,'',decompte


def persoSortie(posx,posy,posSortie,nbDiamant,diamantsRequis,grille):
    
    """ 
    Retourne True si le joueur est sur la sortie, False sinon.
    
    :param int posx: position x du joueur
    :param int posy: position y du joueur
    :param tuple posSortie: couple des coordonnées de la sortie
    :return: bool

    """
    

    etatSortie = 'EF'
    persoSort = False

    (sx,sy) = posSortie
    
    v1 = grille[sy][sx][0]
    v2 = grille[sy][sx][1]
    


    if nbDiamant >= diamantsRequis:
        etatSortie = 'ET'
        if (posx,posy) == posSortie:
            persoSort = True

    else:
        etatSortie = 'EF'
            

    grille[sy][sx] = (v1,v2,etatSortie)

    return persoSort
    
    
def persoEcrase(posx,posy,grille):

    if grille[posx-2][posy][2] == 'B':
        return True
    return False
