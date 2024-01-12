import os

def list_files(directory):
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

if __name__ == "__main__":
    # Utilisez os.path.join pour construire le chemin du répertoire
    directory_path = os.path.join("Fonctionnalités", "Principales")

    files = list_files(directory_path)
    print("Le dossier",directory_path,"à",len(files),"fichiers à ajouter.")

    with open(os.path.join("Fonctionnalités","listeFonctionnalite.tex"), "w") as f:
        for file in files:
            print( "Ajout du fichier",file )
            # Utilisez os.path.join pour construire le chemin complet du fichier
            f.write("\\input{Principales/" + file + "}\n")

