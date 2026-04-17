import csv

from caesar import caesar_encrypt


def encrypt_single_pass(filename: str) -> None:
    with open(filename, "r") as myfile:
        original_password = myfile.read().strip()
    encrypt_password = caesar_encrypt(original_password)
    with open(filename, 'w') as filemod:
        filemod.write(encrypt_password)

def encrypt_passwords_in_file(filename: str) -> None:
    with open(filename, mode='r') as thefile:
        reader = csv.reader(thefile)
        rows = [row for row in reader if row]
    for i in range(1, len(rows)):
        original_password = rows[i][2]
        rows[i][2] = caesar_encrypt(original_password)
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
        



def change_password(filename: str, website: str, password: str) -> bool:
    """TODO: Parte 3."""
    pass


def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    pass
