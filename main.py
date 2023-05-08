if __name__ == '__main__':
    def myfonction(nom):
        print("Bonjour " + nom)

    # myfonction("Fleury")

    # Les collections
    """
    1. Les listes[]
    2.Les tuples()
    3.Les sets{}
    4.Les dictionnaires{}
    
    """
    # dictionnaire
    students = {
        "nom": "IRAKOZE",
        "prenom": "Yves",
        "adresse": ["kinanira", "kibenga"],
        "tel": "75222152"
    }
    print('--------------------Affichage des cles ---------------\n')
    for s in students.keys():
        print(s)

    print('\n--------------------Affichage des valeurs ---------------\n')

    for s in students.values():
        print(s)

    print('\n--------------------Affichage des cles et des valeurs ---------------\n')

    for k, v in students.items():
        print(f"{k} : {v}")

    # les sets (n'acceptent pas  la duplicztion contrerement aux listes)
    # fruits = {'Mangue', 'Banane', 'Avocat', 'Mangue'}
    jours = {"Lundi", "Mardi", "Mercredi",
             "Jeudi", "Vendredi", "Samedi", "Dimanche"}

    # print('----------Affichage des jours---------------\n')

    # for j in jours:
    #     print(j)

    # Les listes
    fruits = ['Mangue', 'Banane', 'Avocat']

    # print('--------------------Affichage avant ajout du nouveau élement---------------\n')

    # for f in fruits:
    # print(f)

    # fruits.append('Pasteque')
    # fruits.insert(0, "pasteque")

    # print('--------------------Affichage avant apres du nouveau element---------------\n')

    # print(fruits)

    print('\n--------------------FIN*-------------------')
