from Cryptodome.Cipher import DES


def pad(text):
    n = len(text) % 8
    return text + (b' ' * n)


def main():
    message = input("Input a message: ")

    while True:
        do_encrypt = input("Encrypt or decrypt the message? (Encrypt/Decrypt): ")
        if do_encrypt.lower().startswith("e", 0, 1) | do_encrypt.lower().startswith("d", 0, 1):
            break
        print("Please input a valid option,\neither Decrypt for decryption or Encrypt for encryption.")

    if do_encrypt.lower().startswith("e", 0, 1):
        des = DES.new(str.encode("abcdefgh"), DES.MODE_ECB)

        padded_text = pad(message)
        encrypted_text = des.encrypt(padded_text)
        print(encrypted_text)
        print("Encrypted with DES")
    else:
        des = DES.new(str.encode("abcdefgh"), DES.MODE_ECB)

        decrypted_text = des.decrypt(pad(message))
        print(decrypted_text)
        print("Decrypted with DES")
    main()


if __name__ == '__main__':
    main()
