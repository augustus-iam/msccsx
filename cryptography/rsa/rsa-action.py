import sys
DEFAULT_BLOCK_SIZE = 128
BYTE_SIZE = 256


def encrypt(plain_text):
    pubKeyFilename = 'RSA-demo_privkey.txt'

    encryptedText = encryptAndWriteToFile(plain_text, pubKeyFilename, DEFAULT_BLOCK_SIZE)
    return encryptedText


def decrypt(encrypted):
    privKeyFilename = 'RSA-demo_pubkey.txt'
    decryptedText = readFromFileAndDecrypt(encrypted, privKeyFilename)
    return decryptedText


def encryptMessage(message, key, blockSize=DEFAULT_BLOCK_SIZE):
    encryptedBlocks = []
    n, e = key

    for block in getBlocksFromText(message, blockSize):
        encryptedBlocks.append(pow(block, e, n))
    return encryptedBlocks

def encryptAndWriteToFile(messageFilename, keyFilename, message,blockSize=DEFAULT_BLOCK_SIZE):
    keySize, n, e = readKeyFile(keyFilename)

    if keySize < blockSize * 8:  # * 8 to convert bytes to bits
        sys.exit('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or less than the key size.Either increase the block size or use different keys. ' % (blockSize * 8, keySize))

    encryptedBlocks = encryptMessage(message, (n, e), blockSize)
    for i in range(len(encryptedBlocks)):
        encryptedBlocks[i] = str(encryptedBlocks[i])
    encryptedContent = ','.join(encryptedBlocks)

    encryptedContent = '%s_%s_%s' % (len(message), blockSize,encryptedContent)

    return encryptedContent

def main():
    message = input("Input a message: ")

    while True:
        do_encrypt = input("Encrypt or decrypt the message? (Encrypt/Decrypt): ")
        if do_encrypt.lower().startswith("e", 0, 1) | do_encrypt.lower().startswith("d", 0, 1):
            break
        print("Please input a valid option,\neither Decrypt for decryption or Encrypt for encryption.")

    if do_encrypt.lower().startswith("e", 0, 1):
        key = input("Input a Public key: ")
        print(encrypt(message, key))
        print("Encrypted with RSA")
    else:
        key = input("Input a Private key: ")
        print(decrypt(message, key))
        print("Decrypted with RSA")
    main()


if __name__ == '__main__':
    main()
