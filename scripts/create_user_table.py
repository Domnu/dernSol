import sqlite3
import os


def create_user_table(db_path):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS "auth_user" (
        "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        "password" VARCHAR(128) NOT NULL,
        "last_login" DATETIME,
        "is_superuser" BOOL NOT NULL,
        "username" VARCHAR(150) NOT NULL UNIQUE,
        "last_name" VARCHAR(150) NOT NULL,
        "email" VARCHAR(254) NOT NULL,
        "is_staff" BOOL NOT NULL,
        "is_active" BOOL NOT NULL,
        "date_joined" DATETIME NOT NULL,
        "first_name" VARCHAR(150) NOT NULL
    );
    """
    if not os.path.isfile(db_path):
        raise FileNotFoundError(f"The database file at {db_path} does not exist.")

    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        conn.commit()


if __name__ == "__main__":
    db_path = input("Enter the full path to your SQLite database file (including the file name): ")
    # Enter this path: H:\dernSol\db.sqlite3
    try:
        create_user_table(db_path)
        print("auth_user table created successfully.")
    except FileNotFoundError as e:
        print(e)
    except sqlite3.OperationalError as e:
        print(f"An error occurred: {e}")
