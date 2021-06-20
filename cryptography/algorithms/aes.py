from base64 import b64encode, b64decode
import hashlib
from Cryptodome.Cipher import AES


def encrypt(plain_text, password):
    private_key = hashlib.scrypt(
        password.encode(), salt=str.encode("salt"), n=2 ** 14, r=8, p=1, dklen=32)

    # create cipher config
    cipher_config = AES.new(private_key, AES.MODE_GCM)

    # return a dictionary with the encrypted text
    cipher_text, tag = cipher_config.encrypt_and_digest(bytes(plain_text, 'utf-8'))
    return b64encode(cipher_text).decode('utf-8')


def decrypt(enc_dict, password):
    cipher_text = b64decode(enc_dict['cipher_text'])
    nonce = b64decode(enc_dict['nonce'])
    tag = b64decode(enc_dict['tag'])

    # generate the private key from the password and salt
    private_key = hashlib.scrypt(
        password.encode(), salt=str.encode("salt"), n=2 ** 14, r=8, p=1, dklen=32)

    # create the cipher config
    cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)

    # decrypt the cipher text
    decrypted = cipher.decrypt_and_verify(cipher_text, tag)

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
        print("Encrypted with AES")
    else:
        print(decrypt(message, key))
        print("Decrypted with AES")
    main()


if __name__ == '__main__':
    main()
