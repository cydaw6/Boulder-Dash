#!/usr/bin/env python
# -*- coding: utf-8 -*-

from upemtk import cree_fenetre,rectangle
from donnees import largeur,hauteur
from grille import construction_grille
from jeu import jeu

if __name__ == '__main__':
    
    
    
    mode = ''
    
    mode = 'aleatoire'
    
    aleatoire = False
    
    if mode == 'aleatoire':
        
        aleatoire = True
        

        
        
    cree_fenetre(largeur,hauteur)
    rectangle(0, 0, largeur, hauteur,couleur='black', remplissage='black', epaisseur=1, tag='')

    jeu(largeur,hauteur,aleatoire)

    
