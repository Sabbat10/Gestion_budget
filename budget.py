# liste des revenus, dépenses et catégories
list_revenu = []
list_depense = []
list_categorie = []

# fonction pour ajouter un revenu
def revenu():
    
    try:
        montant = float(input("Entrez le montant du revenu: "))
        
        if montant <= 0:
            print("❌ Montant invalide")
        else:
            list_revenu.append(montant)
            sum_revenu = sum(list_revenu)
            
            print("\n")
            print(f"✅ Revenu ajouté avec succès ! : {sum_revenu}$")
            print(f"Solde actuelle: {sum(list_revenu) - sum(list_depense)}$")
            return sum_revenu
        
    except ValueError as e:
        print("❌ Entrez un momtant valide", e)
        return 0
    
# fonction pour ajouter une dépense
def depense():
    try:
        montant = float(input("Entrez le montant du depense: "))
        
        if montant >= sum(list_revenu):
            print("solde insuffisant")
            
        else:
            list_depense.append(montant)
            sum_depense = sum(list_depense)
            
            categorie = input("Nourriture, loyer, transport, etc: ")
            list_categorie.append(categorie)
            
            print("\n")
            print(f"✅ Dépense ajoutée avec succès ! : {list_depense}$")
            print(f"Solde actuelle: {sum(list_revenu) - sum(list_depense)}$")
            
            return sum_depense
    
    except ValueError as e:
        print("❌ Entrez un momtant valide", e)
        return 0
    

# fonction pour voir le résumé du budget
def resume():
    print("\n")
    print(f"Total des revenus: {sum(list_revenu)}$")
    print(f"Total des depenses: {sum(list_depense)}$")
    print(f"Solde actuelle: {sum(list_revenu) - sum(list_depense)}$")
    
    
    print("Liste des dépenses: ")
    for i in range(len(list_depense)):
        print(f"{list_categorie[i].upper()} - {list_depense[i]}$")
    
    print("\n")
    print("✅ Résumé affiché avec succès !")


def write_file():
    with open("expenses.txt", "w") as f:
        f.write("Liste des dépenses: \n")
        f.write(f"Total des revenus: {sum(list_revenu)}$\n")
        f.write(f"Total des depenses: {sum(list_depense)}$\n")
        f.write(f"Solde actuelle: {sum(list_revenu) - sum(list_depense)}$\n")
        
        for i in range(len(list_depense)):
            f.write(f"{list_categorie[i].upper()} - {list_depense[i]}$\n")