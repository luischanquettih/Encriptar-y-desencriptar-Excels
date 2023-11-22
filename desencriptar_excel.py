from cryptography.fernet import Fernet

def decrypt_file(key, filename):
    cipher_suite = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_text = file.read()
    decrypted_text = cipher_suite.decrypt(encrypted_text)
    with open(filename.replace('.enc', '_decrypted.xlsx'), 'wb') as file:
        file.write(decrypted_text)

def main():
    key = b'2GDxt6vkGIoJgBkdSCoyqFgdC5oN4NM0py09rq0Ptko='  # Reemplaza con la clave generada previamente
    filename = 'datos.xlsx.enc'  # Cambia esto al nombre del archivo encriptado

    decrypt_file(key, filename)
    print(f"{filename} decrypted to {filename.replace('.enc', '_decrypted.xlsx')}")

if __name__ == "__main__":
    main()
