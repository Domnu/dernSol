import os
import django
from django.contrib.auth import get_user_model

# Configuration de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dernSol.settings')
django.setup()


# Fonction pour créer un utilisateur
def create_user(email, password):
    User = get_user_model()
    user = User.objects.create_user(email=email, password=password)
    print(f"User created: {user.email}")


# Fonction pour créer un super utilisateur
def create_superuser(email, password):
    User = get_user_model()
    admin_user = User.objects.create_superuser(email=email, password=password)
    print(f"Superuser created: {admin_user.email}")


# Fonction pour vérifier les permissions d'un utilisateur
def check_user_permissions(email, perm):
    User = get_user_model()
    user = User.objects.get(email=email)
    has_permission = user.has_perm(perm)
    print(f"User {email} has permission {perm}: {has_permission}")


if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Create User")
        print("2. Create Superuser")
        print("3. Check User Permissions")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            email = input("Enter user email: ")
            password = input("Enter user password: ")
            create_user(email, password)

        elif choice == '2':
            email = input("Enter superuser email: ")
            password = input("Enter superuser password: ")
            create_superuser(email, password)

        elif choice == '3':
            email = input("Enter user email: ")
            perm = input("Enter permission to check (e.g., auth.add_user): ")
            check_user_permissions(email, perm)

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid option. Please try again.")
