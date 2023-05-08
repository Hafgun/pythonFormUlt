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
        "adresse": ["kinanira", "kibenga"]
    }

    # print(type(students))

    # les sets (n'acceptent pas  la duplicztion contrerement aux listes)
    # fruits = {'Mangue', 'Banane', 'Avocat', 'Mangue'}

    # Les listes
    fruits = ['Mangue', 'Banane', 'Avocat']

    print('--------------------Affichage avant ajout du nouveau élement---------------\n')

    for f in fruits:
        print(f)

    # fruits.append('Pasteque')
    fruits.insert(0, "pasteque")

    print('--------------------Affichage avant apres du nouveau element---------------\n')

    print(fruits)

    print('\n--------------------FIN*-------------------')
