import random
import string


def shift(current_position, distance, direction: (0, 1)):
    direction = 1 if direction else -1
    return current_position + direction * distance


def stream_cipher(message, key, do_encrypt=True):
    random.seed(key)
    # The character set must be multiplied by 2 so
    # a character shifted beyond the end of the
    # character set will loop back to the beginning.
    characters = 2 * (
            string.ascii_letters +
            string.digits +
            string.punctuation + ' '
    )
    # I declare this in a variable so the
    # program can work with a variable length character set
    lenchars = len(characters)
    # This will replace each character in the message
    # with a pseudo-random character selected from
    # the character set.

    print(''.join(
        [characters[
             shift(
                 characters.index(message[each_char]), lenchars - int(lenchars * random.random()), do_encrypt
             )
         ]
         for each_char in range(len(message))]))
    if do_encrypt:
        print("Encrypted with Stream Cipher")
    else:
        print("Decrypted with Stream Cipher")


def main():
    message = input("Input a message: ")
    key = input("Input a key: ")
    while True:
        do_encrypt = input("Encrypt or decrypt the message? (Encrypt/Decrypt): ")
        if do_encrypt.lower().startswith("e", 0, 1) | do_encrypt.lower().startswith("d", 0, 1):
            break
        print("Please input a valid option,\neither Decrypt for decryption or Encrypt for encryption.")
    if do_encrypt.lower().startswith("e", 0, 1):
        stream_cipher(message, key, True)
    else:
        stream_cipher(message, key, False)
    main()


if __name__ == '__main__':
    main()
