import os
import django
import shutil
from django.core.management import call_command

# Configurer l'environnement Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dernSol.settings')
django.setup()

# Supprimer la base de données existante
db_path = 'db.sqlite3'
if os.path.exists(db_path):
    os.remove(db_path)

# Supprimer les fichiers de migration existants
for root, dirs, files in os.walk('.'):
    if 'migrations' in dirs:
        migrations_dir = os.path.join(root, 'migrations')
        for migration_file in os.listdir(migrations_dir):
            if migration_file != '__init__.py':
                os.remove(os.path.join(migrations_dir, migration_file))

# Recréer les migrations et la base de données
call_command('makemigrations')
call_command('migrate')

# Créer un superutilisateur
print("Veuillez entrer les informations pour le superutilisateur :")
call_command('createsuperuser')
