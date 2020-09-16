

Lancer le main.py pour jouer.
debug : touche d

██████╗  ██████╗ ██╗   ██╗██╗     ██████╗ ███████╗██████╗     ██████╗  █████╗ ███████╗██╗  ██╗
██╔══██╗██╔═══██╗██║   ██║██║     ██╔══██╗██╔════╝██╔══██╗    ██╔══██╗██╔══██╗██╔════╝██║  ██║
██████╔╝██║   ██║██║   ██║██║     ██║  ██║█████╗  ██████╔╝    ██║  ██║███████║███████╗███████║
██╔══██╗██║   ██║██║   ██║██║     ██║  ██║██╔══╝  ██╔══██╗    ██║  ██║██╔══██║╚════██║██╔══██║
██████╔╝╚██████╔╝╚██████╔╝███████╗██████╔╝███████╗██║  ██║    ██████╔╝██║  ██║███████║██║  ██║
╚═════╝  ╚═════╝  ╚═════╝ ╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝                                                                                              
				     Par Bastos Antoine et Lefebvre Timothée  Dut info 1 - TDA 



I. Organisation du programme.
II. Choix techniques.
III. Problèmes recontrés.


╦
║
╩./-// ORGANISATION DU PROGRAMME //-/
 

Le programme du jeu est organisé est découpé en plusieurs parties - modules -:

- Le main: 	 Met en place le programme.

- Le jeu: 	 Met en relation les différentes fonctions nécessaires au bon fonctionnement du jeu (boucle du jeu).

- La grille:	 Regroupe les fonctions qui sont en rapport avec la gestion et l'affichage de la grille de jeu.

- Le personnage: Regroupe les fonctions qui sont en rapport avec le personnage; 
		 le choix du joueur sur sa direction, son déplacement, les contraintes qu'il subit, etc...

- Les ennemis: 	 Regroupe les focntions en rapport avec les ennemis (rochers,lucioles, etc...)

- Les données:	Regroupe les constantes du jeu.

- upemtk: 	Module graphique de l'UPEM qui repose sur le module tkinter.

+ un fichier images avec les sprites du jeu.


╦╦
║║
╩╩. /-// CHOIX TECHNIQUES //-/

	° Le niveau est définit par une chaine de caractères qui est interprétée
	par le programme après avoir été transformé en liste (ligne) de listes (cases) par une fonction.

	° Chaque case est un triplet de type tuple, avec (la position x de la case, la position y de la case, et l'etat de la case);
	où l'état de la case est définit au départ selon le caractère associé dans la chaine de caractère.
	
	° Grâce au triplet formé par les propriétés de la case, un défilement du niveau a été mis en place en 
	fonction du déplacement du joueur, ce qui donne l'impression qu'une caméra suit le personnage.

	° Le défilement, permet également de se déplacer dans des niveaux d'une taille un peu plus importante.
	En effet l'affichage des images de tous les élements, prend beaucoup de ressources en vidéo, et ralentit le programme.
	Ici, on affiche les images seulement des cases dont les coordonnées se trouvent à l'intérieur de la fenêtre.

	° La touche pour le debug est d, et Echap ferme instantanément la fenêtre si besoin.

	° Pour la première phase, l'éboulement en vertical et latéral, en cascade a été mis en place.

╦╦╦
║║║
╩╩╩. /-// Problèmes recontrés //-/


	° Afin d'obtenir une certaine esthétique du jeu, il aurait été appréciable que le personnage de Rockford possède
	une animation lors de son déplacement (ce qui à été très partiellement implémenté ici, avec seulement l'affichage
	des images en rapport avec sa direction; droite, gauche, haut, bas/ne fait rien). Le roulement des frames de l'animation
	semblaient compliqué à mettre en place sans classes, - structure d'objet que nous n'avons pas encore abordé, et que nous 
	ne savions pas utiliser-.
