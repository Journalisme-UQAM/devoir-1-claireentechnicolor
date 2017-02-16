#coding: utf-8

# Tu n'étais pas loin, Claire.
# Malheureusement, ton script ne fonctionne pas, car rien n'est indenté.
# Une boucle ne produit son effet que sur les lignes indentées se trouvant en-dessous.

for i in range(1931,2018): # Ne pas mettre d'espace avant les deux-points; je demandais de commencer en 1930 aussi (c'est le dernier terme, dans un intervalle, qui n'est pas inclus dans celui-ci) :)

	# Ensuite, ce qui se trouve sous un "for" doit être indenté afin d'être exécuté par la boucle

	for j in range(0,1000):

		# Indentation ici aussi
		# Une boucle imbriquée dans une autre -> bonne idée

		print (str(i)[2:] + format(j, "03d")); # Ce «print» fonctionne; il faut simplement enlever l'espace après «print» et avant la parenthèse par convention et souci de cohérence (il n'y en a pas entre «range» et la parenthèse qui suit, alors que «range» et «print» sont tous deux des fonctions)