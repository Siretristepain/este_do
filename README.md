# este_do

Le but de ce depot est de créer un mini-jeu basé sur le principe du cluedo.
Pour l'instant j'en suis à une V1.

Un tableau récapitule les 6 suspects, les 6 armes et les 6 lieux possibles. 

Au début de la partie, un meurtrier, une arme et un lieu sont tirés au hasard (à trouver).

Le joueur émet une hypothèse à chaque tour. Si elle est fausse, un contre exemple lui est dévoilé et est donc rayé du tableau. 
Ex : si le joueur propose Esteban avec la corde dans le couloir et que tout est faux, l'ordi vas aléatoirement lui montrer soit 'esteban' soit 'corde' soit 'couloir'. Admettons qu'il lui montre 'couloir', ce dernier disparaitra du tableau récapitulatif.

## A FAIRE

- Pour rendre le jeu un peu plus challenge, il faudrait instaurer un système de tour. Par exemple le joueur n'aurait que 10 tours pour trouver la bonne combinaison.

- Il faudrait aussi mettre au point une gestion des erreurs et des majuscules.
