import hashlib
import getpass
import sqlite3
from rich.console import Console
from rich.table import Table

# Initialize the Rich console
console = Console()

def init_db():
    """
    Initialize the SQLite database and create the passwords table if it doesn't exist.
    The table includes columns for website, username, hashed password, security question, and security answer.
    """
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            id INTEGER PRIMARY KEY,
            website TEXT NOT NULL,
            username TEXT NOT NULL,
            hashed_password TEXT NOT NULL,
            security_question TEXT NOT NULL,
            security_answer TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def get_hashed_password(password):
    """
    Generate a SHA-256 hashed password.

    Args:
        password (str): The plaintext password to hash.

    Returns:
        str: The hashed password.
    """
    sha256_hash = hashlib.sha256()
    sha256_hash.update(password.encode('utf-8'))
    return sha256_hash.hexdigest()

def create_password():
    """
    Create a new password entry by asking the user for website, username, password, security question, and answer.
    The password is hashed before storing it in the database along with the other details.
    """
    website = input("Enter the website: ")
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = get_hashed_password(password)
    
    security_question = input("Enter a security question: ")
    security_answer = input("Enter the answer to your security question: ")

    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO passwords (website, username, hashed_password, security_question, security_answer)
        VALUES (?, ?, ?, ?, ?)
    ''', (website, username, hashed_password, security_question, security_answer))
    conn.commit()
    conn.close()
    console.print("[green]Password created successfully.[/green]")

def retrieve_password():
    """
    Retrieve a password entry by asking the user for the website.
    The user is given an option to either enter their password or answer a security question if they forgot their password.
    If the details match, the stored information is displayed.
    """
    website = input("Enter the website: ")
    
    conn = sqlite3.connect('passwords.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT username, hashed_password, security_question, security_answer FROM passwords WHERE website = ?
    ''', (website,))
    row = cursor.fetchone()
    conn.close()
    
    if row:
        username, stored_hashed_password, security_question, stored_security_answer = row
        choice = input("Did you forget your password? (yes/no): ").strip().lower()
        if choice == 'yes':
            console.print(f"Security Question: {security_question}")
            security_answer = input("Enter your security answer: ")
            if security_answer == stored_security_answer:
                table = Table(title="Retrieved Password")
                table.add_column("Website", justify="center", style="cyan", no_wrap=True)
                table.add_column("Username", justify="center", style="magenta")
                table.add_column("Password", justify="center", style="green")

                table.add_row(website, username, "[REDACTED - Reset your password securely]")
                console.print(table)
            else:
                console.print("[red]Incorrect security answer.[/red]")
        else:
            password = getpass.getpass("Enter your password to confirm retrieval: ")
            if stored_hashed_password == get_hashed_password(password):
                table = Table(title="Retrieved Password")
                table.add_column("Website", justify="center", style="cyan", no_wrap=True)
                table.add_column("Username", justify="center", style="magenta")
                table.add_column("Password", justify="center", style="green")

                table.add_row(website, username, password)
                console.print(table)
            else:
                console.print("[red]Incorrect password.[/red]")
    else:
        console.print("[red]Website not found in the password manager.[/red]")

def main():
    """
    The main function initializes the database and provides a menu for the user to create a new password,
    retrieve an existing password, or quit the application.
    """
    init_db()
    while True:
        console.print("1. Create a new password", style="bold blue")
        console.print("2. Retrieve a password", style="bold blue")
        console.print("3. Quit", style="bold blue")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            create_password()
        elif choice == "2":
            retrieve_password()
        elif choice == "3":
            break
        else:
            console.print("[red]Invalid choice. Please try again.[/red]")

if __name__ == "__main__":
    main()
