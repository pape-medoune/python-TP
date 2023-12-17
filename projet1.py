

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

#Going to do the  second Exercise

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

    """ PART 1 """
    res1 = users_bank_trie_croissant(comptes)

    print(res1)

    """ PART 2 """
    res2 = users_bank_trie_decroissant(comptes)

    print(res2)

    # Test for the second exercise done sucessfully




    # Test for the third exercise

    """ PART 1 """

    """ PART 2 """
    # Test for the third exercise done sucessfully



