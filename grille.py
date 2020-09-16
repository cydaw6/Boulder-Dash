#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Ce module comprend les fonctions qui sont en rapport avec la gestion et l'affichage de la grille de jeu
"""


from upemtk import *
from donnees import *
from personnage import *
from time import sleep
import os


__all__ = ['construction_grille','compteurEtPosition',
            'compteurEtPosition','affichage_grille',
            'finPartie','scrolling','barreInfo']


def construction_grille(niveau):
    """
    prend les lignes de sprites (mots) du niveau (une chaîne) en entrée 
    et les met dans la grille (liste)
    
    
    :param str niveau: la chaine de caractère décrivant le niveau
    :return: une liste de listes avec l'etat de chaque case du niveau, la ``grille`` 
    """
    
    lignes=niveau.split()
    
    grille=[]
    ligne=[]

    countL=0
    countC=0
    
    for colonnes in lignes:
        ligne =[]
        for sprite in colonnes:

            ligne.append((str(countL),str(countC),sprite))
            
            countL+=1
            
        grille.append(ligne)
        
        countC += 1
        countL = 0
        
    return grille


def compteurEtPosition(grille,objet):
    
    """
    Cette fonction récupère un objet, et renvoi sont nombre total dans la grille du jeu.
    - Si l'objet est le personnage avant, le jeu, 'R' (renvoi ses coordonnées), ou la sortie 'E', vérifie 
    qu'il sont en quantité fixe, soit 1 chacun.
    
    """
    
    etatCase=list(grille)
    pos_x,pos_y = 0,0
    count = 0
    
    
    for y in range(len(etatCase)):
        
        for x in range(len(etatCase[y])):
            
            (pos_case_x,pos_case_y,etat)=etatCase[y][x]
            
            if etat == objet:
               pos_x,pos_y =x,y
               count+=1
    
    if objet == 'D':
        return count
               
    if objet == 'E':
        assert count == 1, 'Il doit y avoir une seule et unique sortie dans le niveau'
        
    elif objet == 'R':
        assert count == 1, 'Il doit y avoir un seul et unique sprite joueur sur le niveau'
        
    return (pos_x,pos_y)
    

def affichage_grille(grille,largeur,hauteur):
    """
    affiche colonne par colonne, ligne par ligne le sprite qui correspond, au caractère lu.
    
    :param list grille: grille de l'état des cases du jeu
    :param int largeur: largeur de la fenêtre
    :param int hauteur: hauteur de la fenêtre
    """

    numLigne = 0
    
    for ligne in grille:
        
        numColonne = 0
        
        rockfordDirection = ['R1','R2','R3','R4']
        
        for element in ligne:
            
            
            x = int(element[0]) * taille_case
            y = int(element[1]) * taille_case + taille_case
            
            etat = element[2]
            
            if x >= 0 and x <= largeur and y >= taille_case and y <= hauteur : # n'affiche pas les images en dehors de la fenêtre ou sous la barre d'info
            
            
                if etat == 'G':
                    image(x,y, terre, ancrage='nw', tag='')
                    
                elif etat == 'D':
                    image(x,y, diamant, ancrage='nw', tag='')
            
                elif etat == 'W':
                    image(x,y, bordure, ancrage='nw', tag='')
                    
                elif etat == 'B':
                    image(x,y, rocher, ancrage='nw', tag='')
                
                elif etat == 'T':
                    image(x,y, mur, ancrage='nw', tag='')
                
                elif etat == 'R1':
                    image(x,y, r1, ancrage='nw', tag='')
                        
                elif etat == 'R2':
                    image(x,y, r2, ancrage='nw', tag='')
                        
                elif etat == 'R3':
                    image(x,y, r3, ancrage='nw', tag='')
                        
                elif etat == 'R4':
                    image(x,y, r4, ancrage='nw', tag='')
                        
                elif etat == 'E' or etat == 'EF' :
                    image(x,y, sortieF, ancrage='nw', tag='')
                    
                elif etat == 'ET':
                    image(x,y, sortieT, ancrage='nw', tag='')
                    
               
                
            
            numColonne+=1
        numLigne+=1
        
    return 1


def finPartie(largeur,hauteur,ecrase,gagne,timeout):
    """
    Gère l'affiche quand le joueur perd et le reset potentiel
    """
    
    while gagne == True or ecrase == True or timeout == True:
        efface_tout()
        
        if gagne == True:
            
            rectangle(0, 0, largeur, hauteur,couleur='Grey', remplissage='Grey', epaisseur=1, tag='')
            texte(largeur//2,hauteur//2,"Gagné!","White","center")
            texte(largeur//2+100,hauteur//2+75,"reset [r] ","White","center", police="Purisa", taille=15)
            texte(largeur//2-100,hauteur//2+75,"quitter [q] ","White","center", police="Purisa", taille=15)
            
        elif ecrase == True or timeout == True:
            rectangle(0, 0, largeur, hauteur,couleur='black', remplissage='black', epaisseur=1, tag='')
            texte(largeur//2,hauteur//2,"Perdu!","Red","center")
            texte(largeur//2+100,hauteur//2+75,"reset [r] ","White","center", police="Purisa", taille=15)
            texte(largeur//2-100,hauteur//2+75,"quitter [q] ","White","center", police="Purisa", taille=15)
        
        mise_a_jour()
        
        ev = ''
        tev =''
        ev = donne_evenement()
        tev = type_evenement(ev)
        
        
        if tev == 'Touche' and touche(ev) == 'r': 
            return True 
        elif tev == 'Touche' and touche(ev) == 'q': 
            return False


def scrolling(grille,direction):
  
    """
    Pour chaque case, si la case n'est pas celle du joueur, modifie ses coordonées vers le sens opposée à celui du déplacement.
    
    :param list grilleJ: la liste des case
    :param str direction: la direction choisi par le joueur
    :param bool verifDeplace:
    :return: la grille (list), `grille`
    """
    joueur = ['R1','R2','R3','R4']
    a = 0
    
    
    if direction == 'droite' or direction == 'bas':
        a = -1
    elif direction == 'gauche' or direction == 'haut':
        a = 1
    
    lng = len(grille)
    
    for y in range(lng):
        for x in range(len(grille[y])):
                
            if grille[y][x][2] not in joueur:
        
                ligneY = grille[y]
        
                pos_case_x = int(ligneY[x][0])
                pos_case_y = int(ligneY[x][1])
                etat = ligneY[x][2]
    
                
            if direction == 'droite' or direction == 'gauche':
                ligneY[x] = (str(pos_case_x+a),str(pos_case_y),etat)
                    
            elif direction == 'haut' or direction == 'bas':
                    
                ligneY[x] = (str(pos_case_x),str(pos_case_y+a),etat)
                    
    

def barreInfo(diamantsRequis,nbDiamant,countDown,coefscore):
    
    """
    Affiche à l'écran les infos du niveau en cours, le nombre de diamants récupéré, sur le nombre total de diamants, et les points
    
    """
    a = 10

    rectangle(0, 0, largeur, taille_case,couleur='black', remplissage='black', epaisseur=1, tag='')
    rectangle(0, taille_case, largeur, taille_case+2,couleur='chocolate2', remplissage='chocolate2', epaisseur=1, tag='')
    
    image(a, 0, diamant, ancrage='nw', tag='')
    texte(a+62, 0, str(nbDiamant),couleur='cyan2', ancrage='nw', police="Purisa", taille= int(taille_case * 0.75), tag='')
    
    texte(a+62+longueur_texte(str(nbDiamant)), 16, '   /'+str(diamantsRequis),couleur='White', ancrage='nw', police="Purisa", taille=25, tag='')
    
    texte(largeur/2-longueur_texte(str(countDown)), 0, str(countDown), couleur='White', ancrage='nw', police="Purisa", taille=int(taille_case * 0.75), tag='')

    b = largeur-taille_case
    
    texte(b, 0,'score : '+str(nbDiamant*coefscore),couleur='White', ancrage='ne', police="Purisa", taille=int(taille_case * 0.75), tag='')
    
    image(b, 0, iconeScore, ancrage='nw', tag='')
    
          



    
  
