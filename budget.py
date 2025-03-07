list_revenu = []
list_depense = []
def revenu():
    montant = float(input("Entrez le montant du revenu: "))
    list_revenu.append(montant)
    sum_revenu = sum(list_revenu)
    return sum_revenu
    
def depense():
    montant = float(input("Entrez le montant du revenu: "))
    categorie = input("Nourriture, loyer, transport, etc: ")
    print("✅ Dépense ajoutée avec succès !")
    
