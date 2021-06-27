import sys

DEFAULT_BLOCK_SIZE = 128
BYTE_SIZE = 256


def encrypt(plain_text, pubKeyFilename):

    keySize, n, e = readKeyFile(pubKeyFilename)

    if keySize < DEFAULT_BLOCK_SIZE * 8:  # * 8 to convert bytes to bits
        sys.exit(
            'ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or less than the key size.Either increase the block size or use different keys. ' % (
                DEFAULT_BLOCK_SIZE * 8, keySize))

    encryptedBlocks = encryptMessage(plain_text, (n, e), DEFAULT_BLOCK_SIZE)

    for i in range(len(encryptedBlocks)):
        encryptedBlocks[i] = str(encryptedBlocks[i])
    encryptedContent = ','.join(encryptedBlocks)

    encryptedContent = '%s_%s_%s' % (len(plain_text), DEFAULT_BLOCK_SIZE, encryptedContent)

    return encryptedContent


def decrypt(encrypted, privKeyFilename):
    decryptedText = readFromFileAndDecrypt(encrypted, privKeyFilename)
    return decryptedText


def readFromFileAndDecrypt(messageFilename, keyFilename):
    # Using a key from a key file, read an encrypted message from a file
    # and then decrypt it. Returns the decrypted message string.
    keySize, n, d = readKeyFile(keyFilename)

    # Read in the message length and the encrypted message from the file.
    fo = open(messageFilename)
    content = fo.read()
    messageLength, blockSize, encryptedMessage = content.split('_')
    messageLength = int(messageLength)
    blockSize = int(blockSize)

    # Check that key size is greater than block size.
    if keySize < blockSize * 8:  # * 8 to convert bytes to bits
        sys.exit(
            'ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or less than the key size.Did you specify the correct key file and encrypted file?' % (
                blockSize * 8, keySize))

        # Convert the encrypted message into large int values.

        encryptedBlocks = []

        for block in encryptedMessage.split(','):
            encryptedBlocks.append(int(block))

        # Decrypt the large int values.

    return decryptMessage(encryptedBlocks, messageLength, (n, d),
                          blockSize)


def encryptMessage(message, key, blockSize=DEFAULT_BLOCK_SIZE):
    encryptedBlocks = []
    n, e = key

    for block in getBlocksFromText(message, blockSize):
        encryptedBlocks.append(pow(block, e, n))
    return encryptedBlocks


def getBlocksFromText(message, blockSize=DEFAULT_BLOCK_SIZE):
    # Converts a string message to a list of block integers. Each integer
    # represents 128 (or whatever blockSize is set to) string characters.

    messageBytes = message.encode('ascii')  # convert the string to bytes

    blockInts = []
    for blockStart in range(0, len(messageBytes), blockSize):

        blockInt = 0
        for i in range(blockStart, min(blockStart + blockSize,
                                       len(messageBytes))):
            blockInt += messageBytes[i] * (BYTE_SIZE ** (i % blockSize))
        blockInts.append(blockInt)
    return blockInts


def getTextFromBlocks(blockInts, messageLength,
                      blockSize=DEFAULT_BLOCK_SIZE):
    # Converts a list of block integers to the original message string.
    # The original message length is needed to properly convert the last
    # block integer.
    message = []
    for blockInt in blockInts:
        blockMessage = []
    for i in range(blockSize - 1, -1, -1):
        if len(message) + i < messageLength:
            asciiNumber = blockInt // (BYTE_SIZE ** i)
            blockInt = blockInt % (BYTE_SIZE ** i)
            blockMessage.insert(0, chr(asciiNumber))
        message.extend(blockMessage)
    return ''.join(message)


def readKeyFile(keyFilename):
    content = keyFilename
    keySize, n, EorD = content.split(',')
    return (int(keySize), int(n), int(EorD))


def main():
    message = input("Input a message: ")

    while True:
        do_encrypt = input("Encrypt or decrypt the message? (Encrypt/Decrypt): ")
        if do_encrypt.lower().startswith("e", 0, 1) | do_encrypt.lower().startswith("d", 0, 1):
            break
        print("Please input a valid option,\neither Decrypt for decryption or Encrypt for encryption.")

    if do_encrypt.lower().startswith("e", 0, 1):
        key = input("Input a Public key: ")
        print(encrypt(message))
        print("Encrypted with RSA")
    else:
        key = input("Input a Private key: ")
        print(decrypt(message))
        print("Decrypted with RSA")
    main()


if __name__ == '__main__':
    main()
