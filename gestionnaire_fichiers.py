import os 
import glob
import shutil

def menu():
    print("\n")
    print("======= GESTIONNAIRE DE FICHIERS ======== \n")
    print("1. Créer un fichier ")
    print("2. Supprimer un fichier")
    print("3. Lister les fichiers")
    print("4. Lire un fichier")
    print("5. Quitter")
    print("6. Renommer des dossiers")
    print("7. Ajouter du contenu dans un fichier")
    print("8. Vider un fichier")
    print("9. Copier un fichier")
    print("10. rechercher un fichier")
    print("11. créer des dossiers")
    print("12. Supprimer des dossiers \n")
    choix = input("votre choix : ")    
    liste_choix = ["1","2","3","4","5","6","7","8","9","10","11","12"]
    while choix not in liste_choix:
        choix = input("Veuiller entrer un nombre entre 1 et 12 : ")
    return choix
def creation():
    nom_fichier = input("Entrer le nom de votre fichier et l'extension du fichier : ") 
    message_fichier = input("Remplisser le contenu de votre fichier : ")
    if os.path.exists(nom_fichier) and os.path.isfile(nom_fichier):
        print("Désolé mais ce fichier existe déjà ⛔ ✖️  ⛔")
    else:
        with open(nom_fichier, "w") as f:
            f.write(message_fichier)
        print("Fichier créé avec succès ✅ 🥳 🎉")
def suppression():
    remove_file = input("Entrer le nom du fichier dont vous souhaiter supprimer : ")    
    if os.path.exists(remove_file) and os.path.isfile(remove_file):
        os.remove(remove_file)
        print("Fichier supprimé avec succès ✅ 🥳 🎉")
    else:
        print("Erreur de nom de fichier ⛔ ✖️  ⛔")
def liste():
    liste_doc = glob.glob("*")
    liste_tri = [file for file in liste_doc if os.path.isfile(file)]
    print("La liste de vos fichiers : ✅ 🥳 🎉")
    print("\n")
    for i in liste_tri:
        print(i," ,")
    print("\n")
    print("Nombres total de fichiers : ", len(liste_tri))
def lire():
    read_file = input("Entrer le nom du fichier : ")
    if os.path.exists(read_file) and os.path.isfile(read_file):
        with open(read_file, "r") as f:
            print(f.read())
        print("Fichier lu avec succès ✅ 🥳 🎉")
    else:
        print("Erreur de nom de fichier ⛔ ✖️  ⛔")
def renommer():
    liste_rep = ["oui","non"]
    ren_fichier = input("Entrer le fichier dont vous souhaiter renommer : ")
    nou_fichier = input("Entrer le nouveau du fichier : ")
    if os.path.exists(ren_fichier) and os.path.isfile(ren_fichier):
        if os.path.exists(nou_fichier) and os.path.isdir(nou_fichier):
            print("Erreur c'est un dossier ⛔ ✖️  ⛔")
        elif os.path.exists(nou_fichier) and os.path.isfile(nou_fichier):
            rep_fichier = input("Voulez - vous ecraser le fichier existant : oui? non? : ")
            while rep_fichier not in liste_rep:
                rep_fichier = input("Voulez - vous ecraser le fichier existant : oui? non? : ")
            if rep_fichier == "oui":
                os.replace(ren_fichier, nou_fichier)
                ("Fichier remplacé avec succès ✅ 🥳 🎉")
            else:
                print("Merci pour la confirmation ✅ 🥳 🎉")
        else:
            os.rename(ren_fichier, nou_fichier)
            print("Fichier renommé avec succès ✅ 🥳 🎉")
    else:
        print("Erreur de fichier ⛔ ✖️  ⛔")
def ajout():
    file_text = input("Entrer le nom du fichier : ")
    add_text = input("Entrer le nouveau contenu du fichier : ")
    if os.path.exists(file_text) and os.path.isfile(file_text):
        with open(file_text, "a") as f:
            f.write(add_text)
        print("Contenu ajouté avec succès ✅ 🥳 🎉")
    else:
        print("Erreur de fichier ⛔ ✖️  ⛔")
def vide():
    vid_fichier = input("Entrer le nom du fichier dont vous souhaitez vider : ")
    if os.path.exists(vid_fichier) and os.path.isfile(vid_fichier):
        with open(vid_fichier,"w") as f:
            f.truncate()
        print("fichier vidé avec succès ✅ 🥳 🎉")
    else:
        print("Erreur de fichier ⛔ ✖️  ⛔")
def copie():
    src_fichier = input("Entrer le fichier source : ")
    cpy_fichier = input("Entrer le fichier existant : ")
    if os.path.exists(src_fichier) and os.path.isfile(src_fichier):
        if os.path.exists(cpy_fichier) and os.path.isfile(cpy_fichier):
            shutil.copy2(src_fichier, cpy_fichier)
            print("Fichier copié avec succès ✅ 🥳 🎉")
        else:
            with open(cpy_fichier, "w") as f:
                shutil.copy2(src_fichier, cpy_fichier)
                print("Fichier copié avec succès ✅ 🥳 🎉")
                f.close()
    else:
        print("Erreur de fichier ⛔ ✖️  ⛔")
def recherche():
    rech_fichier = glob.glob("*txt")
    mot_rech = input("Entrer le contenu de votre fichier : ")
    liste_frech = [rech for rech in rech_fichier if os.path.isfile(rech)]
    print("Les fichiers recherchés : ")
    for frech in liste_frech:
        with open(frech, "r") as f:
            liste_rech = f.read().splitlines()    
        for line in liste_rech:
            if mot_rech in line:
                print(frech, " , ✅ 🥳 🎉")
    if mot_rech not in line:
        print("Fichier introuvable ⛔ ✖️  ⛔")
def createfolder():
    nom_dossier = input("Entrer le nom du dossier : ")
    if os.path.exists(nom_dossier):
        print("Ce dossier existe déjà ⛔ ✖️  ⛔")
    else:
        os.mkdir(nom_dossier)
        print("Dossier créé avec succès ✅ 🥳 🎉")
def removefolder():
    nom_dossier = input("Entrer le nom du dossier : ")
    if os.path.exists(nom_dossier) and os.path.isdir(nom_dossier):
        os.rmdir(nom_dossier)
        print("Dossier supprimé avec succès ✅ 🥳 🎉")
    else:
        print("Erreur de dossier ⛔ ✖️  ⛔")

while True:
    chx = menu()
    if chx == "1":
        creation()
    elif chx == "2":
        suppression()
    elif chx == "3":
        liste()
    elif chx == "4":
        lire()
    elif chx == "5":
        exit()
    elif chx == "6":
        renommer()  
    elif chx == "7":
        ajout()
    elif chx == "8":
        vide()
    elif chx == "9":
        copie()
    elif chx == "10":
        recherche()
    elif chx == "11":
        createfolder()
    else:
        removefolder()

           
