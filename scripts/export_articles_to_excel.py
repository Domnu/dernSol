import sqlite3
import pandas as pd

# Chemin vers votre base de données SQLite
db_path = 'H:\\dernSol\\db.sqlite3'

# Connexion à la base de données
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Requête SQL pour récupérer les articles de la table chat_article
query = "SELECT * FROM chat_article"

# Exécution de la requête
cursor.execute(query)

# Récupération des résultats
rows = cursor.fetchall()

# Récupération des noms de colonnes
columns = [description[0] for description in cursor.description]

# Fermeture de la connexion à la base de données
conn.close()

# Vérification des résultats obtenus
print("Colonnes :", columns)
print("Nombre de lignes récupérées :", len(rows))
print("Premières lignes récupérées :", rows[:5])

# Création d'un DataFrame pandas à partir des résultats
df = pd.DataFrame(rows, columns=columns)

# Chemin vers le fichier Excel de sortie
output_path = 'H:\\dernSol\\01_Archiv_dernSol\\articles.xlsx'

# Exportation des données vers une feuille Excel
df.to_excel(output_path, index=False)

print(f"Les articles ont été exportés avec succès vers {output_path}")
