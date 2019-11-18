#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

##### constantes utilisée pour le jeu #####

taille_case = 48

largeur = 1024
hauteur = 576



diamantsRequis = 5
diamantAddTime = 5
coefscore = 10
posibiliteDirection = ['droite','gauche','haut','bas']



###--- parametres niveau aléatoire

# a,b : largeur/hauteur du niveau

a,b = 25,10 ## attention certaines valeurs ne fonctionnent pas (pas encore corrigé)


#pourcentages pour chaque type de blocs dans le niveau aleatoire

pTerre = 75
pDiamant = 3
pRocher = 15
pMur = 7

###--- //





######-- -- chemins
#-- images

r1=os.path.join(os.getcwd(),"images"+str(taille_case),'rockfordD.png')
r2=os.path.join(os.getcwd(),"images"+str(taille_case),'rockfordG.png')
r3=os.path.join(os.getcwd(),"images"+str(taille_case),'rockfordH.png')
r4=os.path.join(os.getcwd(),"images"+str(taille_case),'rockford.png')

bordure = os.path.join(os.getcwd(),"images"+str(taille_case),'bordure.png')
terre = os.path.join(os.getcwd(),"images"+str(taille_case),'terre.png')
rocher = os.path.join(os.getcwd(),"images"+str(taille_case),'rocher.png')
diamant = os.path.join(os.getcwd(),"images"+str(taille_case),'diamant.png')
sortieT = os.path.join(os.getcwd(),"images"+str(taille_case),'sortieT.png')
sortieF = os.path.join(os.getcwd(),"images"+str(taille_case),'sortieF.png')
mur = os.path.join(os.getcwd(),"images"+str(taille_case),'bois.png')
iconeScore = os.path.join(os.getcwd(),"images"+str(taille_case),'iconescore.png')
#chemin des images rockford directement dans la fonction d'affichage

#-- niveaux
n1 = os.path.join(os.getcwd(),"niveaux",'n1.txt')









###########################################



