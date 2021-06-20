def reverse(enc_dict):
    translated = ''

    i = len(enc_dict) - 1
    while i >= 0:
        translated = translated + enc_dict[i]
        i = i - 1

    return translated


def main():
    message = input("Input a message(e to exit): ")

    if message.lower().startswith("e", 0, 1) & len(message) == 1:
        print("Bye.")
        exit()
    else:
        print(reverse(message))


main()

if __name__ == '__main__':
    main()
