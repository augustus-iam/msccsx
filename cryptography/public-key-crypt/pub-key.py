import onetimepad

def main():
    message = input("Input a message: ")

    while True:
        do_encrypt = input("Encrypt or decrypt the message? (Encrypt/Decrypt): ")
        if do_encrypt.lower().startswith("e", 0, 1) | do_encrypt.lower().startswith("d", 0, 1):
            break
        print("Please input a valid option,\neither Decrypt for decryption or Encrypt for encryption.")
    if do_encrypt.lower().startswith("e", 0, 1):
        cipher = onetimepad.encrypt(message, 'random')
        print(cipher)
    else:
        msg = onetimepad.decrypt(message, 'random')
        print(msg)
    main()


if __name__ == '__main__':
    main()