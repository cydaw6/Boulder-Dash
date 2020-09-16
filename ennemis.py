#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ce module comprend les fonctions qui sont en rapport avec la gestion des ennemis (rochers, lucioles, etc..)

"""


__all__ = ['eboulement']

def eboulement(grille):
    
    """
    Pour chaque case de le grille de jeu, si la case est celle d'un rocher, met en place son éboulement, 
    si les conditions requise sont réunis
    
    :param list grille: grille des cases du jeu
    :return: la nouvelle grille, `etatCase` , et un booléen si le joueur se retrouve écrasé, `joueurEcrase`
    """

    joueur = ['R1','R2','R3','R4']
    objetEboulement = ['D','B']
    
    joueurEcrase = False
    a = 0
    b = 0

    for y in range(len(grille)):
        
        for x in range(len(grille[y])):

            if grille[y][x][2] in objetEboulement:

                if grille[y][x][2] == 'B':
                    objet = 'B'
                elif grille[y][x][2] == 'D':
                    objet = 'D'

                if grille[y+1][x][2] == '.' and grille[y+2][x][2] in joueur : # verif d'abord si sous le rocher se trouve un vide et sous le vide, le joueur
                    joueurEcrase = True
                    a = 2
                    b = 0

                elif grille[y+1][x][2] == '.': # verif si sous le rocher se trouve un vide
                    a = 1
                    b = 0

                elif grille[y+1][x+1][2] == '.' and grille[y+1][x][2] == objet and grille[y][x+1][2] == '.':
                    a = 0
                    b = 1

                elif grille[y+1][x-1][2] == '.'  and grille[y+1][x][2] == objet and grille[y][x-1][2] == '.':
                    a = 0
                    b = -1
                else:
                    continue

                grille[y][x] = (grille[y][x][0],grille[y][x][1],'.')
                grille[y+a][x+b] = (grille[y+a][x+b][0],grille[y+a][x+b][1],objet)
    
    return joueurEcrase
