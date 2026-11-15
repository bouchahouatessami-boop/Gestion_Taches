#  saisir le nombre des taches
def saisir_N():
    n = int(input("donner le nombre des tâches"))
    while not(n > 0):
        n = int(input("redonner le nombre des tâches"))
    return n

#  saisir la liste des taches
def saisir_les_taches(n):
    ch = ""
    for i in range(n):
        ch += f"la NOTE N°{i} est : " + input(f"donner la tâche N°{i} ") + "\n"
    return ch
# ajouter une tache 
def ajouter_tache(ch):
    titre = input("Titre de la tâche : ")
    num= len(ch.split("\n")) - 1
    ch += f"la NOTE N°{num} est : {titre}\n"
    print("Tâche ajoutée avec succès.")
    return ch

# afficher une tache 
def afficher(ch):
    print("\n--- LISTE DES TACHES ---")
    print(ch)

# rchercher si une tache exciste ou nn
def rechercher(ch):
    pass
# GESTION DES TACHES ET DES COMMANDES
def service(ch):
    while True :
        print("\n=== GESTION DES TACHES ===")
        print("0. Quitter")
        print("1. Ajouter une tache")
        print("2. Afficher ")
        print("3. Rechercher")

        choix= int(input("taper votre choix."))
   
        
        if choix== 0:
            print ("au revoir")
        elif choix == 1:
            ch=ajouter_tache(ch)
        elif choix == 2:
            afficher(ch)   
        elif choix == 3:
            rechercher(ch)
        else:
            print("Choix invalide !")
       
#--- PROGRAMME PRINCIPALE ---
n = saisir_N()
ch = saisir_les_taches(n)
service(ch)