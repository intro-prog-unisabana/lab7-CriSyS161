import csv

from caesar import caesar_encrypt


def encrypt_single_pass(filename: str) -> None:
    """TODO: Parte 1."""
    pass
    with open("filename", "r") as myfile:
        original_password = myfile.read()
    encrypt_password = caesar_encrypt(original_password)
    with open(myfile, 'w') as filemod:
        filemod.write(encrypt_password)
def encrypt_passwords_in_file(filename: str) -> None:
    """TODO: Parte 2."""
    pass


def change_password(filename: str, website: str, password: str) -> bool:
    """TODO: Parte 3."""
    pass


def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    """TODO: Parte 4."""
    pass
