from base64 import b64encode, b64decode
import hashlib
from Cryptodome.Cipher import DES3


def encrypt(plain_text, password):
    # use the Scrypt KDF to get a private key from the password
    private_key = hashlib.scrypt(
        password.encode(), salt=str.encode("salt"), n=2 ** 14, r=8, p=1, dklen=32)

    # create cipher config
    cipher_config = DES3.new(private_key, DES3.MODE_ECB)

    # return a dictionary with the encrypted text
    cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
    return b64encode(cipher_text).decode('utf-8')


def decrypt(enc_dict, password):
    # decode the dictionary entries from base64
    cipher_text = b64decode(enc_dict['cipher_text'])
    nonce = b64decode(enc_dict['nonce'])
    tag = b64decode(enc_dict['tag'])

    # generate the private key from the password and salt
    private_key = hashlib.scrypt(
        password.encode(), salt=str.encode("salt"), n=2 ** 14, r=8, p=1, dklen=32)

    # create the cipher config
    cipher = DES3.new(private_key, DES3.MODE_ECB, nonce=nonce)

    # decrypt the cipher text
    decrypted = cipher.decrypt(cipher_text)

    return decrypted


def main():
    message = input("Input a message: ")
    key = input("Input a key: ")

    while True:
        do_encrypt = input("Encrypt or decrypt the message? (Encrypt/Decrypt): ")
        if do_encrypt.lower().startswith("e", 0, 1) | do_encrypt.lower().startswith("d", 0, 1):
            break
        print("Please input a valid option,\neither Decrypt for decryption or Encrypt for encryption.")

    if do_encrypt.lower().startswith("e", 0, 1):
        print(encrypt(message, key))
        print("Encrypted with DES3")
    else:
        print(decrypt(message, key))
        print("Decrypted with DES3")
    main()


if __name__ == '__main__':
    main()
