from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()

def encrypt_file(key, filename):
    cipher_suite = Fernet(key)
    with open(filename, 'rb') as file:
        plaintext = file.read()
    encrypted_text = cipher_suite.encrypt(plaintext)
    with open(filename + '.enc', 'wb') as file:
        file.write(encrypted_text)

def main():
    key = generate_key()
    print(f"Generated Key: {key.decode()}")

    filename = 'datos.xlsx' # colocar la ruta del archivo

    encrypt_file(key, filename)
    print(f"{filename} encrypted to {filename}.enc")

if __name__ == "__main__":
    main()
