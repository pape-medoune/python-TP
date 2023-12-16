

#First Exercise Done
def trouverUneCombinaison(number):
    tableau = []

    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                if i + j + k == number:
                    combination = tuple(sorted((i, j, k)))
                    if combination not in tableau:
                        tableau.append(combination)

    return tableau

#Going to the  second Exercise
def users_bank_trie_croissant(tableau):
    comptes = [{'nom': 'Diouf', 'prenom': 'Modou', 'epargne': 2500},
               {'nom': 'Sene', 'prenom': 'Pathé', 'epargne': 5000},
               {'nom': 'Ngom', 'prenom': 'Khadim', 'epargne': 10000},
               {'nom': 'Ndiaye', 'prenom': 'Fatou', 'epargne': 1250},
               {'nom': 'Mbengue', 'prenom': 'Alice', 'epargne': 2500},
               {'nom': 'Déme', 'prenom': 'Maty'},
               {'nom': 'Ngom', 'prenom': 'Satou', 'epargne': 4530},
               {'nom': 'Thioune', 'prenom': 'Ameth', 'epargne': 2200}]


    return comptes.sort


if __name__ == '__main__':
    #number = int(input("Veuillez entrer un nombre pour faire la combinaison du jeu de dés:"))

    '''
        determinons le nombre de combinaison 
        pour faire le boucle
    '''
    comptes = [{'nom': 'Diouf', 'prenom': 'Modou', 'epargne': 2500},
               {'nom': 'Sene', 'prenom': 'Pathé', 'epargne': 5000},
               {'nom': 'Ngom', 'prenom': 'Khadim', 'epargne': 10000},
               {'nom': 'Ndiaye', 'prenom': 'Fatou', 'epargne': 1250},
               {'nom': 'Mbengue', 'prenom': 'Alice', 'epargne': 2500},
               {'nom': 'Déme', 'prenom': 'Maty'},
               {'nom': 'Ngom', 'prenom': 'Satou', 'epargne': 4530},
               {'nom': 'Thioune', 'prenom': 'Ameth', 'epargne': 2200}]

    print(comptes[0]['epargne'])

    #result = trouverUneCombinaison(number)
    #print(result)

    #print(tableau)

    #print("Hello Mouhamedoune")