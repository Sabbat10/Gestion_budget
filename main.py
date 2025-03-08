from budget import revenu, depense, resume, list_revenu, list_depense

while True:
    
    print("\n=== Gestionnaire de Budget ===")
    print("1. Ajouter un revenu")
    print("2. Ajouter une dépense")
    print("3. Voir le résumé")
    print("4. Quitter")
    
    choix_option = input("Choisissez une option: 1 - Revenu, 2 - Dépense, 3 - Bilan, 4 - Quitter: ")
    
    if choix_option == "1":
        revenu()
        
    elif choix_option == "2":
        depense()
        
    elif choix_option == "3":
        resume()
        
    elif choix_option == "4":
        print("Vous avez quitté le programme")
        break
