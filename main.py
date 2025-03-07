from budget import revenu, depense, list_revenu

while True:
    
    print("\n=== Gestionnaire de Budget ===")
    print("1. Ajouter un revenu")
    print("2. Ajouter une dépense")
    print("3. Voir le résumé")
    print("4. Quitter")
    
    choix_option = input("Choisissez une option: 1 - Dépense, 2 - Revenu, 3 - Bilan, 4 - Quitter: ")
    
    if choix_option == "1":
        print(f"Revenu ajouté: {revenu()}$")
        print(list_revenu)
        
    elif choix_option == "2":
        depense()
        
    elif choix_option == "3":
        print("Voir le résumé")
    elif choix_option == "4":
        print("Quitter")
        break
