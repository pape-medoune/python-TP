
"""
    Auteur : Mouhamedoune FALL
    LGI3 (option génie logiciel)
    Professeur: Monsieur Diouf
    UNIVERSITE IBA DER THIAM DE THIES
    Année académique: 2023 / 2024
"""


#Going to do the first Exercise
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
#First Exercise done


#Exercice 2

#Part 1
def users_bank_trie_croissant(comptes):
    valid_accounts = [account for account in comptes if 'epargne' in account]

    if valid_accounts:
        min_account = valid_accounts[0]

        for account in valid_accounts[1:]:
            if 'epargne' in account and account['epargne'] < min_account.get('epargne'):
                min_account = account

    return "{" + min_account.get('nom') + "," + str(min_account.get('epargne')) + "}"


#Part 2
def users_bank_trie_decroissant(comptes):
    valid_accounts = [account for account in comptes if 'epargne' in account]

    if valid_accounts:
        max_account = valid_accounts[0]

        for account in valid_accounts[1:]:
            if 'epargne' in account and account['epargne'] > max_account.get('epargne'):
                max_account = account

    return "{" + max_account.get('nom') + "," + str(max_account.get('epargne')) + "}"

#Exercice 2 done


#Exercice 3
def sommeDeDeuxListe(L1, L2):
    nbr1 = ""
    nbr2 = ""

    for i in range(0, len(L1)):
        nbr1 = nbr1 + str(L1[i])

    for i in range(0, len(L2)):
        nbr2 = nbr2 + str(L2[i])

    return int(nbr1) + int(nbr2)

#Exercice 3 done

#Exercice 4
def somme_couple(T1, indice):
    tab2 = []
    k = 0
    for i in range(0, len(T1)):
        for j in range(0, len(T1)):
            res = T1[i] + T1[j]
            k = k + 1
            if res == indice:
                tab2.append((i, j))
    return tab2


#Exercice 4 done



#Exercice 5
def max_distance (sieges):
    for i in range(2, len(sieges)-2):
        if(sieges[i] == 1):
            if(sieges[i-2] == 0 and sieges[i-1]==0 and sieges[i+1]==0 and sieges[i+2]==0 or sieges[i+3]==0 or sieges[i-3]==0):
                emplacement_libre = i
    return emplacement_libre

#Exercice 5 done

if __name__ == '__main__':
    comptes = [
        {'nom': 'Diouf', 'prenom': 'Modou', 'epargne': 2500},
        {'nom': 'Sene', 'prenom': 'Pathé', 'epargne': 5000},
        {'nom': 'Ngom', 'prenom': 'Khadim', 'epargne': 10000},
        {'nom': 'Ndiaye', 'prenom': 'Fatou', 'epargne': 1250},
        {'nom': 'Mbengue', 'prenom': 'Alice', 'epargne': 2500},
        {'nom': 'Déme', 'prenom': 'Maty'},
        {'nom': 'Ngom', 'prenom': 'Satou', 'epargne': 4530},
        {'nom': 'Thioune', 'prenom': 'Ameth', 'epargne': 2200}
    ]


    # Test for the first exercise

    number = int(input("Entrer un nombre:"))

    res = trouverUneCombinaison(number)

    print(res)

    # Test for the first exercise done sucessfully


    #Test for the second exercise

    """ Part 1 """
    res1 = users_bank_trie_croissant(comptes)

    print(res1)

    """ Part 2 """
    res2 = users_bank_trie_decroissant(comptes)

    print(res2)

    # Test for the second exercise done successfully


    # Test for the third exercise

    """ Part 1 """
    L1 = [1, 2, 3]
    L2 = [4, 5, 6]

    sommeTwoList = sommeDeDeuxListe(L1, L2)

    print(f"La somme des deux liste est {sommeTwoList}")

    # Test for the third exercise done successfully



    # Test for Exercises 4

    tabTest = [-1, -2, -3, 2, 1, 3]
    sc=[]
    ind = int(input("Entrer l'indice pour somme_couple"))
    print(f"Tableau apres avoir fait la somme des couple avec l'indice {ind}")
    sc = somme_couple(tabTest, ind)

    print(list(set(tuple(sorted(sc)) for sc in sc)))
 
    # Test for Exercises 4 done


    # Test for Exercises 5


    print("Exericeee 5 ! ")

    

    # Initialisation de mon tableau
    sieges = [0, 1, 0, 0, 1, 0, 0, 0, 1]
    
    #Test de l'exercice numéro 5

    libre = max_distance(sieges)

    print(f"L'emplacement libre est {libre}")

    # Test for Exercises 5 done